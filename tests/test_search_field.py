import requests
import pytest


class TestSearchField:
    lastnames = []
    ids_lastnames = []

    @pytest.mark.parametrize("lastname, status_code", lastnames, ids=ids_lastnames)
    def test_search_participant_by_lastname(self, token, lastname, status_code):
        url = f"http://localhost:8000/user-project/filter-participant/?last_name={lastname}"

        payload = {}
        headers = {
            'Authorization': 'Token '+token
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        assert response.status_code == status_code

    speciality = []
    ids_speciality = []

    @pytest.mark.parametrize("speciality, status_code",speciality,ids=ids_speciality)
    def test_search_participant_by_speciality(self, token,speciality,status_code):
        url = f"http://localhost:8000/user-project/filter-participant/?speciality={speciality}"

        payload = {}
        headers = {
            'Authorization': 'Token '+token
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        assert response.status_code == status_code

    titles = []
    ids_titles = []
    @pytest.mark.parametrize("title, status_code", titles, ids=ids_titles)
    def test_search_project_by_title(self, token, title, status_code):
        url = f"http://localhost:8000/user-project/filter-project/?title={title}"

        payload = {}
        headers = {
            'Authorization': 'Token '+token
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        assert response.status_code == status_code

