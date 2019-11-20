---
name: Configure new shoulder/account in EZID
about: Template for configuring new shoulder/account in EZID
title: 'New account/shoulder:'
labels: New account/shoulder
assignees: ''

---

# Information to send to dev:
EZID prefix/shoulder: doi:10.1234/X5 OR ark:/12345/x5
Account/organization username (login): ezid-admin
Shoulder display name: EZID Admin
Datacenter: CDL.ABC (or leave blank if Crossref prefix or ARK)

# Information to collect from requestor:
Requestor name:
Campus:
Is this request for an eScholarship journal?	
(if eScholarship): Publication title:
Is this request for ARKs or DOIs?	
Primary account contact:	
Primary email address associated with this account:	
Secondary account contact (optional):
How are you planning to use ARKs/DOIs?

#Tasks & steps
Liaison/admin requests a new shoulder (via Google Form) and provides details about what they need (ARKs or DOIs, etc.)

Maria receives request and determines course of action depending on what is requested
NAAN: Fill out NAAN request form (https://n2t.net/e/naan_request) on behalf of user
DataCite prefix: Assign new prefix in Fabrica from list of available prefixes
Crossref prefix: Email Crossref to request new prefix

Maria chooses a short shoulder if user has not requested a specific one (follow existing conventions at https://ezid.cdlib.org/learn/id_concepts)
Default shoulder selection: pick one letter and one digit (not 0 or 1).
To pick letter (for DOI or ARK shoulder), start with a non-vowel, non-ell (inflexible) letter from the org acronym.
To pick the DOI shoulder digit, start with last prefix digit (flexible)
To pick the ARK shoulder digit, start with second to last prefix digit (flexible)

Maria sets up Github issue using new account/shoulder template and assign to Rushiraj

Rushiraj runs a script to generate the shoulder entry on EZID

Rushiraj runs ./install-shoulders and ./reload-all in EZID to install in stg and prod

Rushiraj notifies Maria that shoulder is ready

Maria configures shoulder/account in EZID

Add new shoulder to appropriate group
Set up new user account if applicable
Give user account access to shoulder
Maria notifies user that shoulder is ready
