import json
import pytest
import requests


class TestAuth:
    data_for_tests_login = [
        ("kozlov2777@gmail.com", "Baza12345", 200),
        ("example@gmail.com", "Baza12345", 400),
        ("kozlov2777@gmail.com", "Baza", 400),
        ("T" * 5, "Baza12345", 400),
        ("T" * 71, "Baza12345", 400),
        ("a@gmail.com", "baza12345", 400),
        ("kozlov2777@gmail.com", "T", 400),
        ("kozlov2777@gmail.com", "T" * 13, 400),
        ("kozlov2777@gmail.com", "BAZA12345", 400),
        ("kozlov2777@gmail.com", "baza12345", 400),
        ("kozlov2777@gmail.com", "Baza", 400),
        ("kozlov2777@gmail.com", "база123", 400),
        ("kozlov2777@gmail.com", "@Baza123", 400),
        ("kozlov2777@gmail.com", "", 400),
        ("", "", 400),
        (" ", " ", 400),
    ]
    ids_for_data_for_tests_login = [
        "The system returns status code 200 if the request is successful",
        "The system returns status code 400 if invalid credentials are passed in the request body (email does not belong to the admin)",
        "The system returns status code 400 if invalid credentials are passed in the request body (password does not belong to the admin)",
        "The system returns status code 400 if invalid data is passed in the request body (email of invalid length minlength-1)",
        "The system returns status code 400 if invalid data is passed in the request body (email of invalid length maxlength+1)",
        "The system returns status code 400 if invalid data is passed in the request body (email of invalid format)",
        "The system returns status code 400 if invalid data is passed in the request body (password of invalid length minlength-1)",
        "The system returns status code 400 if invalid data is passed in the request body (password of invalid length maxlength+1)",
        "The system returns status code 400 if invalid data is passed in the request body (password of invalid format - without a lowercase Latin letter)",
        "The system returns status code 400 if invalid data is passed in the request body (password of invalid format - without an uppercase Latin letter)",
        "The system returns status code 400 if invalid data is passed in the request body (password of invalid format - without a digit)",
        "The system returns status code 400 if invalid data is passed in the request body (password of invalid format - in Cyrillic)",
        "The system returns status code 400 if invalid data is passed in the request body (password of invalid format - with special characters)",
        "The system returns status code 400 if invalid data is passed in the request body (empty one required field)",
        "The system returns status code 400 if invalid data is passed in the request body(empty all fields)",
        "The system returns status code 400 if invalid data is passed in the request body(space all fields)"
    ]
    data_for_test_request_for_reset_password = [
        ("qafeeda123@gmail.com", 200),
        ("k@g.c", 400),
        ("k" * 71, 400),
        ("kozlov2777gmailcom", 400),
        ("", 400),
    ]
    ids_for_test_request_for_reset_password = [
        "The system returns status code 200 if the request is successful.",
        "The system returns status code 400 if invalid data is passed in the request body (email of invalid length minlength-1).",
        "The system returns status code 400 if invalid data is passed in the request body (email of invalid length maxlength+1).",
        "The system returns status code 400 if invalid data is passed (email of invalid format).",
        "The system returns status code 400 if invalid data is passed (empty email field)."
    ]
    data_for_reset = [
        ("QABaza546", "QABaza546")
    ]
    ids_data_for_reset = [
        'reset new password'
    ]
    data_for_login_with_new_password = [
        ("qafeeda123@gmail.com", "QABaza546", 200),
        ("qafeeda123@gmail.com", "BazaQA123", 400)
    ]
    ids_for_login_with_new_password = [
        'check that return code 200 with new password',
        'check that return code 400 with old password'
    ]
    email_for_post_condition = [
        ("qafeeda123@gmail.com", 200)
    ]
    ids_for_email_for_post_condition = [
        'request return old password'
    ]
    data_post_condition_password = [
        ("BazaQA123", "BazaQA123")
    ]
    ids_for_data_post_condition_password = [
        "return old password"
    ]

    @pytest.mark.parametrize("email, password, status_code", data_for_tests_login, ids=ids_for_data_for_tests_login)
    def test_login(self, email, password, status_code):
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
        assert response.status_code == status_code

    # Добавити очікуваний результат на текст респонсу, коли буде виправлено баг
    @pytest.mark.parametrize("email, status_code", data_for_test_request_for_reset_password,
                             ids=ids_for_test_request_for_reset_password)
    def test_request_for_reset_password(self, email, status_code):
        url = "http://localhost:8000/users/reset-password-email/"

        payload = json.dumps({
            "email": email
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == status_code

    @pytest.mark.parametrize("password, confirm_password", data_for_reset, ids=ids_data_for_reset)
    def test_reset_password(self, password, confirm_password):
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
        assert response.status_code == 201

    @pytest.mark.parametrize("email, password, status_code", data_for_login_with_new_password,
                             ids=ids_for_login_with_new_password)
    def test_login_with_new_password(self, email, password, status_code):
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
        assert response.status_code == status_code

    def test_logout(self, token):
        url = "http://localhost:8000/users/logout/"

        payload = ""
        headers = {
            'Authorization': 'Token ' + token
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)
        assert response.status_code == 200

    @pytest.mark.parametrize("email, status_code", email_for_post_condition,
                             ids=ids_for_email_for_post_condition)
    def test_post_condition_request_for_reset_password(self, email, status_code):
        url = "http://localhost:8000/users/reset-password-email/"

        payload = json.dumps({
            "email": email
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        assert response.status_code == status_code

    @pytest.mark.parametrize("password, confirm_password", data_post_condition_password,
                             ids=ids_for_data_post_condition_password)
    def test_post_condition_reset_password(self, password, confirm_password):
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
        assert response.status_code == 201

    def test_old_login(self):
        self.test_login
