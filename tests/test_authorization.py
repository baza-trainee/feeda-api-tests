import pytest
import time
from assertpy import assert_that, soft_assertions

from utils.google_auth import process_messages


LOGIN_ERRORS = {
    "email does not belong to the admin": "Invalid data",
    "password does not belong to the admin": "Invalid data",
    "email invalid length minlength-1": "Enter a valid email address.",
    "email invalid length maxlength+1": "Enter a valid email address.",
    "email invalid format": "Enter a valid email address.",
    "email_invalid_empty": "This field may not be blank.",
    "email_invalid_null": "This field may not be null.",
    "password invalid length minlength-1": "Invalid data",
    "password invalid length maxlength+1": "Invalid data",
    "password invalid format - without a lowercase Latin letter": "Invalid data",
    "password invalid format - without an uppercase Latin letter": "Invalid data",
    "password invalid format - without a digit": "Invalid data",
    "password invalid format - in Cyrillic": "Invalid data",
    "password invalid format - with special characters": "Invalid data",
    "password invalid empty": "This field may not be blank.",
    "password invalid null": "This field may not be null.",
}
RESET_PASSWORD_EMAIL_ERRORS = {
    "invalid length minlength-1": "Enter a valid email address.",
    "invalid length maxlength+1": "Enter a valid email address.",
    "email of invalid format.": "Enter a valid email address.",
    "empty email field": "This field may not be blank.",
    "null email field": "This field may not be null.",
}

class TestAuth:
    @pytest.mark.parametrize(
        "email,password,status_code",
        [
            pytest.param(
                "admin123@gmail.com",
                "Feeda12345",
                200,
            ),
        ],
    )
    def test_login_success(self, email, password, status_code, users):
        response = users.login(email=email, password=password)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()).contains_key("token")

    @pytest.mark.parametrize(
        "email,password,status_code",
        [
            pytest.param(
                "a@ukr",
                "Feeda12345",
                400,
                id="email invalid length minlength-1",
            ),
            pytest.param(
                "T" * 71,
                "Feeda12345",
                400,
                id="email invalid length maxlength+1",
            ),
            pytest.param(
                1,
                "Feeda12345",
                400,
                id="email invalid format",
            ),
            pytest.param(
                "",
                "Feeda12345",
                400,
                id="email_invalid_empty",
            ),
            pytest.param(
                None,
                "Feeda12345",
                400,
                id="email_invalid_null",
            )

        ],
    )
    def test_login_email_errors(self, email, password, status_code, users, test_id):
        response = users.login(email=email, password=password)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["email"][0]).is_equal_to(LOGIN_ERRORS[test_id])

    @pytest.mark.parametrize(
        "email,password,status_code",
        [

            pytest.param(
                "admin123@gmail.com",
                "Baza",
                400,
                id="password does not belong to the admin",
            ),
            pytest.param(
                "admin123@gmail.com",
                "Bazank1",
                400,
                id="password invalid length minlength-1",
            ),
            pytest.param(
                "admin123@gmail.com",
                "T" * 60,
                400,
                id="password invalid length maxlength+1",
            ),
            pytest.param(
                "admin123@gmail.com",
                "BAZA12345",
                400,
                id="password invalid format - without a lowercase Latin letter",
            ),
            pytest.param(
                "admin123@gmail.com",
                "baza12345",
                400,
                id="password invalid format - without an uppercase Latin letter",
            ),
            pytest.param(
                "admin123@gmail.com",
                "Baza",
                400,
                id="password invalid format - without a digit",
            ),
            pytest.param(
                "admin123@gmail.com",
                "база123",
                400,
                id="password invalid format - in Cyrillic",
            ),
            pytest.param(
                "admin123@gmail.com",
                "@Baza123",
                400,
                id="password invalid format - with special characters",
            ),


        ],
    )
    def test_login_password_errors(self, email, password, status_code, users, test_id):
        response = users.login(email=email, password=password)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["message"]).is_equal_to(LOGIN_ERRORS[test_id])

    @pytest.mark.parametrize(
        "email,password,status_code",
        [

            pytest.param(
                "example@gmail.com",
                "Feeda12345",
                400,
                id="email does not belong to the admin",
            ),
            pytest.param(
                "admin123@gmail.com",
                "Baza",
                400,
                id="password does not belong to the admin",
            ),
        ],
    )
    def test_login_wrong_credentials_errors(self, email, password, status_code, users, test_id):
        response = users.login(email=email, password=password)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["message"]).is_equal_to(LOGIN_ERRORS[test_id])

    @pytest.mark.parametrize(
        "email,password,status_code",
        [
            pytest.param(
                "admin123@gmail.com",
                "",
                400,
                id="password invalid empty",
            ),
            pytest.param(
                "admin123@gmail.com",
                None,
                400,
                id="password invalid null",
            ),
        ],
    )
    def test_login_empty_and_null_password_errors(self, email, password, status_code, users, test_id):
        response = users.login(email=email, password=password)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["password"][0]).is_equal_to(LOGIN_ERRORS[test_id])



    @pytest.mark.parametrize(
        "email,status_code",
        [
            pytest.param(
                "qafeeda123@gmail.com",
                200,
                id="The system returns status code 200 if the request is successful.",
            ),
        ],
    )
    def test_reset_password_email_success(self, email, status_code, users):
        payload = {"email": email}
        response = users.reset_password_email(data=payload)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)

    @pytest.mark.parametrize(
        "email,status_code",
        [
            pytest.param(
                "k@g.c",
                400,
                id="invalid length minlength-1",
            ),
            pytest.param(
                "k" * 71,
                400,
                id="invalid length maxlength+1",
            ),
            pytest.param(
                "kozlov2777gmailcom",
                400,
                id="email of invalid format.",
            ),
            pytest.param(
                "",
                400,
                id="empty email field",
            ),
            pytest.param(
                None,
                400,
                id="null email field",
            ),
        ],
    )
    def test_reset_password_email_errors(self, email, status_code, users, test_id):
        payload = {"email": email}
        response = users.reset_password_email(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["email"][0]).is_equal_to(RESET_PASSWORD_EMAIL_ERRORS[test_id])

    @pytest.mark.parametrize(
        "password,confirm_password,email",
        [
            pytest.param(
                "Baza12345",
                "Baza12345",
                "qafeeda123@gmail.com",
                id="reset new password",
            )
        ],
    )
    def test_new_password(self, password, confirm_password, email, users):
        payload = {"email": email}
        users.reset_password_email(data=payload)
        time.sleep(5)
        uidb64, token = process_messages()[0]
        payload = {
            "password": password,
            "confirm_password": confirm_password,
            "token": token,
            "uidb64": uidb64,
        }
        response = users.password_reset_complete(data=payload)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(201)
        time.sleep(5)
        response = users.login(email=email, password=password)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)

    def test_logout_success(self, users, config):
        login_response = users.login(
            email=config.get("username"), password=config.get("password")
        )
        payload = {"token": login_response.json()["token"]}

        response = users.logout(data=payload)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)

    def test_logout_errors(self, users, config):
        login_response = users.login(
            email=config.get("username"), password=config.get("password")
        )
        payload = {"token": login_response.json()["token"] + "wrong_token"}

        response = users.logout(data=payload)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(404)
