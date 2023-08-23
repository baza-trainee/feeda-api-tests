import pytest
from assertpy import assert_that, soft_assertions

REGISTRATION_ERRORS = {
        "test_invalid_first_name_min_length": "Ensure this field has at least 2 characters.",
        "test_invalid_first_name_max_length": "Ensure this field has no more than 20 characters.",
        "test_invalid_first_name_null": "This field may not be null.",
        "test_invalid_last_name_min_length": "Ensure this field has at least 2 characters.",
        "test_invalid_last_name_max_length": "Ensure this field has no more than 20 characters.",
        "test_invalid_last_name_null": "This field may not be null.",
        "test_invalid_stack_min_length": "Ensure this field has at least 2 characters.",
        "test_invalid_stack_max_length": "Ensure this field has no more than 300 characters.",
        "test_invalid_stack_null": "This field may not be null.",
        "test_invalid_phone_number_min_length": "The phone number entered is not valid.",
        "test_invalid_phone_number_max_length": "The phone number entered is not valid.",
        "test_invalid_phone_number_null": "This field may not be null.",
        "test_invalid_email_min_length": "Enter a valid email address.",
        "test_invalid_email_max_length": "Ensure this field has no more than 70 characters.",
        "test_invalid_email_null": "This field may not be null.",
        "test_invalid_email_format": "Enter a valid email address.",
        "test_invalid_account_discord_min_length": "Ensure this field has at least 7 characters.",
        "test_invalid_account_discord_max_length": "Ensure this field has no more than 37 characters.",
        "test_invalid_account_discord_null": "This field may not be null.",
        "test_invalid_account_linkedin_min_length": "Ensure this field has at least 19 characters.",
        "test_invalid_account_linkedin_max_length": "Ensure this field has no more than 128 characters.",
        "test_invalid_account_linkedin_null": "This field may not be null.",
        "test_invalid_city_min_length": "Ensure this field has at least 2 characters.",
        "test_invalid_city_max_length": "Ensure this field has no more than 50 characters.",
        "test_invalid_city_null": "This field may not be null.",
        "test_invalid_experience_string": "Must be a valid boolean.",
        "test_invalid_experience_null": "This field may not be null.",
        "test_invalid_type_participant_string": "Incorrect type. Expected pk value, received str.",
        "test_invalid_type_participant_non_allowed_number": "Invalid pk \"1000\" - object does not exist.",
        "test_invalid_type_participant_null": "This field may not be null.",
        "test_invalid_project_string": "Expected a list of items but got type \"str\".",
        "test_invalid_project_non_allowed_number": "Invalid pk \"1000\" - object does not exist.",
        "test_invalid_project_null": "This field may not be null.",
        "test_invalid_conditions_participation_string": "Must be a valid boolean.",
        "test_invalid_conditions_participation_null": "This field may not be null.",
        "test_invalid_conditions_participation_false": "Both conditions_participation and processing_personal_data must be True",
        "test_invalid_processing_personal_data_string": "Must be a valid boolean.",
        "test_invalid_processing_personal_data_null": "This field may not be null.",
        "test_invalid_processing_personal_data_false": "Both conditions_participation and processing_personal_data must be True",
    }


