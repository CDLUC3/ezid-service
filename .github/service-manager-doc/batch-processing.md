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

In the above scenario, the command will mint DOIs on the shoulder doi:10.5072/FK2 based on metadata provided in the file "batchtest.csv" whose metadata fields correspond to the information in the file called "mappings," and the command will run based on the information in the script "batch-register.py". The identifiers will be associated in the user account associated with whichever credentials are used instead of "username" and "password".

Other notes about the above scenario: 
- `-c` is for the credentials being supplied
- p = preview, shows a preview of the metadata (remove for final operation)
s = shoulder 
mint = operation (can also be create or update)

## Example scenario 1: batch processing ARKs




Check the preview of the results to make sure they look good
If everything looks good and no errors, run the registration command again without the p parameter:  python batch-register.py -c apitest:apitest  -s doi:10.5072/FK2 mint mappings manifold_resources_batchtest.csv

Tips & tricks:
Arrow up to run the last command again
In vi mappings:
hit i to insert new information
Esc then :wq to quit and return to main terminal window



Notes & references:

Mappings file (required lines highlighted in yellow)
_profile = datacite
/resource/titles/title = $1
_target = $2
/resource/publicationYear = 2020
/resource/resourceType@resourceTypeGeneral = Dataset
/resource/publisher = EZID
/resource/creators/creator/creatorName = EZID Group


If metadata will be the same for each object (e.g., publication date for all DOIs is 2020) you can specify this in the mappings file, as shown above. If metadata varies from object to object, specify the spreadsheet column where this information will be read (e.g., $1 specifies that the titles for each DOI are in Column 1 of the csv file). 


To update existing DOIs:
Spreadsheet needs to have a column for id

To do this with Crossref DOIs:
Spreadsheet needs to include Crossref XML (entire blob inside a single cell)
