import json
import pytest
import configparser
import os
import subprocess
import pytest

from api.users import Users
from api.user_project import UserProject


def run_tests():
    pytest.main(["-v", "--alluredir=allure-results", "tests"])


def generate_allure_report():
    subprocess.run(
        ["allure", "generate", "allure-results", "--clean", "-o", "allure-report"]
    )


def serve_allure_report():
    subprocess.run(["allure", "serve", "allure-results"])


@pytest.fixture(scope="session")
def config():
    config_file_path = os.path.join("../config", "config.ini")
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
def test_id(request):
    yield request.node.callspec.id


# @pytest.fixture
# def token():
#     url = "http://localhost:8000/users/login/"
#
#     payload = json.dumps({
#         "email": "admin123@gmail.com",
#         "password": "Feeda12345"
#     })
#     headers = {
#         'Content-Type': 'application/json'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#     assert response.status_code == 200
#
#     token = json.loads(response.content)["token"]
#
#     yield token


@pytest.fixture
def project(user_project):
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
    response = user_project.create_project(data=payload)
    yield response
    parsed_response = response.json()
    url = parsed_response.get("url")
    user_project.project_delete(project_url=url)


@pytest.fixture
def participant(user_project):
    payload = {
        "first_name": "Anastasia",
        "last_name": "Luzina",
        "speciality": 3,
        "phone_number": "+380999999999",
        "email": "testing@gmail.com",
        "comment": "string",
        "account_discord": "anastasiia",
        "account_linkedin": "https://www.linkedin.com/in/anastasiia",
        "city": "string",
        "experience": False,
        "project": [2, 3],
        "stack": "QA Manual, Postman",
        "type_participant": 1
    }

    response = user_project.add_participant(data=payload)

    yield response

    parsed_response = response.json()
    participant_id = parsed_response.get("id")

    user_project.delete_participant(participant_id=participant_id)
