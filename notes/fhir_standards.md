# Framework 
FHIR is based on "Resources" which are the common building blocks for all exchanges.

Example of a 'Patient' FIHR object here in JSON

```json
{
  "resourceType": "Patient",
  "id" : "23434",
  "meta" : {
    "versionId" : "12",
    "lastUpdated" : "2014-08-18T15:43:30Z"
  }
  "text": {
    "status": "generated",
    "div": "<!-- Snipped for Brevity -->"
  },
  "extension": [
    {
      "url": "http://example.org/consent#trials",
      "valueCode": "renal"
    }
  ],
  "identifier": [
    {
      "use": "usual",
      "label": "MRN",
      "system": "http://www.goodhealth.org/identifiers/mrn",
      "value": "123456"
    }
  ],
  "name": [
    {
      "family": "Levin",
      "given": [
        "Henry"
      ],
      "suffix": [
        "The 7th"
      ]
    }
  ],
  "gender": {
    "text": "Male"
  },
  "birthDate": "1932-09-24",
  "active": true
}
```


## 2.1.16.4 Interactions 
For manipulation of resources, FHIR provides a REST API with a rich but simple set of interactions:

Create = POST https://example.com/base/{resourceType}
Read = GET https://example.com/base/{resourceType}/{id}
Update = PUT https://example.com/base/{resourceType}/{id}
Patch = PATCH https://example.com/base/{resourceType}/{id}
Delete = DELETE https://example.com/base/{resourceType}/{id}
Search = GET https://example.com/base/{resourceType}?search parameters...
History = GET https://example.com/base/{resourceType}/{id}/_history
Transaction = POST https://example.com/base/ (POST a transaction bundle to the system)
Operation = GET https://example.com/base/{resourceType}/{id}/${opname}
The FHIR specification describes other kinds of exchanges beyond this simple RESTful API, including exchange of groups of resources as Documents, as Messages, and by using various types of Services.