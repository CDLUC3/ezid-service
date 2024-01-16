import argparse
import base64
import csv
import getpass
import traceback
import re
import sys
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse

# We'd prefer to use LXML, but stick with the inferior built-in
# library for better portability.
import xml.etree.ElementTree


def loadMappings(file):
    # returns: [(destination, expression), ...]
    m = []
    with open(file) as f:
        n = 0
        for l in f:
            n += 1
            try:
                assert "=" in l, "invalid syntax"
                d, e = [v.strip() for v in l.split("=", 1)]
                if d.startswith("/"):
                    assert re.match(
                        "/resource(/\w+)+(@\w+)?$", d
                    ), "invalid absolute XPath expression"
                else:
                    assert re.match("[.\w]+$", d), "invalid element name"
                m.append((d, e))
            except Exception as e:
                assert False, "%s, line %d: %s" % (file, n, str(e))
    return m


def parseOutputColumns(columns, mappings):
    # columns: "element,1,2,..."
    # mappings: [(destination, expression), ...]
    # returns: ["element", 0, 1, ...]
    elements = [d for d, e in mappings if not d.startswith("/")] + [
        "_n",
        "_id",
        "_error",
    ]
    l = []
    for c in columns.split(","):
        try:
            i = int(c)
            # We'll check the upper bound on the column reference after
            # reading the first input row.
            assert i > 0, "argument -o: invalid input column reference"
            l.append(i - 1)
        except ValueError:
            assert c in elements, "argument -o: no such output element: " + c
            l.append(c)
    return l


def interpolate(expression, row):
    # expression: string in which $n, ${n}, ${n:f}, $$ will be interpolated
    # row: [value1, value2, ...]
    # returns: string or complex object
    v = ""
    i = 0
    for m in re.finditer("\$(?:\d+|{\d+}|{\d+(?:,\d+)*:\w+}|\$)", expression):
        v += expression[i : m.start()]
        try:
            if m.group(0) == "$$":
                v += "$"
            elif m.group(0).startswith("${"):
                if ":" in m.group(0):
                    cols, f = m.group(0)[2:-1].split(":")
                    args = [row[int(c) - 1] for c in cols.split(",")]
                    try:
                        import functions

                        r = getattr(functions, f)(*args)
                        if isinstance(r, str):
                            v += r
                        else:
                            # We allow a function to return a complex object only if
                            # the expression consists of the function reference and
                            # nothing more--- and in this case, the object can be
                            # returned immediately.
                            assert m.group(0) == expression, (
                                "unsupported interpolation: "
                                + "function returned complex object but there is "
                                + "other text in expression"
                            )
                            return r
                    except Exception as e:
                        assert False, "error calling user-supplied function %s: %s" % (
                            f,
                            str(e),
                        )
                else:
                    v += row[int(m.group(0)[2:-1]) - 1]
            else:
                v += row[int(m.group(0)[1:]) - 1]
        except IndexError:
            assert False, "input column reference exceeds number of columns"
        i = m.end()
    v += expression[i:]
    return v.strip()


def setDataciteValue(node, path, value):
    # node: XML node or None
    # path: "/resource/abspath@attribute" or "relpath@attribute"
    # value: string or complex object
    # returns: node if node was supplied, else root node
    def q(tag):
        return "{http://datacite.org/schema/kernel-4}" + tag

    if type(value) is tuple:
        value = [value]
    if type(value) is list:
        if len(value) == 0:
            return node
        assert all(
            type(v) is tuple and len(v) == 2 and isinstance(v[0], str) for v in value
        ), (
            "invalid return value from user-supplied function: "
            + "malformed list or tuple"
        )
        assert all(re.match("(\w+|[.])(/(\w+|[.]))*(@\w+)?$", v[0]) for v in value), (
            "invalid return value from user-supplied function: "
            + "invalid relative XPath expression"
        )
    elif isinstance(value, str):
        value = value.strip()
        if value == "":
            return node
    else:
        assert False, "invalid return value from user-supplied function"
    p = path[10 if path.startswith("/resource/") else 0 :].split("/")
    a = None
    if "@" in p[-1]:
        p[-1], a = p[-1].split("@")
    if node == None:
        node = xml.etree.ElementTree.Element(q("resource"))
        node.attrib["{http://www.w3.org/2001/XMLSchema-instance}schemaLocation"] = (
            "http://datacite.org/schema/kernel-4 "
            + "http://schema.datacite.org/meta/kernel-4/metadata.xsd"
        )
        n = xml.etree.ElementTree.SubElement(node, q("identifier"))
        n.attrib["identifierType"] = "(:tba)"
        n.text = "(:tba)"
    n = node
    for i, e in enumerate(p):
        if e != ".":
            # If we're at the terminal element of the path and we're not
            # setting an attribute, we always add a new child element.
            if i == len(p) - 1 and a == None:
                c = None
            else:
                c = n.find(q(e))
            if c != None:
                n = c
            else:
                n = xml.etree.ElementTree.SubElement(n, q(e))
    if a != None:
        assert isinstance(value, str), (
            "unsupported interpolation: attribute %s requires string value" % a
        )
        n.attrib[a] = value
    else:
        if isinstance(value, str):
            n.text = value
        else:
            for relpath, v in value:
                setDataciteValue(n, relpath, v)
    return node


