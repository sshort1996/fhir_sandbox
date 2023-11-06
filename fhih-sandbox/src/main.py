import requests
import json

# Define the base URL of the FHIR server
base_url = 'https://hapi.fhir.org/baseR4'

# Function to send a GET request to retrieve a resource
def get_resource(resource_type, resource_id):
    url = f'{base_url}/{resource_type}/{resource_id}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
   
# Function to send a POST request to create a new resource
def create_resource(resource_type, resource_data):
    url = f'{base_url}/{resource_type}'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(resource_data))
    
    if response.status_code == 201:
        return response.json()
    else:
        print(f'Error: {response.status_code}')

# # Example usage
# patient_data = {
#     "resourceType": "Patient",
#     "name": [
#         {
#             "given": ["John"],
#             "family": "Doe"
#         }
#     ],
#     "gender": "male",
#     "birthDate": "1980-01-01"
# }

# Assuming the JSON object is stored in a file called 'data.json'
with open('patient_details.fhir.json') as json_file:
    data = json.load(json_file)

# Now the JSON data is loaded into the 'data' variable as a Python object


# Create a new patient resource
created_patient = create_resource("Patient", data)
print(f'created_patient: {created_patient}')

# Retrieve a patient resource
retrieved_patient = get_resource("Patient", created_patient["id"])
print(f'retrieved_patient: {retrieved_patient}')
