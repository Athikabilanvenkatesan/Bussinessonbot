# Bussinessonbot

This project is a REST API built using Flask-RESTful and Flask-SQLAlchemy. It provides endpoints for searching bank branches in India.

# Requirements
* Python 3.x
* Flask
* Flask-RESTful
* Flask-SQLAlchemy


# Installation
Clone this repository or download the ZIP file.
Install the required packages using pip install -r requirements.txt.
Set the SQLALCHEMY_DATABASE_URI variable in the app.py file to point to your database file.
Run the app using python app.py.


# API Endpoints

# GET /api/search
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



# GET /api/branch
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


# Output

Case 1

 Search API to return possible matches across all columns and all rows, ordered by IFSC code (ascending order) with limit and offset.


![image](https://user-images.githubusercontent.com/113780724/221828578-2e3b6013-f77d-4da3-baa8-d45a01b25665.png)

Case 2

 Branch API to return possible matches based on the branch name ordered by IFSC code (descending order) with limit and offset


![image](https://user-images.githubusercontent.com/113780724/221829696-010852e4-2a01-4612-b4bc-0edd7f1ee34e.png)