def transform(args, mappings, row):
    # mappings: [(destination, expression), ...]
    # row: [value1, value2, ...]
    # returns: metadata dictionary
    md = {}
    dr = None
    for i, (d, e) in enumerate(mappings):
        try:
            v = interpolate(e, row)
            if d.startswith("/"):
                dr = setDataciteValue(dr, d, v)
            else:
                assert isinstance(v, str), (
                    "unsupported interpolation: "
                    + "user-supplied function must return string value in mapping to "
                    + "EZID metadata element"
                )
                md[d] = v
        except AssertionError as err:
            assert False, "%s, line %d: %s" % (args.mappingsFile, i + 1, str(err))
    if dr != None:
        if args.operation == "mint":
            s = args.shoulder
        else:
            s = md["_id"]
        dr.findall("*[@identifierType]")[0].attrib["identifierType"] = (
            "ARK" if s.startswith("ark:/") else "DOI"
        )
        md["datacite"] = (xml.etree.ElementTree.tostring(dr)).decode("UTF-8")
    return md


def toAnvl(record):
    # record: metadata dictionary
    # returns: string
    def escape(s, colonToo=False):
        if colonToo:
            p = "[%:\r\n]"
        else:
            p = "[%\r\n]"
        return re.sub(p, lambda c: "%%%02X" % ord(c.group(0)), str(s))

    return "".join(
        "%s: %s\n" % (escape(k, True), escape(record[k])) for k in sorted(record.keys())
    )


def process1(args, record):
    # record: metadata dictionary
    # returns: (identifier or None, "error: ..." or None)
    # N.B.: _id is removed from record
    if args.operation == "mint":
        id = None
        if args.removeIdMapping and "_id" in record:
            del record["_id"]

        r = urllib.request.Request(
            "https://ezid.cdlib.org/shoulder/" + urllib.parse.quote(args.shoulder, ":/")
        )
    else:
        id = str(record["_id"])
        del record["_id"]
        r = urllib.request.Request(
            "https://ezid.cdlib.org/id/" + urllib.parse.quote(id, ":/")
        )
        r.get_method = lambda: "PUT" if args.operation == "create" else "POST"
    s = toAnvl(record).encode("UTF-8")
    r.data = s
    r.add_header("Content-Type", "text/plain; charset=UTF-8")
    r.add_header("Content-Length", str(len(s)))
    if args.cookie != None:
        r.add_header("Cookie", args.cookie)
    else:
        r.add_header(
            "Authorization",
            "Basic "
            + base64.b64encode(
                (args.username + ":" + args.password).encode("utf-8")
            ).decode("utf-8"),
        )
    c = None
    try:
        c = urllib.request.urlopen(r)
        s = c.read().decode("UTF-8")
        assert s.startswith("success:"), s
        return (s[8:].split()[0], None)
    except urllib.error.HTTPError as e:
        if e.fp != None:
            s = e.fp.read().decode("UTF-8")
            if not s.startswith("error:"):
                s = "error: " + s
            return (id, s)
        else:
            return (id, "error: %d %s" % (e.code, e.msg))
    except Exception as e:
        return (id, "error: " + str(e))
    finally:
        if c != None:
            c.close()


