---
name: Maintenance account
about: Template for moving accounts into a maintenance status
title: ''
labels: ''
assignees: ''

---

Account information
NAAN: 
EZID account name(s): 
EZID user:
EZID group(s):
DataCite data center(s): 
Number of DOIs (number reserved): 
Number of ARKs:

1. Disable login (Maria)

2a. If DataCite DOI, move PIDs to CDL.CDL datacenter (Maria)

2b. If DataCite DOI, delete old client datacenter in Fabrica (if applicable) (Maria)

3. Move PIDs to cdl_nonpaying group (Rushiraj)

4. Move user to cdl_nonpaying group (Rushiraj)

5. Rename the original group to *_nonpaying (Rushiraj)

6. Add "active: false" flag to shoulder entry in master_shoulders.txt. (John)

7. Associate the shoulder with CDL.CDL datacenter in master_shoulders.txt (John)

8. Remove datacenter in master_shoulders.txt (if no longer in use) (John)
