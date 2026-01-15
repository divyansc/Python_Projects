# Employee Management API
## About the Project
This is a simple backend project built using Django and Django REST Framework.
The project provides APIs to manage employees in a company.
The main goal of this project is to perform basic CRUD operations and secure the APIs using authentication.

## What This Project Does

+ Allows creating a new employee

+ Allows viewing all employees

+ Allows viewing a single employee by ID

+ Allows updating employee details

+ Allows deleting an employee

+ Prevents creating employees with duplicate email IDs

+ Only authenticated users can access the APIs

### Technologies Used:

- Python

- Django

- Django REST Framework

- JWT Authentication (SimpleJWT)

- SQLite database

### Employee Fields

Each employee has the following fields:

- id (auto generated)

- name

- email (unique)

- department

- role

- date_joined (auto generated)

How to Run the Project
1. Activate virtual environment
source venv/Scripts/activate   # For Windows (Git Bash)

2. Install required packages
pip install django djangorestframework djangorestframework-simplejwt

3. Apply migrations
python manage.py makemigrations
python manage.py migrate

4. Create superuser
python manage.py createsuperuser

5. Start the server
python manage.py runserver

### Authentication

JWT authentication is used.

Get access token

POST /api/token/

{
  "username": "admin",
  "password": "password"
}


Use the token in headers:

Authorization: Bearer <access_token>

### API Endpoints
Create Employee

POST /api/employees/

Get All Employees

GET /api/employees/

### Supports filtering and pagination:

/api/employees/?department=HR
/api/employees/?role=Developer
/api/employees/?page=2

Get Single Employee

GET /api/employees/{id}/

Update Employee

PUT /api/employees/{id}/

Delete Employee

DELETE /api/employees/{id}/

### Error Handling

Returns 400 if validation fails (like duplicate email)

Returns 401 if user is not authenticated

Returns 404 if employee ID does not exist

Returns 201 on successful creation

Returns 204 on successful deletion

### Testing

Basic tests are written to check all main APIs.

To run tests:

python manage.py test


Tests include:

Creating an employee

Checking duplicate email case

Listing employees

Getting employee by ID

Updating employee

Deleting employee

### Summary
This project demonstrates basic backend development using Django REST Framework, including authentication, validation, and API testing.

