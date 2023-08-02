import json
import pytest
import requests


# from feeda-api-tests.controllers.quickstart import process_messages


@pytest.fixture
def token():
    url = "http://localhost:8000/users/login/"

    payload = json.dumps({
        "email": "qafeeda123@gmail.com",
        "password": "BazaQA123"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic cWFmZWVkYTEyM0BnbWFpbC5jb206QmF6YVFBMTIz'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200

    token = json.loads(response.content)['token']

    yield token


@pytest.fixture
def project(token):
    url = "http://localhost:8000/user-project/create-project/"

    payload = json.dumps({
        "title": "feeda",
        "comment": "hr app",
        "type_project": 1,
        "complexity": 1,
        "project_status": 1,
        "start_date_project": "2003-07-16",
        "end_date_project": "2003-07-19",
        "address_site": "https://www.google.com/",
        "url": "Unknown Type: slug"
    })
    headers = {
        'Authorization': 'Token ' + token,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    yield response


@pytest.fixture
def create_participant(token):
    url = "http://localhost:8000/user-project/add-participant/"

    payload = json.dumps({
        "first_name": "Anastasia",
        "last_name": "Luzina",
        "speciality": 1,
        "phone_number": "+380999999999",
        "email": "testing@gmail.com",
        "comment": "string",
        "account_discord": "anastasiia",
        "account_linkedin": "https://www.linkedin.com/in/anastasiia",
        "city": "string",
        "experience": False,
        "project": 1,
        "stack": "QA Manual"
    })
    headers = {
        'Authorization': 'Token ' + token,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    yield response
