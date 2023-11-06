from fhir.resources.patient import Patient

import os
print(os.getcwd())

file_path = os.path.join('data','patient_details.fhir.json')
my_patient = Patient.parse_file(file_path)
print(f'my_patient: {" ".join(my_patient.name[0].given)} {(my_patient.name[0].family)}')
print(f'my_patient: {(my_patient.address[0])}')
print(f'my_patient: {" ".join(my_patient.address[0].line)}, {(my_patient.address[0].city)}, {(my_patient.address[0].state)}, {(my_patient.address[0].country)}')