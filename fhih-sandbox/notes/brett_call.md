AV has a number of prods in the health space

cubico 
halo 
few others

primary health ecosystem

halo is one of the products

interpoerabikity layer 

theres no cloud based patient management environ
for record keeping for GP's 

data captured via one of 3/4 PMS 
51% [sic] of practices use best practive premier as their PMS


generally logs direclty to an on premise server, to sql server .NET app

time has passed 

what halo does:
best practice was various integrators 

go see doctor, 
that info needs to get into best pracice (a software??) so dr can see you with all the data
historically involce it teams placing .net agent on each server (5000 across aus)
creates a headache to manage all agents in an isolated env.
same for apps making dr's bookings (hot doc)

an api layer sitting on azure using azure api gatewat to abstract the complexity away from integrators
no need to worry about the remote env. 
just a sql passthrough

by 2025 all will use halo

currently standard is fhir

we want to help halo become fhir compliant, as well as sql passwthrough, write and read for appointments,

main thing is fhir compliacnce

bupa want to be an integrator into best practice. 

throwing cash at it to get it compliant in 6 months

main thing lacking is the ability to read schema with no standard enforced on the local database

skill sets 
 - data enfineering 
 - data modelling
 - map incoming data (might be fhir compliant) into an executable SQL statement 
 - revers of above 

 learn: 
  - fhir standards
  - tech stack azure (best practices is azure), .NET, caching, redis,   