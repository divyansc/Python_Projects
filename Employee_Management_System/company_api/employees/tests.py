from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Employee


class EmployeeAPITest(TestCase):

    def setUp(self):
        """
        This runs before every test.
        We create a user and authenticate API requests.
        """
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="testuser",
            password="testpass"
        )

        self.client.force_authenticate(user=self.user)

        self.employee = Employee.objects.create(
            name="John Doe",
            email="john@company.com",
            department="Engineering",
            role="Developer"
        )

    
    # CREATE EMPLOYEE
    def test_create_employee(self):
        data = {
            "name": "Alice",
            "email": "alice@company.com",
            "department": "HR",
            "role": "Manager"
        }

        response = self.client.post(
            "/api/employees/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_employee_with_existing_email(self):
        """
        Edge case: email already exists
        """
        data = {
            "name": "Another John",
            "email": "john@company.com"
        }

        response = self.client.post(
            "/api/employees/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # LIST EMPLOYEES
    def test_list_employees(self):
        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    # GET SINGLE EMPLOYEE
    def test_get_employee(self):
        response = self.client.get(
            f"/api/employees/{self.employee.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_employee_not_found(self):
        response = self.client.get("/api/employees/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    
    # UPDATE EMPLOYEE
    def test_update_employee(self):
        data = {
            "name": "John Updated",
            "email": "john@company.com",
            "department": "Engineering",
            "role": "Team Lead"
        }

        response = self.client.put(
            f"/api/employees/{self.employee.id}/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

   
    # DELETE EMPLOYEE
    def test_delete_employee(self):
        response = self.client.delete(
            f"/api/employees/{self.employee.id}/"
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