class TestParticipantRegistration:
    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code", [
            pytest.param("A", "Doe", "Backend", "+380999999999", "a@example.com", "asdf#1234",
                         "https://www.linkedin.com/adoe", "New York", True, [1], True, True, 1, 400,
                         id="test_invalid_first_name_min_length"),

            pytest.param("Aaaaaaaaaaaaaaaaaaaaa", "Smith", "Frontend", "+380999999999", "john@example.com", "john#5678",
                         "https://www.linkedin.com/johnsmith", "San Francisco", True, [1], True, True, 1, 400,
                         id="test_invalid_first_name_max_length"),

            pytest.param(None, "Smith", "Frontend", "+380999999999", "john@example.com", "john#5678",
                         "https://www.linkedin.com/johnsmith", "San Francisco", True, [1], True, True, 1, 400,
                         id="test_invalid_first_name_null"),

        ]
    )
    def tests_first_name_errors(
            self,
            user_project,
            first_name,
            last_name,
            stack,
            phone_number,
            email,
            account_discord,
            account_linkedin,
            city,
            experience,
            project,
            conditions_participation,
            processing_personal_data,
            type_participant,
            status_code,
            test_id
    ):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "stack": stack,
            "phone_number": phone_number,
            "email": email,
            "account_discord": account_discord,
            "account_linkedin": account_linkedin,
            "experience": experience,
            "city": city,
            "project": project,
            "conditions_participation": conditions_participation,
            "processing_personal_data": processing_personal_data,
            "type_participant": type_participant
        }
        response = user_project.join(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["first_name"][0]).is_equal_to(REGISTRATION_ERRORS[test_id])

    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code", [
            pytest.param("Jane", "D", "Full Stack", "+380999999999", "jane@example.com", "jane#5678",
                         "https://www.linkedin.com/janed",
                         "San Francisco", True, [1], True, True, 1, 400,
                         id="test_invalid_last_name_min_length"),

            pytest.param("Alice", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "AI", "+380999999999",
                         "alice@example.com",
                         "alice#4321", "https://www.linkedin.com/alice", "Los Angeles", True, [1], True, True, 1, 400,
                         id="test_invalid_last_name_max_length"),
            pytest.param("Alice", None, "AI", "+380999999999",
                         "alice@example.com",
                         "alice#4321", "https://www.linkedin.com/alice", "Los Angeles", True, [1], True, True, 1, 400,
                         id="test_invalid_last_name_null"),
        ]
    )
    def tests_last_name_errors(
            self,
            user_project,
            first_name,
            last_name,
            stack,
            phone_number,
            email,
            account_discord,
            account_linkedin,
            city,
            experience,
            project,
            conditions_participation,
            processing_personal_data,
            type_participant,
            status_code,
            test_id
    ):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "stack": stack,
            "phone_number": phone_number,
            "email": email,
            "account_discord": account_discord,
            "account_linkedin": account_linkedin,
            "experience": experience,
            "city": city,
            "project": project,
            "conditions_participation": conditions_participation,
            "processing_personal_data": processing_personal_data,
            "type_participant": type_participant
        }
        response = user_project.join(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["last_name"][0]).is_equal_to(REGISTRATION_ERRORS[test_id])

    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code", [
            pytest.param("Mike", "Johnson", "U", "+380999999999", "mike@example.com", "mike#9876",
                         "https://www.linkedin.com/mikejohnson", "Chicago", True, [1], True, True, 1, 400,
                         id="test_invalid_stack_min_length"),
            pytest.param("Eve", "Smith", "Development" + "a" * 292, "+380999999999", "eve@example.com", "eve#5678",
                         "https://www.linkedin.com/evesmith", "Seattle", True, [1], True, True, 1, 400,
                         id="test_invalid_stack_max_length"),
            pytest.param("Eve", "Smith", None, "+380999999999", "eve@example.com", "eve#5678",
                         "https://www.linkedin.com/evesmith", "Seattle", True, [1], True, True, 1, 400,
                         id="test_invalid_stack_null"),
        ]
    )
    def tests_stack_errors(
            self,
            user_project,
            first_name,
            last_name,
            stack,
            phone_number,
            email,
            account_discord,
            account_linkedin,
            city,
            experience,
            project,
            conditions_participation,
            processing_personal_data,
            type_participant,
            status_code,
            test_id
    ):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "stack": stack,
            "phone_number": phone_number,
            "email": email,
            "account_discord": account_discord,
            "account_linkedin": account_linkedin,
            "experience": experience,
            "city": city,
            "project": project,
            "conditions_participation": conditions_participation,
            "processing_personal_data": processing_personal_data,
            "type_participant": type_participant
        }
        response = user_project.join(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["stack"][0]).is_equal_to(REGISTRATION_ERRORS[test_id])

    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code", [
            pytest.param("Max", "Smith", "Gaming", "+38099999999", "max@example.com", "max#1234",
                         "https://www.linkedin.com/maxsmith",
                         "Los Angeles", True, [1], True, True, 1, 400,
                         id="test_invalid_phone_number_min_length"),

            pytest.param("Olivia", "Johnson", "Art", "+3809999999996", "olivia@example.com", "olivia#1234",
                         "https://www.linkedin.com/oliviajohnson", "Chicago", True, [1], True, True, 1, 400,
                         id="test_invalid_phone_number_max_length"),
            pytest.param("Olivia", "Johnson", "Art", None, "olivia@example.com", "olivia#1234",
                         "https://www.linkedin.com/oliviajohnson", "Chicago", True, [1], True, True, 1, 400,
                         id="test_invalid_phone_number_null"),
        ]
    )
    def tests_phone_number_errors(
            self,
            user_project,
            first_name,
            last_name,
            stack,
            phone_number,
            email,
            account_discord,
            account_linkedin,
            city,
            experience,
            project,
            conditions_participation,
            processing_personal_data,
            type_participant,
            status_code,
            test_id
    ):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "stack": stack,
            "phone_number": phone_number,
            "email": email,
            "account_discord": account_discord,
            "account_linkedin": account_linkedin,
            "experience": experience,
            "city": city,
            "project": project,
            "conditions_participation": conditions_participation,
            "processing_personal_data": processing_personal_data,
            "type_participant": type_participant
        }
        response = user_project.join(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["phone_number"][0]).is_equal_to(REGISTRATION_ERRORS[test_id])

    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code", [
            pytest.param("Bob", "Johnson", "Data Science", "+380999999999", "bob@example", "bob#9876",
                         "https://www.linkedin.com/bobjohnson", "Chicago", True, [1], True, True, 1, 400,
                         id="test_invalid_email_min_length"),

            pytest.param("Eleanor", "Rigby", "Music", "+380999999999", "eleanor.rigby@example.com" + "a" * 50,
                         "eleanor#5678",
                         "https://www.linkedin.com/eleanorrigby", "Liverpool", True, [1], True, True, 1,
                         400,
                         id="test_invalid_email_max_length"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "davidexample", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, [1], True, True, 1, 400,
                         id="test_invalid_email_format"),
            pytest.param("David", "Smith", "Analytics", "+380999999999", None, "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, [1], True, True, 1, 400,
                         id="test_invalid_email_null"),
        ]
    )
    def tests_email_errors(
            self,
            user_project,
            first_name,
            last_name,
            stack,
            phone_number,
            email,
            account_discord,
            account_linkedin,
            city,
            experience,
            project,
            conditions_participation,
            processing_personal_data,
            type_participant,
            status_code,
            test_id
    ):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "stack": stack,
            "phone_number": phone_number,
            "email": email,
            "account_discord": account_discord,
            "account_linkedin": account_linkedin,
            "experience": experience,
            "city": city,
            "project": project,
            "conditions_participation": conditions_participation,
            "processing_personal_data": processing_personal_data,
            "type_participant": type_participant
        }
        response = user_project.join(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["email"][0]).is_equal_to(REGISTRATION_ERRORS[test_id])

    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code", [
            pytest.param("Sophia", "Smith", "Design", "+380999999999", "sophia@example.com", "s#1111",
                         "https://www.linkedin.com/sophiasmith", "LAD", True, 1, True, True, 1, 400,
                         id="test_invalid_account_discord_min_length"),

            pytest.param("Oliver", "Johnson", "Programming", "+380999999999", "oliver@example.com",
                         "f"*39+"#0000", "https://www.linkedin.com/oliverjohnson", "San Francisco",
                         True, 1, True, True, 1, 400,
                         id="test_invalid_account_discord_max_length"),
            pytest.param("Oliver", "Johnson", "Programming", "+380999999999", "oliver@example.com", None,
                         "https://www.linkedin.com/oliverjohnson", "San Francisco" + "a" * 40, True, 1, True, True,
                         1, 400,
                         id="test_invalid_account_discord_null"),
        ]
    )
    def tests_account_discord_errors(
            self,
            user_project,
            first_name,
            last_name,
            stack,
            phone_number,
            email,
            account_discord,
            account_linkedin,
            city,
            experience,
            project,
            conditions_participation,
            processing_personal_data,
            type_participant,
            status_code,
            test_id
    ):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "stack": stack,
            "phone_number": phone_number,
            "email": email,
            "account_discord": account_discord,
            "account_linkedin": account_linkedin,
            "experience": experience,
            "city": city,
            "project": project,
            "conditions_participation": conditions_participation,
            "processing_personal_data": processing_personal_data,
            "type_participant": type_participant
        }
        response = user_project.join(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["account_discord"][0]).is_equal_to(REGISTRATION_ERRORS[test_id])

    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code", [
            pytest.param("Alex", "Brown", "IT", "+380999999999", "alex@example.com", "alex#5678",
                         "linkedin.com/in/an", "San Francisco", True, 1, True, True, 1,
                         400,
                         id="test_invalid_account_linkedin_min_length"),

            pytest.param("Lucas", "Davis", "Networking", "+380999999999", "lucas@example.com", "lucas#9876",
                         "https://www.linkedin.com/lucasdavis" + "a" * 109, "Chicago", True, 1, True, True, 1,
                         400,
                         id="test_invalid_account_linkedin_max_length"),
            pytest.param("Lucas", "Davis", "Networking", "+380999999999", "lucas@example.com", "lucas#9876",
                         None, "Chicago", True, 1, True, True, 1,
                         400,
                         id="test_invalid_account_linkedin_null"),
        ]
    )
    def tests_account_linkedin_errors(
            self,
            user_project,
            first_name,
            last_name,
            stack,
            phone_number,
            email,
            account_discord,
            account_linkedin,
            city,
            experience,
            project,
            conditions_participation,
            processing_personal_data,
            type_participant,
            status_code,
            test_id
    ):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "stack": stack,
            "phone_number": phone_number,
            "email": email,
            "account_discord": account_discord,
            "account_linkedin": account_linkedin,
            "experience": experience,
            "city": city,
            "project": project,
            "conditions_participation": conditions_participation,
            "processing_personal_data": processing_personal_data,
            "type_participant": type_participant
        }
        response = user_project.join(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["account_linkedin"][0]).is_equal_to(REGISTRATION_ERRORS[test_id])

    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code", [
            pytest.param("Sophia", "Smith", "Design", "+380999999999", "sophia@example.com", "sophia#5678",
                         "https://www.linkedin.com/sophiasmith", "L", True, [1], True, True, 1, 400,
                         id="test_invalid_city_min_length"),

            pytest.param("Oliver", "Johnson", "Programming", "+380999999999", "oliver@example.com", "oliver#1234",
                         "https://www.linkedin.com/oliverjohnson", "San Francisco" + "a" * 40, True, [1], True, True,
                         1, 400,
                         id="test_invalid_city_max_length"),
            pytest.param("Sophia", "Smith", "Design", "+380999999999", "sophia@example.com", "sophia#5678",
                         "https://www.linkedin.com/sophiasmith", None, True, [1], True, True, 1, 400,
                         id="test_invalid_city_null"),

        ]
    )
    def tests_city_errors(
            self,
            user_project,
            first_name,
            last_name,
            stack,
            phone_number,
            email,
            account_discord,
            account_linkedin,
            city,
            experience,
            project,
            conditions_participation,
            processing_personal_data,
            type_participant,
            status_code,
            test_id
    ):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "stack": stack,
            "phone_number": phone_number,
            "email": email,
            "account_discord": account_discord,
            "account_linkedin": account_linkedin,
            "experience": experience,
            "city": city,
            "project": project,
            "conditions_participation": conditions_participation,
            "processing_personal_data": processing_personal_data,
            "type_participant": type_participant
        }
        response = user_project.join(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["city"][0]).is_equal_to(REGISTRATION_ERRORS[test_id])

    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code", [
            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", "invalid_experience", 1, True, True,
                         1,
                         400,
                         id="test_invalid_experience_string"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", None, 1, True, True, 1, 400,
                         id="test_invalid_experience_null"),
        ]
    )
    def tests_experience_errors(
            self,
            user_project,
            first_name,
            last_name,
            stack,
            phone_number,
            email,
            account_discord,
            account_linkedin,
            city,
            experience,
            project,
            conditions_participation,
            processing_personal_data,
            type_participant,
            status_code,
            test_id
    ):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "stack": stack,
            "phone_number": phone_number,
            "email": email,
            "account_discord": account_discord,
            "account_linkedin": account_linkedin,
            "experience": experience,
            "city": city,
            "project": project,
            "conditions_participation": conditions_participation,
            "processing_personal_data": processing_personal_data,
            "type_participant": type_participant
        }
        response = user_project.join(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["experience"][0]).is_equal_to(REGISTRATION_ERRORS[test_id])

    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code", [
            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, [1], True, True, "strstr",
                         400,
                         id="test_invalid_type_participant_string"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, [1], True, True, 1000, 400,
                         id="test_invalid_type_participant_non_allowed_number"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, [1], True, True, None,
                         400,
                         id="test_invalid_type_participant_null"),
        ]
    )
    def tests_type_participant_errors(
            self,
            user_project,
            first_name,
            last_name,
            stack,
            phone_number,
            email,
            account_discord,
            account_linkedin,
            city,
            experience,
            project,
            conditions_participation,
            processing_personal_data,
            type_participant,
            status_code,
            test_id
    ):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "stack": stack,
            "phone_number": phone_number,
            "email": email,
            "account_discord": account_discord,
            "account_linkedin": account_linkedin,
            "experience": experience,
            "city": city,
            "project": project,
            "conditions_participation": conditions_participation,
            "processing_personal_data": processing_personal_data,
            "type_participant": type_participant
        }
        response = user_project.join(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["type_participant"][0]).is_equal_to(REGISTRATION_ERRORS[test_id])

    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code", [
            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, "strstr", True, True, 1, 400,
                         id="test_invalid_project_string"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, [1000], True, True, 1, 400,
                         id="test_invalid_project_non_allowed_number"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, None, True, True, 1, 400,
                         id="test_invalid_project_null"),
        ]
    )
    def tests_project_errors(
            self,
            user_project,
            first_name,
            last_name,
            stack,
            phone_number,
            email,
            account_discord,
            account_linkedin,
            city,
            experience,
            project,
            conditions_participation,
            processing_personal_data,
            type_participant,
            status_code,
            test_id
    ):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "stack": stack,
            "phone_number": phone_number,
            "email": email,
            "account_discord": account_discord,
            "account_linkedin": account_linkedin,
            "experience": experience,
            "city": city,
            "project": project,
            "conditions_participation": conditions_participation,
            "processing_personal_data": processing_personal_data,
            "type_participant": type_participant
        }
        response = user_project.join(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["project"][0]).is_equal_to(REGISTRATION_ERRORS[test_id])

    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code", [
            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, [1], "invalid_conditions", True, 1,
                         400,
                         id="test_invalid_conditions_participation_string"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, [1], None, True, 1, 400,
                         id="test_invalid_conditions_participation_null"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, [1], False, True, 1, 400,
                         id="test_invalid_conditions_participation_false"),
        ]
    )
    def tests_conditions_participation_errors(
            self,
            user_project,
            first_name,
            last_name,
            stack,
            phone_number,
            email,
            account_discord,
            account_linkedin,
            city,
            experience,
            project,
            conditions_participation,
            processing_personal_data,
            type_participant,
            status_code,
            test_id
    ):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "stack": stack,
            "phone_number": phone_number,
            "email": email,
            "account_discord": account_discord,
            "account_linkedin": account_linkedin,
            "experience": experience,
            "city": city,
            "project": project,
            "conditions_participation": conditions_participation,
            "processing_personal_data": processing_personal_data,
            "type_participant": type_participant
        }
        response = user_project.join(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            if "conditions_participation" in response.json():
                error_key = "conditions_participation"
            else:
                error_key = "non_field_errors"
            assert_that(response.json()[error_key][0]).is_equal_to(REGISTRATION_ERRORS[test_id])

    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code", [
            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, [1], True, "invalid_conditions", 1,
                         400,
                         id="test_invalid_processing_personal_data_string"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, [1], True, None, 1, 400,
                         id="test_invalid_processing_personal_data_null"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, [1], True, False, 1, 400,
                         id="test_invalid_processing_personal_data_false"),
        ]
    )
    def tests_processing_personal_data_errors(
            self,
            user_project,
            first_name,
            last_name,
            stack,
            phone_number,
            email,
            account_discord,
            account_linkedin,
            city,
            experience,
            project,
            conditions_participation,
            processing_personal_data,
            type_participant,
            status_code,
            test_id
    ):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "stack": stack,
            "phone_number": phone_number,
            "email": email,
            "account_discord": account_discord,
            "account_linkedin": account_linkedin,
            "experience": experience,
            "city": city,
            "project": project,
            "conditions_participation": conditions_participation,
            "processing_personal_data": processing_personal_data,
            "type_participant": type_participant
        }
        response = user_project.join(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            if "processing_personal_data" in response.json():
                error_key = "processing_personal_data"
            else:
                error_key = "non_field_errors"
            assert_that(response.json()[error_key][0]).is_equal_to(REGISTRATION_ERRORS[test_id])

    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code",
        [
            pytest.param(
                "An", "Doe", "Backend", "+380999999999", "a@example.com",
                "aq#1234", "https://www.linkedin.com/adoe", "New York",
                True, [1], True, True, 1, 201,
                id="test_first_name_min_length",
            ),
            pytest.param(
                "JohnJohJohnJohnJohnJ", "Smith", "Frontend", "+380999999999", "john@example.com",
                "john#5678", "https://www.linkedin.com/johnsmith", "San Francisco",
                True, [1], True, True, 1, 201,
                id="test_first_name_max_length",
            ),
            pytest.param(
                "Jane", "Da", "Full Stack", "+380999999999", "jane@example.com",
                "jane#5678", "https://www.linkedin.com/janed", "San Francisco",
                True, [1], True, True, 1, 201,
                id="test_last_name_min_length",
            ),
            pytest.param(
                "Alice", "t"*19, "AI", "+380999999999",
                "alice@example.com", "alice#4321", "https://www.linkedin.com/alice", "Los Angeles",
                True, [1], True, True, 1, 201,
                id="test_last_name_max_length",
            ),
            pytest.param(
                "Mike", "Johnson", "UI", "+380999999999", "mike@example.com",
                "mike#9876", "https://www.linkedin.com/mikejohnson", "Chicago",
                True, [1], True, True, 1, 201,
                id="test_speciality_min_length",
            ),
            pytest.param(
                "Eve", "Smith", "Data Science" + "a" * 286, "+380999999999", "eve@example.com",
                "eve#5678", "https://www.linkedin.com/evesmith", "Seattle",
                True, [1], True, True, 1, 201,
                id="test_speciality_max_length",
            ),
            pytest.param(
                "Bob", "Johnson", "Data Science", "+380999999999", "bob@gmail.com",
                "bob#9876", "https://www.linkedin.com/bobjohnson", "Chicago",
                True, [1], True, True, 1, 201,
                id="test_email_min_length",
            ),
            pytest.param(
                "Eleanor", "Rigby", "Music", "+380999999999",
                "eleanor.rigby@example.com" + "a" * 45, "eleanor#5678",
                "https://www.linkedin.com/eleanorrigby", "Liverpool",
                True, [1], True, True, 1, 201,
                id="test_email_max_length",
            ),
            pytest.param(
                "Max", "Smith", "Gaming", "+380999999999", "max@example.com",
                "msgg#0000", "https://www.linkedin.com/maxsmith", "Los Angeles",
                True, [1], True, True, 1, 201,
                id="test_discord_min_length",
            ),
            pytest.param(
                "Olivia", "Johnson", "Art", "+380999999999", "olivia@example.com",
                "aaaaaaaaaaaaaaaaaaa#0000", "https://www.linkedin.com/oliviajohnson", "Chicago",
                True, [1], True, True, 1, 201,
                id="test_discord_max_length",
            ),
            pytest.param(
                "Alex", "Brown", "IT", "+380999999999", "alex@example.com",
                "alex#5678", "https://www.linkedin.com/a" + "a" * 10, "San Francisco",
                True, [1], True, True, 1, 201,
                id="test_linkedin_min_length",
            ),
            pytest.param(
                "Lucas", "Davis", "Networking", "+380999999999", "lucas@example.com",
                "lucas#9876", "https://www.linkedin.com/lucasdavis" + "a" * 92, "Chicago",
                True, [1], True, True, 1, 201,
                id="test_linkedin_max_length",
            ),
            pytest.param(
                "Sophia", "Smith", "Design", "+380999999999", "sophia@example.com",
                "sophia#5678", "https://www.linkedin.com/sophiasmith", "LA",
                True, [1], True, True, 1, 201,
                id="test_city_min_length",
            ),
            pytest.param(
                "Oliver", "Johnson", "Programming", "+380999999999", "oliver@example.com",
                "oliver#1234", "https://www.linkedin.com/oliverjohnson", "a" * 50,
                True, [1], True, True, 1, 201,
                id="test_city_max_length",
            ),


        ]
    )
    def test_participant_registration_success(
            self,
            user_project,
            first_name,
            last_name,
            stack,
            phone_number,
            email,
            account_discord,
            account_linkedin,
            city,
            experience,
            project,
            conditions_participation,
            processing_personal_data,
            type_participant,
            status_code,
    ):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "stack": stack,
            "phone_number": phone_number,
            "email": email,
            "account_discord": account_discord,
            "account_linkedin": account_linkedin,
            "experience": experience,
            "city": city,
            "project": project,
            "conditions_participation": conditions_participation,
            "processing_personal_data": processing_personal_data,
            "type_participant": type_participant
        }
        response = user_project.join(data=payload)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
