import requests
import json
import pytest


class TestProjectAdminPanel:
    data = []
    ids = []

    @pytest.mark.parametrize(
        "title, comment, type_project, complexity, project_status, start_date_project,"
        "end_date_project, address_site, status_code",
        data,
        ids=ids,
    )
    def test_create_project(
        self,
        token,
        title,
        comment,
        type_project,
        complexity,
        project_status,
        start_date_project,
        end_date_project,
        address_site,
        status_code,
    ):
        url = "http://localhost:8000/user-project/create-project/"

        payload = json.dumps(
            {
                "title": title,
                "comment": comment,
                "type_project": type_project,
                "complexity": complexity,
                "project_status": project_status,
                "start_date_project": start_date_project,
                "end_date_project": end_date_project,
                "address_site": address_site,
            }
        )
        headers = {
            "Authorization": "Token " + token,
            "Content-Type": "application/json",
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == status_code

    def get_id_participant(self, create_participant):
        response = create_participant
        parsed_response = response.json()
        participant_id = parsed_response.get("id")
        return participant_id

    def get_id_project(self, project):
        response = project
        parsed_response = response.json()
        project_id = parsed_response.get("id")
        return project_id

    def get_url(self, project):
        response = project
        parsed_response = response.json()
        url = parsed_response.get("url")
        return url

    def test_add_participant_to_project(self, token, project, create_participant):
        url = "http://localhost:8000/user-project/command/"

        payload = json.dumps(
            {
                "user": [
                    self.get_id_participant(create_participant=create_participant)
                ],
                "project": self.get_id_project(project=project),
            }
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic " + token,
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.raise_for_status()

    def test_get_view_project(self, token):
        url = "http://localhost:8000/user-project/filter-project/"

        payload = {}
        headers = {"Authorization": "Token " + token}

        response = requests.request("GET", url, headers=headers, data=payload)
        assert response.raise_for_status()

    def test_get_projects(self, token):
        url = "http://localhost:8000/user-project/projects/"

        payload = {}
        headers = {"Authorization": "Token " + token}

        response = requests.request("GET", url, headers=headers, data=payload)
        assert response.raise_for_status()

    # Тут помилка, зробити баг репорт!!
    def test_update_team(self, token, project, create_participant):
        url = f"http://127.0.0.1:8000/user-project/command-update/{self.get_id_project(project=project)}/"

        payload = json.dumps(
            {
                "user": [
                    self.get_id_participant(create_participant=create_participant)
                ],
                "project": {
                    "title": "string",
                    "start_date_project": "2023-07-18",
                    "complexity": {"complexity": "string"},
                },
            }
        )
        headers = {
            "Authorization": "Token 778524f2b854fdb4aad7f9f1f748e6392a250f21",
            "Content-Type": "application/json",
            "Cookie": "csrftoken=L0woWx8TnXBzBwfh1bNqYNpivPIgNs0u",
        }

        response = requests.request("PUT", url, headers=headers, data=payload)
        assert response.raise_for_status()

    # Розібратись з кукі
    data_for_update = []
    ids_for_data_for_update = []

    @pytest.mark.parametrize(
        "first_name, last_name, email, project_type, complexity, status, title, comment,"
        " start_date_project, end_date_project, address_site, status_code",
        data_for_update,
        ids=ids_for_data_for_update,
    )
    def test_update_project(
        self,
        project,
        token,
        first_name,
        last_name,
        email,
        project_type,
        complexity,
        status,
        title,
        comment,
        start_date_project,
        end_date_project,
        address_site,
        status_code,
    ):
        url = f"http://127.0.0.1:8000/user-project/project/{self.get_url(project=project)}/"

        payload = json.dumps(
            {
                "participants": [
                    {"first_name": first_name, "last_name": last_name, "email": email}
                ],
                "type_project": {"project_type": project_type},
                "complexity": {"complexity": complexity},
                "project_status": {"status": status},
                "title": title,
                "comment": comment,
                "start_date_project": start_date_project,
                "end_date_project": end_date_project,
                "address_site": address_site,
            }
        )
        headers = {
            "Authorization": "Token " + token,
            "Content-Type": "application/json",
            "Cookie": "csrftoken=L0woWx8TnXBzBwfh1bNqYNpivPIgNs0u",
        }

        response = requests.request("PUT", url, headers=headers, data=payload)
        assert response.status_code == status_code

    def test_delete_project(self, project, token):
        url = f"http://127.0.0.1:8000/user-project/project/{self.get_url(project=project)}/"

        payload = {}
        headers = {
            "Authorization": "Token " + token,
            "Cookie": "csrftoken=L0woWx8TnXBzBwfh1bNqYNpivPIgNs0u",
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)
        assert response.raise_for_status()
