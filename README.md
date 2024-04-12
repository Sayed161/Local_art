# Artwork API

This is a Django REST Framework project for Local Artwork Showcase.

## Setup
- Clone the repository:https://github.com/Sayed161/Local_art.git
- Install dependencies: Django,Django Restframework, Python
    - (pip install -r requirements.txt)
- Run this two command - 
   - python manage.py makemigrations
   - python manage.py migrate
- Create a superuser to access the Django admin interface:
python manage.py createsuperuser
- Run the Server 
  - python manage.py runserver

## API Endpoints
## User Registraions
- URL : Register/
- Method: POST
- Description: Create a new User.
- Required Fields : Username,First Name, Last Name,Email,password,confirm password

## User Login
- URL : /login/
- Method: POST
## Authentication - The API supports user authentication with token-based authentication.
- Description: Login a User.Also get Random Token and UID.
- Required Fields : Username,password

## User Logout
- URL : logout/
- Method: POST
- Description: Log out the authenticated user and delete the token.
- Required Fields : None.

## Artworks
## Only Authenticated User

- URL: "Artwork/"
- Method: POST,GET,UPDATE,DELETE(CRUD)
-(GET) Description: Get a list of all artworks.
-(POST)Description: Create a new artwork.
-(UPDATE) Description : Upadate any Arkworks.
-(Delete) Description : Delete any Artworks
-(POST) Required Fields: title, artist, description, imageURL.

## Artist
## Only Authenticated User

- URL: "Artisits/"
- Method: POST,GET,UPDATE,DELETE(CRUD)

## Language
Python,Django,Django RESTFramework

## Database
PostgreSQL


