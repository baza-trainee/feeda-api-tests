import pytest

from assertpy import assert_that, soft_assertions

from utils.google_auth import process_messages


LOGIN_ERRORS = {
    "email does not belong to the admin": "Invalid data",
    "password does not belong to the admin": "Invalid data",
    "email invalid length minlength-1": "Enter a valid email address.",
    "email invalid length maxlength+1": "Enter a valid email address.",
    "invalid format": "Email invalid",
    "password invalid length minlength-1": "Ensure this field has at least 2 characters.",
    "password invalid length maxlength+1": "Invalid data",
    "invalid format - without a lowercase Latin letter": "Invalid data",
    "invalid format - without an uppercase Latin letter": "Invalid data",
    "invalid format - without a digit": "Invalid data",
    "invalid format - in Cyrillic": "Invalid data",
    "invalid format - with special characters": "Invalid data",
    "empty one required field": "This field may not be blank.",
    "empty all fields": "This field may not be blank.",
    "space all fields": "This field may not be blank.",
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
                "example@gmail.com",
                "Baza12345",
                400,
                id="email does not belong to the admin",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "Baza",
                400,
                id="password does not belong to the admin",
            ),
            pytest.param(
                "T" * 5,
                "Baza12345",
                400,
                id="invalid length minlength-1",
            ),
            pytest.param(
                "T" * 71,
                "Baza12345",
                400,
                id="invalid length maxlength+1",
            ),
            pytest.param(
                "a@gmail.com",
                "baza12345",
                400,
                id="invalid format",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "T",
                400,
                id="invalid length minlength-1",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "T" * 13,
                400,
                id="invalid length maxlength+1",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "BAZA12345",
                400,
                id="invalid format - without a lowercase Latin letter",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "baza12345",
                400,
                id="invalid format - without an uppercase Latin letter",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "Baza",
                400,
                id="invalid format - without a digit",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "база123",
                400,
                id="invalid format - in Cyrillic",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "@Baza123",
                400,
                id="invalid format - with special characters",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "",
                400,
                id="empty one required field",
            ),
            pytest.param(
                "",
                "",
                400,
                id="empty all fields",
            ),
            pytest.param(
                " ",
                " ",
                400,
                id="space all fields",
            ),
        ],
    )
    def test_login_errors(self, email, password, status_code, users, test_id):
        response = users.login(email=email, password=password)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            # assert_that(response.json()["message"][0]).is_equal_to(LOGIN_ERRORS[test_id])




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
                id="The system returns status code 400 if invalid data is passed in the request body (email of "
                "invalid length minlength-1).",
            ),
            pytest.param(
                "k" * 71,
                400,
                id="The system returns status code 400 if invalid data is passed in the request body (email of "
                "invalid length maxlength+1).",
            ),
            pytest.param(
                "kozlov2777gmailcom",
                400,
                id="The system returns status code 400 if invalid data is passed (email of invalid format).",
            ),
            pytest.param(
                "",
                400,
                id="The system returns status code 400 if invalid data is passed (empty email field).",
            ),
        ],
    )
    def test_reset_password_email_errors(self, email, status_code, users):
        payload = {"email": email}
        response = users.reset_password_email(data=payload)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)

    @pytest.mark.parametrize(
        "password,confirm_password,email",
        [
            pytest.param(
                "QABaza546",
                "QABaza546",
                "qafeeda123@gmail.com",
                id="reset new password",
            )
        ],
    )
    def test_new_password(self, password, confirm_password, email, users):
        payload = {"email": email}
        users.reset_password_email(data=payload)
        uidb64, token = process_messages()[-1]
        payload = {
            "password": password,
            "confirm_password": confirm_password,
            "token": token,
            "uidb64": uidb64,
        }
        response = users.password_reset_complete(data=payload)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(201)

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
