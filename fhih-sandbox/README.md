# Documenting the videos at Sidharth Ramesh's youtube channel


## Creating a patient FHIR resource
grab fihr schema from documentation -> downloads -> json

located in fhir.schema.json

point vs code to this schema in workplace settings json

create patient details text file

map these types to fhir resource types by referring to 
https://www.hl7.org/fhir/patient.html

when entering data into a fhir type object use ctrl+space and most should be prefilled from the schema

## Interacting with the publicly available FIHR API's

We'll use the hapi fhir one as in the youtube series

https://hapi.fhir.org/baseR4/swagger-ui/?page=Patient

Base url:

https://hapi.fhir.org/baseR4

He uses Insomnia to interact with the API's, let's just use python `requests`, see `main.py`

