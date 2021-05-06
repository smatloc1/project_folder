
# Mighty Missions Network

Mighty Missions Network is an application for non-profits, social enterprises, and other mission-based organizations.  It was created to faciliatate community and collaboration between organizations that share a similar mission or cause.  It is believed that these connections will bring a greater reward and enable each organization to increase their ability to meet the needs of their respective communities. 
            


## Authors

- [@sherrymatlock](https://github.com/smatloc1)

  
## Usage

This project is to be used by the following:

- Nonprofits
- Social Enterprises

User organizations will go the the homepage and sign in with their organization's name (login).
After login, they will be directed to their profile page, which shows the details for the organizations.
Once logged in they will see the search bar and are now able to search for other organizations by cause or name.
A new user or organizaton can click on register (in the navbar) from the homepage.  From there they will,
be logged in as a new user and taken to their profile page. 


## Features

- Homepage
- Register a New Org into the Database
- Generate a Profile Page
- Search Function
    - By Name
    - By Cause

  
## Screenshots

[App Screenshot]('/static/img/homepage-prt-sc.png')
[App Screenshot]('/static/img/register-prt-sc.png')
[App Screenshot]('/static/img/profile-prt-sc.png')
[App Screenshot]('/static/img/searchbycause-prt-sc.png')


## Installation
Requires PostgreSQL
createdb mmdata
git clone the project_folder repo
inside this directory, create a virtual environment
activate virtual environment
pip install requirements
python model.py to create Cause and Org classes
python crud.py to create functions needed for server.py
python seed.py to create tables and seed the database
python server.py to run the server
python tests.py to run unit and integration tests of the functions
open your browser to localhost:5000

## Tech Stack

Flask, Python, SQLAlchemy, unittest, Postgresql, Session, Jinja, HTML, CSS, and Bootstrap

  
## Acknowledgements

 - [Hackbright Engineering Academy](https://hackbrightacademy.com/)
  