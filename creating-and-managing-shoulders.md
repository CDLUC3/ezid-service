# Creating and Managing EZID Shoulders
*Note: UCOP VPN access required*

## Accessing the servers

1. Identify which EZID server you will need to be working in:
- Stage: uc3-ezidui01x2-stg.cdlib.org
- Dev: uc3-ezidui01x2-dev.cdlib.org
- Prod: uc3-ezidui01x2-prd.cdlib.org


2. In a Terminal window, log in to the EZID server using ssh and the server name:
   
`ssh uc3-ezidui01x2-stg.cdlib.org`

*Note*: Depending on your setup, you may need to add your computer username to the beginning of the command, e.g.: 

`ssh username@uc3-ezidui01x2-stg.cdlib.org`

3. When prompted, enter your password

*Note: Server passwords are created and managed by the IAS team*

5. Become the EZID role account user:
`sudo su - ezid`

7. Navigate to the EZID directory:
`cd ezid`

9. Now you are ready to run a shoulder management command. Follow the instructions below depending on which operation you need to run.

## General notes about creating shoulders
The basic command for creating a new shoulder is structured as follows:

`./manage.py shoulder-create-idtype idtype:/12345/b6 "ARK Shoulder Name"`

In the above example, `idtype` would be replaced with `doi` or `ark` depending on which type of shoulder is being created. For DOIs, the `/` character after `idtype` is not used.

There are additional elements required for creating DOI shoulders. See the sections below. 

Once a shoulder creation command has been executed, the changes are reflected immediately in EZID. 

### Create a new DataCite DOI shoulder

`./manage.py shoulder-create-doi doi:12345/b6 "DOI Shoulder Name" --datacite "CDL.CDL"`

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

`./manage.py shoulder-create-doi doi:12345/b6 "DOI Shoulder Name" --crossref`

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
