# CATTLE MANAGEMENT SYSTEM

## Project set up
### Set up Virtual Environment
  #### Install virtualenv package
   The virtualenv package is required to create virtual environments. You can install it with pip:
   
    pip install virtualenv
  #### Create the virtual environment
   To create a virtual environment, you must specify a path. For example to create one in the local directory called ‘mypython’, type the following:
   
     virtualenv mypython
  #### Activate the virtual environment
   You can activate the python environment by running the following command:
   
  Mac OS / Linux
  
      source mypython/bin/activate
  Windows
  
      mypthon\Scripts\activate
   
  You should see the name of your virtual environment in brackets on your terminal line e.g. (mypython).
  Any python commands you use will now work with your virtual environment  
  #### Deactivate the virtual environment
   To decativate the virtual environment and use your original Python environment, simply type ‘deactivate’.
      
     deactivate


### Packages
|Package | Version|
|---------|--------|
|Django | 3.2|
|djangorestframework | 3.12.4|
|djangorestframework-simplejwt|4.6.0|
|Pillow |8.2.0|
|pip | 21.0.1|
|psycopg2| 2.8.6|
|PyJWT | 2.1.0|
|sqlparse|0.4.1|

### Commands
 Go to cattle_manager using the following command :
    
    cd cattle_manager
 Run the server using the following command :
 
    python manage.py runserver

## Description
 A Django bases


## Features
- Authentication of Users using JWT
- Adding Animals of their Cattle
- Stores all the information about the animal such as delivery date,gender,its childrens etc.
- Notify the user about the Animal delivery date etc.
- Search the Animals based on tag number.
- Update the Animals
- Generating the Report

## Technologies
 - Python Programming
 - Django Rest Framework








