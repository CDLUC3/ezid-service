---
name: Transfer to DataCite
about: Template for transferring EZID account to DataCite
title: ''
labels: ''
assignees: ''

---

**Account information**
Prefix(es):
NAAN(s):
EZID username(s):
EZID Group(s): 
DataCite data center(s): 
Number of DOIs (number reserved):
Number of ARKs:

**Steps**
- [ ] 1. Disable user account(s) (Maria)

- [ ] 2. Move identifiers (DataCite/Crossref)

- [ ] 3. Delete datacenter in Fabrica (Maria)

- [ ] 4. “Unhook" shoulders from EZID user(s) and group (Rushiraj)

- [ ] 5. Run “delete user” script (Rushiraj) (this will delete the identifiers)

- [ ] 6. Delete group if last user in group (Rushiraj)

- [ ] 7. Remove datacenter in master_shoulders.txt (if no longer in use) (John)

- [ ] 8. If a shoulder is no longer meant to be used to create new ids by this user or any other user, remove minter, if any. (John)

- [ ] 9. Move shoulder and datacenter entries from master_shoulders.txt to former_shoulders.txt. (John)

- [ ] 10. Move NAAN entry, if relevant, from master_naans to former_naans. (John)

- [ ] 11. Add NAAN, as relevant (copied from previous step), to end of commented recycling list near top of former_naans. (John) 

- [ ] 12. Remove client from (a) EZID-L mailing list, (b) client list at https://ezid.cdlib.org/learn/#02, (c) Crossref notification emails, as appropriate (Maria)