def formOutputRow(args, row, record, recordNum, id, error):
    # row: [value1, value2, ...]
    # record: metadata dictionary
    # id: identifier or None
    # error: error message or None
    # returns: list
    l = []
    for c in args.outputColumns:
        if type(c) is int:
            l.append(row[c])
        else:
            if c == "_n":
                l.append(str(recordNum))
            elif c == "_id":
                l.append(id or "")
            elif c == "_error":
                l.append(error or "")
            else:
                l.append(record[c])
    return l


def process(args, mappings):
    class StrictTabDialect(csv.Dialect):
        delimiter = "\t"
        quoting = csv.QUOTE_NONE
        doublequote = False
        lineterminator = "\r\n"

    w = csv.writer(sys.stdout)
    n = 0
    for row in csv.reader(
        open(args.inputFile), dialect=(StrictTabDialect if args.tabMode else csv.excel)
    ):
        n += 1
        if n == 1:
            numColumns = len(row)
            assert (
                max([-1] + [c for c in args.outputColumns if type(c) is int])
                < numColumns
            ), "argument -o: input column reference exceeds number of columns"
        try:
            assert len(row) == numColumns, "inconsistent number of columns"
            row = [c for c in row]
            record = transform(args, mappings, row)
            if args.previewMode:
                sys.stdout.write("\n")
                sys.stdout.write(toAnvl(record))
            else:
                id, error = process1(args, record)
                w.writerow([c for c in formOutputRow(args, row, record, n, id, error)])
                sys.stdout.flush()
        except Exception as e:
            assert False, "record %d: %s" % (n, str(e))


def main():
    def validateShoulder(s):
        if not (s.startswith("ark:/") or s.startswith("doi:")):
            raise argparse.ArgumentTypeError("invalid shoulder")
        return s

    p = argparse.ArgumentParser(description="Batch registers identifiers.")
    p.add_argument(
        "operation", choices=["create", "mint", "update"], help="operation to perform"
    )
    p.add_argument("mappingsFile", metavar="mappings", help="configuration file")
    p.add_argument("inputFile", metavar="input.csv", help="input metadata in CSV form")
    p.add_argument(
        "-c",
        metavar="CREDENTIALS",
        dest="credentials",
        help="either username:password, or just username (password will be "
        + "prompted for), or session=... (as obtained by using the "
        + "EZID client tool)",
    )
    p.add_argument(
        "-o",
        metavar="COLUMNS",
        dest="outputColumns",
        default="_n,_id,_error",
        help="comma-separated list of columns to output, defaults to "
        + "_n,_id,_error",
    )
    p.add_argument(
        "-p",
        dest="previewMode",
        action="store_true",
        help="preview mode: don't register identifiers, instead, write "
        + "transformed metadata to standard output",
    )
    p.add_argument(
        "-r",
        dest="removeIdMapping",
        action="store_true",
        help="remove any mapping to _id; useful when temporarily minting",
    )
    p.add_argument(
        "-s",
        metavar="SHOULDER",
        dest="shoulder",
        type=validateShoulder,
        help="the shoulder to mint under, e.g., ark:/99999/fk4",
    )
    p.add_argument(
        "-t",
        dest="tabMode",
        action="store_true",
        help="tab mode: the input metadata is tab-separated (multiline values "
        + "and tab characters in values are not supported)",
    )
    args = p.parse_args(sys.argv[1:])
    if not args.previewMode:
        assert args.credentials != None, "operation requires -c argument"
    if args.operation == "mint":
        assert args.shoulder != None, "operation requires -s argument"
    mappings = loadMappings(args.mappingsFile)
    if args.operation in ["create", "update"]:
        assert "_id" in [d for d, e in mappings], "operation requires mapping to _id"
    args.outputColumns = parseOutputColumns(args.outputColumns, mappings)
    if not args.previewMode:
        if args.credentials.startswith("sessionid="):
            args.cookie = args.credentials
        else:
            args.cookie = None
            if ":" in args.credentials:
                args.username, args.password = args.credentials.split(":", 1)
            else:
                args.username = args.credentials
                args.password = getpass.getpass()
    process(args, mappings)


try:
    main()
except Exception as e:
    print((traceback.format_exc()))
    sys.stderr.write("%s: error: %s\n" % (sys.argv[0].split("/")[-1], str(e)))
    sys.exit(1)
