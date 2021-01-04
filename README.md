# Data Representation Project

### GMIT - Higher Diploma in Computing and Data Analytics.
### Author : Slawomir Sowa
### Email : G00376519@gmit.ie


This repository contains all the files for Data Representation Project. 

### The repository contains the following files:

* server.py - Flask server application 
* requirements.txt - text file with python packages required to run the app
* static_pages - folder contains html pages, CSS and img folder. 
* config.ini - configuration file contains MySQL database details 
* mysql_dbconfig.py - python file to read config.ini 
* windows_DAO.py - Data Access Object python file to interact with database 
* .gitignore - GitHub gitignore file
* initdb.sql - file contains SQL statements to create database  

### Instruction

1. Clone repository: https://github.com/Slawak1/Data-Representation-Project
2. Create and activate blank virtual environment with a directory named <code>venv</code>
3. Run code <code> pip install -r requirements.txt</code> to install required Python packages
4. Create a MySQL database from <code>initdb.sql</code>
5. Edit <code>config.ini</code> file by entering your database details 
6. Run Flas server (On Windows):
* <code>SET FLASK_APP=server</code>
* <code>SET FLASK_ENV=development</code>
* <code>flask run</code>
7. Open http://127.0.0.1:5000/ in web browser

### Short Description of the Project

The project involved writing a Flask server program that consumes a REST API and creating a web interface. Project contains three html files:
- index.html, 
- login.html 
- main.html 

and two MySQL tables: 
- users, 
- customers.

The functionalities that have been introduced are:
- logging in (verification with the user database)
- user registration (adding a user to the database)
- Displaying the customer table, where you can add, delete and edit customers.

Login form is implemented but needs some security improvements.


