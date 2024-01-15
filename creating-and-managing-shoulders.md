# Creating and Managing EZID Shoulders
This document explains the procedure for creating and managing shoulders in EZID. Creating and managing shoulders in EZID is an essential operation that enables users to register identifiers. 

A shoulder is a unique concept that only exists in the context of EZID and for some ARK users. It is an an extended DOI prefix or ARK NAAN that functions as an attachment point for an identifier string. Its original intended purpose was to multiply the potential namespaces available on a given prefix or NAAN. This was more relevant in the earlier days of EZID when it was more common for users to share the same prefixes or NAANs. As current practices in EZID have evolved away from prefix/NAAN sharing, the original purpose of shoulders is less relevant. However, EZID continues to use them for historical, practical, and technical purposes. 

A shoulder typically consists of a letter and number following a slash after a prefix or NAAN. For example, in doi:10.5070/B5, 10.5070 is the prefix and B5 is the shoulder. There is extensive documentation about shoulders on the [EZID](https://ezid.cdlib.org/learn/id_basics) and [ARK Alliance](https://arks.org/about/ark-features/) websites. For the purposes of setting up new accounts and new shoulders, the general rule of thumb is to pick a random letter and number, avoiding vowels, the letter l, and the digits 1 and 0 when possible (to minimize transcription errors). 

Currently, creating and managing shoulders requires using Python management commands. In the future, the workflow could be improved by enabling shoulder creation and management functions in the EZID Admin UI. 

Prior to creating and managing a shoulder, communication with a current or prospective user is required to determine their needs and the best course of action. If the request entails a new prefix or NAAN, additional coordination with prefix and NAAN authorities (DataCite, Crossref, and the NAAN Registry, respectively) is required. See the [related guide](https://github.com/CDLUC3/ezid-service/blob/master/reviewing-and-processing-new-user-accounts.md) about this aspect of the process. 

Once a shoulder has been created, it needs to be linked to the user's account in EZID. See the [related documentation](https://github.com/CDLUC3/ezid-service/blob/master/reviewing-and-processing-new-user-accounts.md) for the list of steps. 

## Prerequisites
- Determine if the user needs a DataCite shoulder, Crossref shoulder, or ARK shoulder
- Determine if the user will be using a shoulder on an existing prefix/NAAN or if they require a new prefix or NAAN
- If a new prefix is required, contact DataCite or Crossref ([see related documentation](https://github.com/CDLUC3/ezid-service/blob/master/reviewing-and-processing-new-user-accounts.md))
- If a new NAAN is required, submit the NAAN request form ([see related documentation](https://github.com/CDLUC3/ezid-service/blob/master/reviewing-and-processing-new-user-accounts.md))
- Determine what the shoulder extension will be (e.g., `B5`)
- UCOP VPN access is required and must be enabled in order to run the below operations

## Accessing the servers

1. Identify which EZID server you will need to be working in:
- Stage: uc3-ezidui01x2-stg.cdlib.org
- Dev: uc3-ezidui01x2-dev.cdlib.org
- Prod: uc3-ezidui01x2-prd.cdlib.org


2. In a Terminal window, log in to the EZID server using ssh and the server name:
   
`ssh uc3-ezidui01x2-stg.cdlib.org`

*Note*: Depending on your setup, you may need to add your computer username to the beginning of the command, e.g.: 

`ssh username@uc3-ezidui01x2-stg.cdlib.org`

3. If prompted, enter your password. Server passwords are created and managed by the IAS team. As of November 23, IAS is preferring that servers be accessed via ssh key instead of passwords. Contact IAS if you need a ssh key and/or need help using it to access EZID. 

5. Become the EZID role account user:
`sudo su - ezid`

7. Navigate to the EZID directory:
`cd ezid`

9. Now you are ready to run a shoulder management command. Follow the instructions below depending on which operation you need to run.

## General notes about creating shoulders
The basic command for creating a new shoulder is structured as follows:

`./manage.py shoulder-create-idtype idtype:/12345/b6 "ARK Shoulder Name"`

In the above example, `idtype` would be replaced with `doi` or `ark` depending on which type of shoulder is being created. For DOIs, the `/` character after `idtype` is not used.

ARK shoulders use lowercase, and DOI shoulders use uppercase (e.g., `b6` and `B6`).

There are additional elements required for creating DOI shoulders. See the sections below. 

Once a shoulder creation command has been executed, the changes are reflected immediately in EZID. 

### Create a new DataCite DOI shoulder

`./manage.py shoulder-create-doi doi:12345/B6 "DOI Shoulder Name" --datacite "CDL.CDL"`

In the above example, "CDL.CDL" denotes the datacenter (EZID parlance, known as a "repository" in DataCite's system) associated with the shoulder. A datacenter/repository key is required for every DataCite shoulder in EZID.

Currently, the list of EZID datacenters corresponds to the 10 UC campuses plus CDL. The datacenter included in the shoulder command indicates which campus the intended user of the shoulder is based at. 

The list of current datacenters is as follows:

- CDL.CDL
- CDL.UCB
- CDL.UCD
- CDL.UCI
- CDL.UCLA
- CDL.UCM
- CDL.UCR
- CDL.UCSB
- CDL.UCSC
- CDL.UCSD
- CDL.UCSF

### Create a new Crosref DOI shoulder

`./manage.py shoulder-create-doi doi:12345/B6 "DOI Shoulder Name" --crossref`

### Create a new ARK shoulder

`./manage.py shoulder-create-ark ark:/12345/b6 "ARK Shoulder Name"`

## Miscellaneous shoulder management commands

### Update an existing shoulder
This command is used to change the name of an existing shoulder. Use the `shoulder-update-organization` command, enter the shoulder to be updated, and then enter the new name. 

`./manage.py shoulder-update-organization ark:/99999/fk4 “New ARK Shoulder Name”`

In the above example, the command will change the name associated with shoulder `ark:/99999/fk4` to New ARK Shoulder Name.

To update an existing DOI shoulder, the command would be:

`./manage.py shoulder-update-organization doi:12345/fk5 "New DOI Shoulder Name"`

### Create a super-shoulder
*Add explanatory notes about super-shoulders*

Super-shoulders are created just like regular shoulders following the instructions above, with the addition of a super-shoulder designation. 

`./manage.py shoulder-create-idtype idtype:/12345/ "Super-Shoulder Name" --super-shoulder`

### Change a DataCite shoulder's datacenter
This command is used to change the datacenter associated with a DataCite DOI shoulder. Enter the `shoulder-update-datacenter` command, enter the shoulder to be updated, and then enter the new datacenter (see list above) to be associated with the shoulder. For example, if a current shoulder is associated with CDL.CDL but we want to change it to UC Berkeley, we would use the following command: 

`./manage.py shoulder-update-datacenter doi:10.12345/FK5 “CDL.UCB”`


### View a list of all shoulders

`./manage.py shoulder-list`
