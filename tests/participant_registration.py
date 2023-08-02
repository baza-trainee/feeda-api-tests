import pytest
import requests
import json


class TestParticipantRegistration:
    data = []
    ids = []
    @pytest.mark.parametrize("first_name, last_name, stack, phone_number, email, account_discord, "
                             "account_linkedin, city, experience, project, conditions_participation, "
                             "processing_personal_data, type_participant, status_code", data, ids=ids)
    def test_participant_registration(self, token, first_name, last_name, stack, phone_number, email, account_discord,
                                      account_linkedin, city, experience, project, conditions_participation,
                                      processing_personal_data, type_participant, status_code):
        url = "http://localhost:8000/user-project/join/"

        payload = json.dumps({
            "first_name": first_name,
            "last_name": last_name,
            "stack": stack,
            "phone_number": phone_number,
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
            'Authorization': 'Token '+ token,
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        assert response.status_code == status_code