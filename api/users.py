import os
import requests
import logging

from utils.logger import log_response


class Auth:
    def __init__(self):
        self.base_url = os.environ["BASE_URL"]
        self.headers = {"Content-Type": "application/json"}

    def login(self, email: str, password: str) -> requests.Response:
        url = f"{self.base_url}/users/login/"
        data = {
            "email": email,
            "password": password
        }

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

    def logout(self, token: str) -> requests.Response:
        url = f"{self.base_url}/users/logout/"
        data = {
            "token": token,
        }

        try:
            response = requests.delete(url, headers=self.headers, json=data)
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

    def password_reset_complete(self, new_password_data: dict) -> requests.Response:
        url = f"{self.base_url}/users/password-reset-complete/"

        try:
            response = requests.patch(url, headers=self.headers, json=new_password_data)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    def password_reset_verify(self, uidb64: str, token: str) -> requests.Response:
        url = f"{self.base_url}/users/password-reset/{uidb64}/{token}/"

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

    def reset_password_email(self, data: dict) -> requests.Response:
        url = f"{self.base_url}/users/reset-password-email/"

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
