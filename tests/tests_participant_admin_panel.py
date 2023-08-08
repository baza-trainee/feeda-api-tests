import pytest
import json
import requests


class TestParticipantsPageOfTheAdminPanel:
    data_for_create_participant_admin = [
        (
            "Anastasia",
            "Luzina",
            1,
            "+380999999999",
            "testing@gmail.com",
            "Valid comment",
            "anastasiia#1234",
            "https://www.linkedin.com/in/anastasiia",
            "city",
            True,
            1,
            "QA Manual",
            201,
        ),
        (
            "A",
            "Luzina",
            1,
            "+380999999999",
            "testing@gmail.com",
            "Valid comment",
            "anastasiia#1234",
            "https://www.linkedin.com/in/anastasiia",
            "city",
            True,
            1,
            "QA Manual",
            400,
        ),
        (
            "A" * 21,
            "Luzina",
            1,
            "+380999999999",
            "testing@gmail.com",
            "Valid comment",
            "anastasiia#1234",
            "https://www.linkedin.com/in/anastasiia",
            "city",
            True,
            1,
            "QA Manual",
            400,
        ),
    ]

    ids_for_data_for_create_participant_admin = [
        "Verify that the server returns status code 201 (Created) with the correct data for adding a participant to the project.",
        "The system returns status code 400 if invalid data is passed in the request body (first_name is invalid minlength-1).",
        "The system returns status code 400 if invalid data is passed in the request body (first_name of invalid length maxlength+1).",
    ]

    # "The system returns status code 400 if invalid data is passed in the request body (first_name of invalid length NULL).",
    # "The system returns status code 400 if invalid data is passed in the request body (last_name is invalid minlength-1).",
    # "The system returns status code 400 if invalid data is passed in the request body (last_name is invalid maxlength+1).",
    # "The system returns status code 400 if invalid data is passed in the request body (last_name is invalid length NULL).",
    # "The system returns status code 400 if invalid data is passed in the request body (speciality invalid length NULL).",
    # "The system returns status code 400 if invalid data is passed in the request body (phone_number of invalid length minlength-1).",
    # "The system returns status code 400 if invalid data is passed in the request body (phone_number of invalid length maxlength+1).",
    # "The system returns status code 400 if invalid data is passed in the request body (phone_number of invalid length NULL).",
    # "The system returns status code 400 if invalid data is passed in the request body (email of invalid length minlength-1).",
    # "The system returns status code 400 if invalid data is passed in the request body (email of invalid length maxlength+1).",
    # "The system returns status code 400 if invalid data is passed in the request body (email of invalid length NULL).",
    # "The system returns status code 400 if invalid data is passed in the request body (email of an invalid format).",
    # "The system returns status code 400 if invalid data is passed in the request body (discord of invalid length minlength-1).",
    # "The system returns status code 400 if invalid data is passed in the request body (discord of invalid length maxlength+1).",
    # "The system returns status code 400 if invalid data is passed in the request body (discord invalid length NULL).",
    # "The system returns status code 400 if invalid data is passed in the request body (city of invalid length minlength-1).",
    # "The system returns status code 400 if invalid data is passed in the request body (city of invalid length maxlength+1).",
    # "The system returns status code 400 if invalid data is passed in the request body (city of invalid length NULL).",
    # "The system returns status code 400 if you pass invalid data in the request body (experience is invalid length NULL).",
    # "The system returns status code 400 if invalid data is passed in the request body (stack of invalid length minlength-1).",
    # "The system returns status code 400 if invalid data is passed in the request body (stack of invalid length maxlength+1).",
    # "The system returns status code 400 if invalid data is passed in the request body (invalid length stack NULL).",
    # "The system returns status code 400 if you try to add a participant to a non-existent project"

    @pytest.mark.parametrize(
        "first_name, last_name, speciality, phone_number, email, comment, account_discord, account_linkedin, city,"
        " experience, project, stack, status_code_for_create",
        data_for_create_participant_admin,
        ids=ids_for_data_for_create_participant_admin,
    )
    def test_create_participant(
        self,
        token,
        first_name,
        last_name,
        speciality,
        phone_number,
        email,
        comment,
        account_discord,
        account_linkedin,
        city,
        experience,
        project,
        stack,
        status_code_for_create,
    ):
        url = "http://localhost:8000/user-project/add-participant/"
        payload = json.dumps(
            {
                "first_name": first_name,
                "last_name": last_name,
                "speciality": speciality,
                "phone_number": phone_number,
                "email": email,
                "comment": comment,
                "account_discord": account_discord,
                "account_linkedin": account_linkedin,
                "city": city,
                "experience": experience,
                "project": project,
                "stack": stack,
            }
        )
        headers = {
            "Authorization": "Token " + token,
            "Content-Type": "application/json",
        }
        response_create = requests.request("POST", url, headers=headers, data=payload)
        assert response_create.status_code == status_code_for_create

    def get_id_participant(self, create_participant):
        response = create_participant
        parsed_response = response.json()
        participant_id = parsed_response.get("id")
        return participant_id

    data = [
        (
            "Anna",
            "Luzina",
            1,
            "+380999999999",
            "testing@gmail.com",
            "Valid comment",
            "anastasiia#1234",
            "https://www.linkedin.com/in/anastasiia",
            "city",
            True,
            1,
            "QA Manual",
            201,
        )
    ]
    ids_for_update = ["test"]

    @pytest.mark.parametrize(
        "first_name, last_name, speciality, phone_number, email, comment, account_discord, account_linkedin, city,"
        " experience, project, stack, status_code",
        data,
        ids=ids_for_update,
    )
    def test_update_participant(
        self,
        token,
        create_participant,
        first_name,
        last_name,
        speciality,
        phone_number,
        email,
        comment,
        account_discord,
        account_linkedin,
        city,
        experience,
        project,
        stack,
        status_code,
    ):
        participant_id = self.get_id_participant(create_participant)
        url = f"http://localhost:8000/user-project/participant-detail/{participant_id}/"
        payload = json.dumps(
            {
                "first_name": first_name,
                "last_name": last_name,
                "speciality": speciality,
                "phone_number": phone_number,
                "email": email,
                "comment": comment,
                "account_discord": account_discord,
                "account_linkedin": account_linkedin,
                "city": city,
                "experience": experience,
                "project": project,
                "stack": stack,
            }
        )
        headers = {
            "Authorization": "Token " + token,
            "Content-Type": "application/json",
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        assert response.status_code == status_code

    def test_get_participant_by_id(self, token, create_participant):
        participant_id = self.get_id_participant(create_participant)
        url = f"http://localhost:8000/user-project/get-participant/{participant_id}/"
        payload = {}
        headers = {
            "Authorization": "Token " + token,
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()

    def test_get_all_participant(self, token, create_participant):
        url = "http://localhost:8000/user-project/participants-list/"

        payload = {}
        headers = {
            "Authorization": "Token " + token,
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response.raise_for_status()

    def test_delete(self, token, create_participant):
        participant_id = self.get_id_participant(create_participant)
        url = f"http://localhost:8000/user-project/participant-detail/{participant_id}/"
        payload = {}
        headers = {"Authorization": "Token " + token}
        response_delete = requests.request("DELETE", url, headers=headers, data=payload)
        assert response_delete.status_code == 200
