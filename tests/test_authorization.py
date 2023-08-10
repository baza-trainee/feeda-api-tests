import pytest

from utils.google_auth import process_messages


class TestAuth:
    @pytest.mark.parametrize(
        "email,password,status_code",
        [
            pytest.param(
                "kozlov2777@gmail.com",
                "Baza12345",
                200,
                id="The system returns status code 200 if the request is successful",
            ),
            pytest.param(
                "example@gmail.com",
                "Baza12345",
                400,
                id="The system returns status code 400 if invalid credentials are passed in the request body "
                "(email does not belong to the admin)",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "Baza",
                400,
                id="The system returns status code 400 if invalid credentials are passed in the request body "
                "(password does not belong to the admin)",
            ),
            pytest.param(
                "T" * 5,
                "Baza12345",
                400,
                id="The system returns status code 400 if invalid data is passed in the request body (email of "
                "invalid length minlength-1)",
            ),
            pytest.param(
                "T" * 71,
                "Baza12345",
                400,
                id="The system returns status code 400 if invalid data is passed in the request body (email of "
                "invalid length maxlength+1)",
            ),
            pytest.param(
                "a@gmail.com",
                "baza12345",
                400,
                id="The system returns status code 400 if invalid data is passed in the request body (email of "
                "invalid format)",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "T",
                400,
                id="The system returns status code 400 if invalid data is passed in the request body (password of "
                "invalid length minlength-1)",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "T" * 13,
                400,
                id="The system returns status code 400 if invalid data is passed in the request body (password of "
                "invalid length maxlength+1)",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "BAZA12345",
                400,
                id="The system returns status code 400 if invalid data is passed in the request body (password of "
                "invalid format - without a lowercase Latin letter)",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "baza12345",
                400,
                id="The system returns status code 400 if invalid data is passed in the request body (password of "
                "invalid format - without an uppercase Latin letter)",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "Baza",
                400,
                id="The system returns status code 400 if invalid data is passed in the request body (password of "
                "invalid format - without a digit)",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "база123",
                400,
                id="The system returns status code 400 if invalid data is passed in the request body (password of "
                "invalid format - in Cyrillic)",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "@Baza123",
                400,
                id="The system returns status code 400 if invalid data is passed in the request body (password of "
                "invalid format - with special characters)",
            ),
            pytest.param(
                "kozlov2777@gmail.com",
                "",
                400,
                id="The system returns status code 400 if invalid data is passed in the request body (empty one "
                "required field)",
            ),
            pytest.param(
                "",
                "",
                400,
                id="The system returns status code 400 if invalid data is passed in the request body (empty all fields)",
            ),
            pytest.param(
                " ",
                " ",
                400,
                id="The system returns status code 400 if invalid data is passed in the request body (space all fields)",
            ),
        ],
    )
    def test_login(self, email, password, status_code, users):
        response = users.login(email=email, password=password)

        assert response.status_code == status_code

    # TODO: add expected result, when bug will be fixed
    @pytest.mark.parametrize(
        "email,status_code",
        [
            pytest.param(
                "qafeeda123@gmail.com",
                200,
                id="The system returns status code 200 if the request is successful.",
            ),
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
    def test_request_for_reset_password(self, email, status_code, users):
        payload = {"email": email}
        response = users.reset_password_email(data=payload)

        assert response.status_code == status_code

    @pytest.mark.parametrize(
        "password,confirm_password",
        [pytest.param("QABaza546", "QABaza546", id="reset new password")],
    )
    def test_reset_password(self, password, confirm_password, users):
        uidb64, token = process_messages()
        payload = {
            "password": password,
            "confirm_password": confirm_password,
            "token": token,
            "uidb64": uidb64,
        }

        response = users.password_reset_complete(data=payload)

        assert response.status_code == 201

    @pytest.mark.parametrize(
        "email,password,status_code",
        [
            pytest.param(
                "qafeeda123@gmail.com",
                "QABaza546",
                200,
                id="check that return code 200 with new password",
            ),
            pytest.param(
                "qafeeda123@gmail.com",
                "BazaQA123",
                400,
                id="check that return code 400 with old password",
            ),
        ],
    )
    def test_login_with_new_password(self, email, password, status_code, users):
        response = users.login(email=email, password=password)

        assert response.status_code == status_code

    def test_logout(self, users, config):
        login_response = users.login(
            email=config.get("username"), password=config.get("password")
        )
        payload = {"token": login_response.json()["token"]}

        response = users.logout(data=payload)

        assert response.status_code == 200

    @pytest.mark.parametrize(
        "email,status_code",
        [
            pytest.param("qafeeda123@gmail.com", 200, id="request return old password"),
        ],
    )
    def test_post_condition_request_for_reset_password(self, email, status_code, users):
        payload = {"email": email}

        response = users.reset_password_email(data=payload)

        assert response.status_code == status_code

    @pytest.mark.parametrize(
        "password,confirm_password",
        [
            pytest.param("BazaQA123", "BazaQA123", id="return old password"),
        ],
    )
    def test_post_condition_reset_password(self, password, confirm_password, users):
        uidb64, token = process_messages()
        payload = {
            "password": password,
            "confirm_password": confirm_password,
            "token": token,
            "uidb64": uidb64,
        }

        response = users.password_reset_complete(data=payload)

        assert response.status_code == 201

    # def test_old_login(self):
    #     self.test_login
