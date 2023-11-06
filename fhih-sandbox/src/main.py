"""
A flask app that allows users to manage their medications
Users should be able to:
 - register and login
 - view their medication details
 - provide contact details, so that reminders can be sent via SMS (email might be easier)
 - admin users (or prescribers) can login and view, update, or delete prescriptions
The app should include all the usual securtity measures
 - password hashing and salting for user credentials
 - email authentication for user accounts
 - strong password enforcement
 - restricted subdomains requiring authorisation
 - ensure all inputs are sanitissed against SQL injections
Any and all medically relevant data should be stored in a FHIR server
 - Patient, medications and prescriptions details should be recorded as a patient resource
 - We will use fhirclient python lib to interact with fhir api's 

Architecture notes:
 - FHIR is designed for storing healthcare data, not passwords. We should store user credentials
   in a seperate database. Let's set up a local MySQL database for storing User data and credentials
"""

############################################
#            ROUGH OUTLINE                 #
############################################


# Import necessary libraries and modules

# Define Flask app and configuration settings

# Create database connection to MySQL
# Initialize necessary tables if they don't exist

# Define User class with appropriate attributes and methods
# Implement password hashing and salting methods

# Define Medication class with appropriate attributes and methods

# Define Prescription class with appropriate attributes and methods
# Implement authentication decorator for admin users

# Define routes and their corresponding functions
# Implement route to register users
# Implement route to login users
# Implement route to view medication details
# Implement route to provide contact details for reminders
# Implement route accessible only to admin users to view, update, or delete prescriptions

# Implement necessary security measures:
  # Password hashing and salting for user credentials
  # Email authentication for user accounts
  # Strong password enforcement
  # Restricted subdomains requiring authorization
  # Input sanitization against SQL injections

# Connect to FHIR server using fhirclient library

# Define FHIR resources:
  # Define Patient resource with appropriate attributes and methods
  # Define Medication resource with appropriate attributes and methods
  # Define Prescription resource with appropriate attributes and methods

# Implement methods to interact with FHIR server:
  # Method to create a new patient resource
  # Method to retrieve patient's medication details from FHIR server
  # Method to update patient's contact details in FHIR server
  # Method to retrieve prescriptions from FHIR server for admin users

# Run the Flask app
