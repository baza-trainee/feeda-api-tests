import json
import pytest
import requests
from controllers.quickstart import process_messages



@pytest.fixture
def login(email, password):
    url = "http://localhost:8000/users/login/"

    payload = json.dumps({
        "email": email,
        "password": password
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic a296bG92Mjc3N0BnbWFpbC5jb206QmF6YTEyMzQ1'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    yield response


@pytest.fixture
def token():
    url = "http://localhost:8000/users/login/"

    payload = json.dumps({
        "email": "kozlov2777@gmail.com",
        "password": "Baza12345"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic a296bG92Mjc3N0BnbWFpbC5jb206QmF6YTEyMzQ1'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 200

    token = json.loads(response.content)['token']

    yield token


@pytest.fixture
def request_for_reset_password(email):
    url = "http://localhost:8000/users/reset-password-email/"

    payload = json.dumps({
        "email": email
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    yield response


@pytest.fixture
def reset_password(password, confirm_password):
    url = "http://localhost:8000//users/password-reset-complete/"
    pairs = process_messages()  # Отримуємо список пар 'uidb64' і 'token'
    for uidb64, token in pairs:
        payload = json.dumps({
            "password": password,
            "confirm_password": confirm_password,
            "token": token,
            "uidb64": uidb64
        })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)

    yield response

@pytest.fixture
def create_project(title, comment, type_project, complexity, project_status, start_date_project, end_date_project,
                   address_site, urls, token):
    url = "http://localhost:8000/user-project/create-project/"

    payload = json.dumps({
        "title": title,
        "comment": comment,
        "type_project": type_project,
        "complexity": complexity,
        "project_status": project_status,
        "start_date_project": start_date_project,
        "end_date_project": end_date_project,
        "address_site": address_site,
        "url": urls
    })
    headers = {
        'Authorization': 'Token '+ token,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    yield response


@pytest.fixture
def add_participant_to_project(first_name, last_name, speciality, phone_number, email, account_discord,
                               account_linkedin, city, experience, project, stack, conditions_participation,
                               processing_personal_data, token):
    url = "http://127.0.0.1:8000/user-project/add-participant/"

    payload = json.dumps({
        "first_name": first_name,
        "last_name": last_name,
        "speciality": speciality,
        "phone_number": phone_number,
        "email": email,
        "account_discord": account_discord,
        "account_linkedin": account_linkedin,
        "city": city,
        "experience": experience,
        "project": project,
        "stack": stack,
        "conditions_participation": conditions_participation,
        "processing_personal_data": processing_personal_data
    })
    headers = {
        'Authorization': 'Token '+ token,
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=L0woWx8TnXBzBwfh1bNqYNpivPIgNs0u'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    yield response


@pytest.fixture
def view_project_information(token):
    url = "http://localhost:8000/user-project/filter-project/"

    payload = {}
    headers = {
        'Authorization': 'Token '+ token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    yield response


@pytest.fixture
def get_projects(token):
    url = "http://localhost:8000/user-project/filter-project/"

    payload = {}
    headers = {
        'Authorization': 'Token '+ token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    yield response


@pytest.fixture
# Подивитись до цього тесту!!!
def update_team(user_id, title, start_date_project, complexity, token):
    url = "http://127.0.0.1:8000/user-project/command-update/1/"

    payload = json.dumps({
        "user": [
            user_id
        ],
        "project": {
            "title": title,
            "start_date_project": start_date_project,
            "complexity": {
                "complexity": complexity
            }
        }
    })
    headers = {
        'Authorization': 'Token '+ token,
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=L0woWx8TnXBzBwfh1bNqYNpivPIgNs0u'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    yield response

@pytest.fixture
# Подивитись до цього тесту!!!
def update_team(first_name, last_name, email, project_type, complexity, status, title, comment, start_date_project,
                end_date_project, address_site, token):
    url = "http://127.0.0.1:8000/user-project/project/string1/"

    payload = json.dumps({
        "participants": [
            {
                "first_name": first_name,
                "last_name": last_name,
                "email": email
            }
        ],
        "type_project": {
            "project_type": project_type
        },
        "complexity": {
            "complexity": complexity
        },
        "project_status": {
            "status": status
        },
        "title": title,
        "comment": comment,
        "start_date_project": start_date_project,
        "end_date_project": end_date_project,
        "address_site": address_site
    })
    headers = {
        'Authorization': 'Token '+ token,
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=L0woWx8TnXBzBwfh1bNqYNpivPIgNs0u'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    yield response

@pytest.fixture
# Подивитись до цього тесту!!!
def delete_project(token):
    url = "http://127.0.0.1:8000/user-project/project/string2/"

    payload = {}
    headers = {
        'Authorization': 'Token '+ token,
        'Cookie': 'csrftoken=L0woWx8TnXBzBwfh1bNqYNpivPIgNs0u'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)
    yield response

@pytest.fixture
def registration_a_new_participant_in_baza_trainee(first_name, last_name, speciality, phone_number, email,
                                                   account_discord, account_linkedin, city, experience, project,
                                                   conditions_participation, processing_personal_data,type_participant):
    url = "http://localhost:8000/user-project/join/"

    payload = json.dumps({
        "first_name": first_name,
        "last_name": last_name,
        "speciality": speciality,
        "phone_number":phone_number,
        "email": email,
        "account_discord": account_discord,
        "account_linkedin": account_linkedin,
        "city": city,
        "experience": experience,
        "project": project,
        "conditions_participation": conditions_participation,
        "processing_personal_data": processing_personal_data,
        "type_participant": type_participant
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    yield response

@pytest.fixture
def search_participant_by_last_name(token):
    url = "http://localhost:8000/user-project/filter-participant/?last_name=Maruv"

    payload = {}
    headers = {
        'Authorization': 'Token '+ token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    yield response


@pytest.fixture
def search_participant_by_speciality(token):
    url = "http://localhost:8000/user-project/filter-participant/?last_name=Maruv"

    payload = {}
    headers = {
        'Authorization': 'Token '+ token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    yield response


@pytest.fixture
def search_project_by_title(token):
    url = "http://localhost:8000/user-project/filter-project/?title=string"

    payload = {}
    headers = {
        'Authorization': 'Token '+ token
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    yield response
# @pytest.fixture
# def test(token):
#     url = "http://localhost:8000/user-project/projects/"
#
#     payload = {}
#     headers = {
#         'Authorization': 'Token '+ token
#     }
#
#     response = requests.request("GET", url, headers=headers, data=payload)
#     yield response
