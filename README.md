# excel-data-collection
This flask application allows an admin to collect data from excel workbooks onto a database. The admin needs to define the table, its column, and data types (Text, Number, Date). These data types will be validated before attempting to write to the database table.

## Setup
### Get Postgresql database up
Get a postgresql database going. Install docker on your OS. This is tested on MacOS and Linux. Then use the postgres image here https://store.docker.com/images/022689bf-dfd8-408f-9e1c-19acac32e57b?tab=description by running 

    docker pull postgres 
    
on your terminal. 
Create a postgresql database container as: 

    docker run --name mydatabase -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
    
That command creates an postgres container called mydatabase from the postgres image exposing port 5432 of your host OS to the newly created container. If everything works out, install pgAdmin or your favorite Postgresql GUI browser and log in with user = postgres, password = postgres, port 5432, host = localhost.

### Do database migration
Use the requirements.txt to create a new virtual environment or a conda environment with environment.yml.Tested with python 3.5. Now cd into the root of the folder where run.py resides and run these commands:

    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade

This migration is powered by flask-migrate https://flask-migrate.readthedocs.io/en/latest/. After this first migration, your database should have the tables built to reflect the models defined in the models.py file under the app directory.

### Run application
    python run.py

Navigate to localhost:5000/admin/departments and create a group eg. Marketing Department. Then add a data source which basically builds a table on your database ready for data to fill it. Give it a descriptive name and then the table's name - lower cases and no spaces. Once a table is added, add some columns and their column types. Create an excel file with with the columns you defined and add some rows of data. Navigate to localhost:5000/upload and select the table's descriptive name from the dropdown list, browse to select the excel file you created and then Submit. The excel data is loaded onto the database table and the user gets a preview of the data - first 10 rows.

#### Validations
1. Columns from the excel file are compared with columns on the database table for matches.
2. Data types are validated against column definitions on the database table. Eg. if a text is found in a number column, the application stops and then complains. The user has to fix the data and try uploading the data again.

