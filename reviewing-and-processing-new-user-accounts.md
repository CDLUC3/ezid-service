# Reviewing and processing new user accounts in EZID
This is a companion guide to https://github.com/CDLUC3/ezid-service/blob/master/creating-and-managing-shoulders.md.

This guide describes how new accounts requests are initiated and what the EZID Service Manager needs to do to review and process a new account. 

**Contents**
- [Initial triage](#initial-triage-of-new-account-requests)
- [General guidance](#general-guidance-about-setting-up-new-accounts)
- [DataCite accounts](#user-will-be-registering-DataCite-DOIs)
- [ARK accounts](#user-will-be-registering-ARK-identifiers)
- [Special cases](#special-cases)

## Initial triage of new account requests
EZID regularly receives requests from prospective users. Only prospective users from UC can be considered for new accounts at this time. If the prospective user is not from UC, the Service Manager should indicate that EZID is not currently taking on new users and provide information about other options as appropriate (e.g., ARK Alliance, Crossref, DataCite, Zenodo, etc.).

If the prospective user is from UC and has not yet been in touch with the campus EZID contact, loop in the campus contact for them to initiate a conversation about whether EZID is the right solution for their needs. In some cases, EZID may be the best option, and in some cases a different solution would be better. 

In some cases, a prospective user from UC may request a new account without realizing that one already exists for their group/department. It is therefore important to check existing account usage in EZID first before moving forward. 

For more information about handling new account requests, see the [EZID Service Manager guide](https://docs.google.com/document/d/1HYjKFJ2cKTgs5R5V5oRcL5oQ0SN_IVeHIZI6KPpEVco/edit?usp=sharing).

If the Service Manager and campus contact determine that a new account should be created, follow the steps below depending on the type of identifer the account will be working with. 

## General guidance about setting up new accounts

- **Tracking requests:** Create a new Github issue in the [ezid-service repository](https://github.com/CDLUC3/ezid-service/issues) with the basic details of the request (provided via the request form). This will provide a record of the request for tracking and historical purposes. Remember that Github issues are public, so do not include sensitive information like a user's email or password in the body of the issue.
  
- **Best practices for account ownership:** Ideally, the person or group requesting the account will be able to provide more than one point of contact to ensure continuity in the event that someone moves on or is otherwise unavailable. Likewise, it is ideal for the main email address on the account to be a shared inbox that multiple people have access to, as opposed to an individual account. If the account requestor only provides one point of contact and a single individual's email address, follow up to request a secondary contact as well as a different email address.
  
- **Setting a username:** Users may provide a suggested username when they submit the account request form. It is at the Service Manger's discretion to choose a username that best fits the circumstances of the account. Usernames are public in the sense that they can be seen on identifier landing pages and other public pages in EZID, so they should not contain any sensitive information. Ideally the username will indicate something about the group or project associated with the account, for example `ucla-robotics-lab`. 

- **Setting a shoulder label:** Users may provide a suggested shoulder label when they submit the account request form. It is at the Service Manger's discretion to choose a shoulder label that best fits the circumstances of the account. Shoulder labels are not public and are not included in any identifier metadata, but they are useful internally in the EZID system to identify the group or project a shoulder is associated with. In many cases, the shoulder label will be the same as the username, e.g., `ucla-robotics-lab`.
  
- **Setting a password:** When the Service Manager sets up a new account, they need to set an initial password so that the user can log in for the first time. This should be treated as a temporary password that the user should change once they have logged in successfully. An example of a temporary password is `ezid123`.
  
- **Linking user accounts to shoulders:** A user account needs to be created before it can be linked to a shoulder. Create the user account, click `Save`, and then reopen the user account details to link it to a shoulder.  


## User will be registering DataCite DOIs
1. Ask the user or campus contact (depending on the situation) to fill out the [EZID request form](https://tinyurl.com/ezid-request)
   
2. Create a new Github issue in the [ezid-service repository](https://github.com/CDLUC3/ezid-service/issues) with the basic details of the request (provided via the request form), so that the task can be tracked and recorded
   
3. Write to support@datacite.org to request a new DOI prefix. Provide the details of the repository (currently, this correponds to an EZID datacenter) where the DOIs will be registered.

The repository codes correspond to the ten campuses plus CDL and are listed in the [Creating and managing shoulders guide](https://github.com/CDLUC3/ezid-service/blob/master/creating-and-managing-shoulders.md).

**Example prefix request:**

> 📩
> *Hi DataCite,*
>
> *Could I please obtain a new prefix for CDL.UCB?*
> 
> *Thanks!*
> *Maria*

DataCite will typically turn around a prefix request within 1-2 business days. Note that requesting prefixes from DataCite is a temporary workaround until EZID determines whether or not to reconfigure its repository structure. For more information, see [this Github issue](https://github.com/CDLUC3/ezid-service/issues/256). 

4. Set up a new DOI shoulder as described in [Creating and managing shoulders](https://github.com/CDLUC3/ezid-service/blob/master/creating-and-managing-shoulders.md)
   
5. In the EZID Admin portal, associate the new shoulder with an existing or new EZID group (in most cases, the group will be the one associated with the relevant UC campus)
   
6. Create a new user account in the EZID Admin portal with the details provided in the request form. Set a temporary password that the user will change later, e.g., `ezid123`.
   
7. Link the new user account to the new shoulder
    
8. Write to the user and campus contact confirming that the account has been created. There is a canned response in Freshdesk that can be used and adapted as needed.
   
9. Add the account contact email to the [EZID listserv](https://listserv.ucop.edu) (`EZID-L@LISTSERV.UCOP.EDU`) so that they will receive important EZID service announcements
    
10. Close out the Github issue 

## User will be registering ARK identifiers
1. Find out whether the user has already obtained a [NAAN](https://arks.org/about/getting-started-implementing-arks/) (this is not common).
   
2. If not, [submit a NAAN request](https://docs.google.com/forms/d/e/1FAIpQLSfd1CX6idwLB47g8OGKUG654auV8IU8yI7DAs61cXGOoFDn0g/viewform?c=0&w=1) on the user's behalf, indicating EZID and your name as the service provider.
   
3. Ask the user or campus contact (depending on the situation) to fill out the [EZID request form](https://tinyurl.com/ezid-request)
   
4. Create a new Github issue in the [ezid-service repository](https://github.com/CDLUC3/ezid-service/issues) with the basic details of the request (provided via the request form), so that the task can be tracked and recorded
   
5. Set up a new ARK shoulder as described in [Creating and managing shoulders](https://github.com/CDLUC3/ezid-service/blob/master/creating-and-managing-shoulders.md)
   
6. In the EZID Admin portal, associate the new shoulder with an existing or new EZID group (in most cases, the group will be the one associated with the relevant UC campus)
   
7. Create a new user account in the EZID Admin portal with the details provided in the request form. Set a temporary password that the user will change later, e.g., `ezid123`.
   
8. Link the new user account to the new shoulder
   
9. Write to the user and campus contact confirming that the account has been created. There is a canned response in Freshdesk that can be used and adapted as needed.
    
10. Add the account contact email to the [EZID listserv](https://listserv.ucop.edu) (`EZID-L@LISTSERV.UCOP.EDU`) so that they will receive important EZID service announcements
    
11. Close out the Github issue 

## Special cases

### User will be registering Crossref identifiers
See the [separate guide about Crossref] 

### User needs a new shoulder on an existing prefix or NAAN
In some cases, an existing user may get in touch asking for a new shoulder on an existing prefix or NAAN. This does not need to go through the same approval process as for a brand-new account, but it is at the Service Manager's discretion to determine how best to move forward. 

From a technical standpoint, the process of setting up a shoulder on an existing prefix or NAAN is the same as setting up a shoulder for the first time. Refer to the [Creating and managing shoulders](https://github.com/CDLUC3/ezid-service/blob/master/creating-and-managing-shoulders.md) guide for the step-by-step process. 

In EZID Admin, the new shoulder will need to be added to a group as with other shoulders, and linked to the user account(s) that the requestor has identified or to a new user account depending on the situation. 
