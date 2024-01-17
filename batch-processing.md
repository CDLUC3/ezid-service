# Batch processing
EZID's batch processing functions are helpful for registering or updating a high volume of identifiers at once. 

Full technical documentation is in the [EZID API documentation](https://ezid-stg.cdlib.org/doc/apidoc.html) and [EZID client tools repo](https://github.com/CDLUC3/ezid-client-tools). 

## Prerequisites
- Cloned client tools repository on your local machine
- Terminal window
- Mapping file that corresponds to the metadata you will be registering
- csv of identifier metadata that corresponds to the mapping file
- The latest batch procesing script (should be in the client tools repo - check with a developer if you are not sure)

## Notes
- VPN access is not required
- Username and password are required - use the credentials for whichever account will be associated with the identifiers
- The mapping file and csv are dynamic, meaning they will be different for each batch process depending on the types of identifiers you are registering (e.g., ARKs vs DOIs) and the metadata you are registering with each identifier
- Make sure all of your files, including the csv, are in your local client tools folder

## Example command
`python batch-register.py -c username:password -p -s doi:10.5072/FK2 mint mappings batchtest.csv`

In the above scenario, the command will `mint` DOIs on the shoulder `doi:10.5072/FK2` based on metadata provided in the file `batchtest.csv` whose metadata fields correspond to the information in the file called `mappings`, and the command will run based on the information in the script `batch-register.py`. The identifiers will be associated in the user account associated with whichever credentials are used instead of "username" and "password".

**Other notes about the above scenario:**
- `-c` = the credentials being supplied
- `p` = preview, shows a preview of the metadata (remove for final operation)
- `s` = shoulder where the DOIs will be minted 
- `mint` = operation (can also be `create` or `update`)

Check the preview of the results to make sure they look good. If everything looks good and no errors, run the registration command again without the p parameter:  `python batch-register.py -c username:password  -s doi:10.5072/FK2 mint mappings batchtest.csv`

The results will output in the Terminal window. If you want to output a csv of the identifiers, you can specify that at the end of the command and it will dump the identifiers into a csv on your machine, e.g.:

`python batch-register.py -c username:password  -s doi:10.5072/FK2 mint mappings batchtest.csv >> results.csv`

## Example scenario 1: batch processing ARKs
Given a hypothetical scenario where a batch of ARKs are being created (meaning, the identifier strings will be specified as part of the operation), the command would look something like this:

`python3 batch-register.py -c username:password create arkmapping ucla-batch-test.csv`

See the example mapping file [here](https://github.com/CDLUC3/ezid-service/blob/master/arkmapping)

See the example csv [here](https://github.com/CDLUC3/ezid-service/blob/master/ucla-batch-test.csv)

## Example scenario 2: batch processing DOIs
Given a hypothetical scenario in which a batch of grant DOIs are being registered, the command would look something like this:

`python3 batch-register.py -c username:password mint -s doi:10.5072/FK2 map test-grants2.csv`

See the example mapping file [here](https://github.com/CDLUC3/ezid-service/blob/master/map)

See the example csv [here](https://github.com/CDLUC3/ezid-service/blob/master/test-grants2.csv)

## Other possible scenarios

**To update existing identifiers:**
- The spreadsheet needs to have a column for id
- Use the `update` command instead of `mint` or `create`

**To batch process Crossref DOIs:**
- The spreadsheet needs to include Crossref XML (entire blob inside a single cell)





