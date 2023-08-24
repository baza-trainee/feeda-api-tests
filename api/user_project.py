import requests
import logging
import allure

from utils.logger import log_response


class UserProject:
    def __init__(self, token: str, config: dict):
        self.base_url = config.get("base_url")
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Token {self.token}",
        }

    @allure.step("Add participant")
    def add_participant(self, data: dict) -> requests.Response:
        url = f"{self.base_url}/user-project/add-participant/"

        try:
            response = requests.post(url, headers=self.headers, json=data)
            if response.status_code != 400:
                response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Delete command")
    def command_delete(self, cmd_id: str) -> requests.Response:
        url = f"{self.base_url}/user-project/command-delete/{cmd_id}/"

        try:
            response = requests.delete(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Update command")
    def command_update(self, cmd_id: str, data: dict) -> requests.Response:
        url = f"{self.base_url}/user-project/command-update/{cmd_id}/"

        try:
            response = requests.put(url, headers=self.headers, json=data)
            if response.status_code != 404:
                response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Create command")
    def create_command(self, data: dict) -> requests.Response:
        url = f"{self.base_url}/user-project/command/"

        try:
            response = requests.post(url, headers=self.headers, json=data)
            if response.status_code != 400:
                response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Get commands")
    def get_commands(self) -> requests.Response:
        url = f"{self.base_url}/user-project/commands/"

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Create project")
    def create_project(self, data: dict) -> requests.Response:
        url = f"{self.base_url}/user-project/create-project/"

        try:
            response = requests.post(url, headers=self.headers, json=data)
            if response.status_code != 400:
                response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Filter participant")
    def filter_participant(self) -> requests.Response:
        url = f"{self.base_url}/user-project/filter-participant/"

        try:
            response = requests.get(url)
            if response.status_code != 404:
                response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Filter project")
    def filter_project(self) -> requests.Response:
        url = f"{self.base_url}/user-project/projects/"

        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code != 404:
                response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Get participant")
    def get_participant(self, participant_id: str) -> requests.Response:
        url = f"{self.base_url}/user-project/get-participant/{participant_id}/"

        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code != 404:
                response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Join")
    def join(self, data: dict) -> requests.Response:
        url = f"{self.base_url}/user-project/join/"

        try:
            response = requests.post(url, headers=self.headers, json=data)
            if response.status_code != 400:
                response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Update participant")
    def update_participant(self, participant_id: str, data: dict) -> requests.Response:
        url = f"{self.base_url}/user-project/participant-detail/{participant_id}/"

        try:
            response = requests.put(url, headers=self.headers, json=data)
            if response.status_code != 404:
                response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Delete participant")
    def delete_participant(self, participant_id: str) -> requests.Response:
        url = f"{self.base_url}/user-project/participant-detail/{participant_id}/"

        try:
            response = requests.delete(url, headers=self.headers)
            if response.status_code != 404:
                response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Get participants list")
    def get_participants_list(self) -> requests.Response:
        url = f"{self.base_url}/user-project/participants-list/"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Read project")
    def project_read(self, project_url: str) -> requests.Response:
        url = f"{self.base_url}/user-project/project/{project_url}/"

        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code != 404:
                response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Update project")
    def project_update(self, project_url: str, data: dict) -> requests.Response:
        url = f"{self.base_url}/user-project/project/{project_url}/"

        try:
            response = requests.put(url, headers=self.headers, json=data)
            if response.status_code != 400:
                response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Delete project")
    def project_delete(self, project_url: str) -> requests.Response:
        url = f"{self.base_url}/user-project/project/{project_url}/"

        try:
            response = requests.delete(url, headers=self.headers)
            if response.status_code != 404:
                response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("List projects")
    def projects_list(self) -> requests.Response:
        url = f"{self.base_url}/user-project/projects/"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Send read")
    def send_read(self, user_id: str) -> requests.Response:
        url = f"{self.base_url}/user-project/send/{user_id}/"

        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code != 404:
                response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Search participant")
    def search_participant(self, param: str) -> requests.Response:
        url = f"{self.base_url}/user-project/search-user/?query={param}"

        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response