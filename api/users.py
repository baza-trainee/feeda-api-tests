import requests
import logging
import allure

from utils.logger import log_response


class Users:
    def __init__(self, config: dict):
        self.base_url = config.get("base_url")
        self.headers = {"Content-Type": "application/json"}

    @allure.step("Login")
    def login(self, email: str, password: str) -> requests.Response:
        url = f"{self.base_url}/users/login/"
        data = {"email": email, "password": password}

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

    @allure.step("Logout")
    def logout(self, data: dict) -> requests.Response:
        url = f"{self.base_url}/users/logout/"

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

    @allure.step("Complete password reset")
    def password_reset_complete(self, data: dict) -> requests.Response:
        url = f"{self.base_url}/users/password-reset-complete/"

        try:
            response = requests.patch(url, headers=self.headers, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"An error occurred: {err}")
            raise err
        except Exception as err:
            logging.error(f"An unknown error occurred: {err}")
            raise err

        log_response(response)

        return response

    @allure.step("Verify password reset")
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

    @allure.step("Reset password email")
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
