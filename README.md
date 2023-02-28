# Bussinessonbot

This project is a REST API built using Flask-RESTful and Flask-SQLAlchemy. It provides endpoints for searching bank branches in India.

#Requirements
Python 3.x
Flask
Flask-RESTful
Flask-SQLAlchemy


#Installation
Clone this repository or download the ZIP file.
Install the required packages using pip install -r requirements.txt.
Set the SQLALCHEMY_DATABASE_URI variable in the app.py file to point to your database file.
Run the app using python app.py.


#API Endpoints

#GET /api/search
This endpoint returns a list of bank branches that match the given search query. The query is case-insensitive and can match any of the following fields:

Bank Name
IFSC Code
Branch Name
Address
City
District
State
The response contains an array of bank branch objects. Each object has the following fields:

ifsc: IFSC code of the branch
bank_id: ID of the bank
branch: Name of the branch
address: Address of the branch
city: City of the branch
district: District of the branch
state: State of the branch
bank_name: Name of the bank


Query Parameters:

q (required): Search query
limit (optional, default: 10): Maximum number of branches to return
offset (optional, default: 0): Offset for pagination



#GET /api/branch
This endpoint returns a list of bank branches that match the given search query. The query is case-insensitive and can match any of the following fields:

Bank Name
IFSC Code
Branch Name
Address
City
District
State
The response contains an array of bank branch objects. Each object has the following fields:

ifsc: IFSC code of the branch
bank_id: ID of the bank
branch: Name of the branch
address: Address of the branch
city: City of the branch
district: District of the branch
bank_name: Name of the bank


Query Parameters:

q (required): Search query
limit (optional, default: 10): Maximum number of branches to return
offset (optional, default: 0): Offset for pagination






