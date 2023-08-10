import json
import pytest
import requests
import configparser
import os

from api.users import Users
from api.user_project import UserProject


@pytest.fixture(scope="session")
def config():
    config_file_path = os.path.join("config", "config.ini")
    config_parser = configparser.ConfigParser(os.environ)
    config_parser.read(config_file_path)

    api_config = {
        "base_url": config_parser.get("api", "base_url"),
        "username": config_parser.get("api", "username"),
        "password": config_parser.get("api", "password"),
    }

    yield api_config


@pytest.fixture
def users(config):
    users_client = Users(config=config)

    yield users_client


@pytest.fixture
def user_project(config, users):
    login_response = users.login(
        email=config.get("username"), password=config.get("password")
    )
    user_project_client = UserProject(
        config=config, token=login_response.json()["token"]
    )

    yield user_project_client


@pytest.fixture
def token():
    url = "http://localhost:8000/users/login/"

    payload = json.dumps({"email": "qafeeda123@gmail.com", "password": "BazaQA123"})
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic cWFmZWVkYTEyM0BnbWFpbC5jb206QmF6YVFBMTIz",
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200

    token = json.loads(response.content)["token"]

    yield token


@pytest.fixture
def project(token):
    url = "http://localhost:8000/user-project/create-project/"

    payload = json.dumps(
        {
            "title": "feeda",
            "comment": "hr app",
            "type_project": 1,
            "complexity": 1,
            "project_status": 1,
            "start_date_project": "2003-07-16",
            "end_date_project": "2003-07-19",
            "address_site": "https://www.google.com/",
            "url": "Unknown Type: slug",
        }
    )
    headers = {"Authorization": "Token " + token, "Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)
    yield response


@pytest.fixture
def participant(token):
    url = "http://localhost:8000/user-project/add-participant/"

    payload = json.dumps(
        {
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
            "stack": "QA Manual",
        }
    )
    headers = {"Authorization": "Token " + token, "Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    yield response
