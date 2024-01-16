# Crossref accounts in EZID

## Overview
Crossref DOIs are supported in EZID along with DataCite DOIs but there are important differences in terms of how Crossref DOIs are registered and how Crossref accounts are configured. This guide provides documentation about working with Crossref accounts in EZID. 

If questions arise about EZID and Crossref, consult with the PAD team and with Crossref support as needed. 

## Users of EZID's Crossref services
Currently, usage of EZID's Crossref services is limited to:

- CDL PAD team and the journals and preprints they support on the eScholarship and Janeway platforms
- San Francisco Estuary and Watershed Science (SFEWS)

## PAD team requests
Supporting the PAD team's shoulder requests typically happen through the following scenarios:

- [Setting up a new journal with DOIs for the first time](#setting-up-a-new-journal-with-DOIs-for-the-first-time) (most common)
- [Setting up a journal in EZID that already has DOIs](#setting-up-a-journal-in-EZID-that-already-has-DOIs) (not as common)
- [Setting up a journal with an independent Crossref account](#setting-up-a-journal-with-an-independent-Crossref-account) (uncommon)

### Setting up a new journal with DOIs for the first time
When the PAD team is setting up a new journal or preprint platform with DOIs for the first time, they will get in touch with the EZID Service Manager (typically via Slack or check-in meeting) and enter information about the request in [this tracking sheet](https://docs.google.com/spreadsheets/d/1BP-_clMt5QL5QHJLmHzyeTNHlAsizXGI6vPZq4FReWc/edit#gid=0).

**Questions to confirm with the PAD team are:**
- Which campus is this publication associated with?
- Will the DOIs be registered on CDL's 10.5070 prefix or a different one (10.5070 is the default scenario)

**To set up a journal/preprint account:**

1. Set up a new Crossref shoulder following the guidance in the [Creating and managing shoulders guide](https://github.com/CDLUC3/ezid-service/blob/master/creating-and-managing-shoulders.md)
   
2. Add the shoulder to the relevant campus group in EZID:
- `ucblibrary` (Berkeley)
- `ucd-library` (Davis)
- `uci` (Irvine)
- `ucla-library` (UCLA)
- `ucmlibrary` (Merced)
- `ucrlibrary` (Riverside)
- `ucsdlib` (San Diego)
- `ucsf` (UCSF)
- `sb-lib` (Santa Barbara)
- `ucsc-lib` (Santa Cruz)


3. Add the shoulder to the `eschol_harvester` group in EZID
   
4. Add the shoulder to the relevant campus eSchol user account in EZID:
- `ucb-eschol`
- `ucd-eschol`
- `uci-eschol`
- `ucla-eschol`
- `ucm-eschol`
- `ucr-eschol`
- `ucsd_eschol`
- `ucsf-eschol`
- `sb-eschol`
- `ucsc-eschol`

5. Make sure that the shoulder is also added to the `eschol_harvester` user account and relevant campus library account (this should happen automatically)
   
7. Notify the PAD team that the shoulder is ready to be used

### Setting up a journal in EZID that already has DOIs
In some cases, the PAD team takes over a journal or preprint server that previously had its own Crossref membership or mechanism for registering Crossref DOIs. As part of the PAD team taking over the publication, the DOIs need to be transferred to CDL's Crossref account and added to EZID. This process involves a few parts: (1) requesting that Crossref transfer the publication's prefix and DOIs, (2) setting up the transferred prefixes in EZID, and (3) re-registering the existing DOIs in EZID. 

**Requesting a DOI transfer from Crossref**

The PAD team will instruct the publication to send an email to Crossref to request a transfer. The EZID Service Manager will be copied on the request. The request typically looks like this:

> *[PUBLICATION NAME] has been registering DOIs on the prefix [DOI PREFIX] via [NAME OF ORIGINAL PLATFORM AND/OR SPONSORING MEMBER]. [PUBLICATION NAME] is moving to the California Digital Library (CDL), and we therefore wish to transfer our prefix to the CDL’s Crossref member account effective [DATE OF DESIRED TRANSFER]. We authorize CDL to register and manage DOIs on our behalf using this prefix. As a result of this transfer, the California Digital Library should be listed as the publisher in metadata registered in Crossref.*

Crossref will follow up and request additional information as needed. 

> **Example of previous cases for reference:**
> 
> - *Journal of Evolution and Health*
> - *EarthArXiv*

**Setting up the transferred prefixes in EZID**

Once Crossref has approved the request, the prefixes need to be added to EZID so that they can be used for managing existing DOIs and registering new ones. In order to support both managing existing DOIs and registering new ones, the transferred prefix needs to be set up as two shoulders: a super-shoulder and a regular one. 

For example, given a scenario in which the "Journal of Transferred Prefixes" is moving to EZID and its prefix is 10.12345, the following two shoulders will be created:

- `10.12345/` (this is the super-shoulder)
- `10.12345/J5` (this is the regular shoulder)

Shoulder labels must be unique in EZID, so the super-shoulder label should be something like `Journal of Transferred Prefixes (no minter)` and the regular shoulder would be `Journal of Transferred Prefixes`

Follow the documentation in the [Creating and managing shoulders guide](https://github.com/CDLUC3/ezid-service/blob/master/creating-and-managing-shoulders.md) to see the specific management commands for creating the above.

Once the shoulders have been created, set them up in EZID Admin following the same process described above in [Setting up a new journal with DOIs for the first time](#setting-up-a-new-journal-with-DOIs-for-the-first-time)

**Re-registering the existing DOIs in EZID**

Once the shoulders are created the account configured, the PAD team can proceed with re-registering the existing DOIs in EZID, using the super-shoulder. 

This process is handled by the PAD team so there is nothing the Service Manager needs to do. However, some questions may arise if the PAD team experiences any issues or errors. 

### Setting up a journal with an independent Crossref account
This is not a common scenario. The most prominent example is SFEWS. In this scenario, the journal's DOI registrations are sponsored/covered by CDL, but the journal maintains its own process for registering DOIs outside of EZID. 

In other words, this publication's DOIs will be accounted for in CDL's Crossref invoices, but there will be no record of their activity within EZID. 
