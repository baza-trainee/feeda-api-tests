import os
import requests
import logging

from utils.logger import log_response


class UserProject:
    def __init__(self, token: str):
        self.base_url = os.environ["BASE_URL"]
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Token {self.token}"
        }

    def add_participant(self, data: dict) -> requests.Response:
        url = f"{self.base_url}/user-project/add-participant/"

        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

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

    def command_update(self, cmd_id: str, data: dict) -> requests.Response:
        url = f"{self.base_url}/user-project/command-update/{cmd_id}/"

        try:
            response = requests.put(url, headers=self.headers, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    def create_command(self, data: dict) -> requests.Response:
        url = f"{self.base_url}/user-project/command/"

        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

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

    def create_project(self, data: dict) -> requests.Response:
        url = f"{self.base_url}/user-project/create-project/"

        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    def filter_participant(self) -> requests.Response:
        url = f"{self.base_url}/user-project/filter-participant/"

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

    def filter_project(self) -> requests.Response:
        url = f"{self.base_url}/user-project/filter-project/"

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

    def get_participant(self, participant_id: str) -> requests.Response:
        url = f"{self.base_url}/user-project/get-participant/{participant_id}/"

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

    def join(self, data: dict) -> requests.Response:
        url = f"{self.base_url}/user-project/join/"

        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    def update_participant(self, participant_id: str, data: dict) -> requests.Response:
        url = f"{self.base_url}/user-project/participant-detail/{participant_id}/"

        try:
            response = requests.put(url, headers=self.headers, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    def delete_participant(self, participant_id: str) -> requests.Response:
        url = f"{self.base_url}/user-project/participant-detail/{participant_id}/"

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

    def get_participants_list(self) -> requests.Response:
        url = f"{self.base_url}/user-project/participants-list/"

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

    def user_project_project_read(self, project_url: str) -> requests.Response:
        url = f"{self.base_url}/user-project/project/{project_url}/"

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

    def user_project_project_update(self, project_url: str, data: dict) -> requests.Response:
        url = f"{self.base_url}/user-project/project/{project_url}/"

        try:
            response = requests.put(url, headers=self.headers, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    def user_project_project_delete(self, project_url: str) -> requests.Response:
        url = f"{self.base_url}/user-project/project/{project_url}/"

        try:
            response = requests.delete(url, headers=self.headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    def user_project_projects_list(self) -> requests.Response:
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

    def user_project_send_read(self, user_id: str) -> requests.Response:
        url = f"{self.base_url}/user-project/send/{user_id}/"

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
