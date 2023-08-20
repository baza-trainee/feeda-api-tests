import pytest


class TestParticipantRegistration:
    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code",
        [
            pytest.param(
                "A", "Doe", "Backend", "+380999999999", "a@example.com",
                "a#1234", "https://www.linkedin.com/adoe", "New York",
                True, [3], True, True, 3, 201,
                id="test_first_name_min_length",
            ),
            pytest.param(
                "JohnJohJohnJohnJohnJ", "Smith", "Frontend", "+380999999999", "john@example.com",
                "john#5678", "https://www.linkedin.com/johnsmith", "San Francisco",
                True, [3], True, True, 3, 201,
                id="test_first_name_max_length",
            ),
            pytest.param(
                "Jane", "D", "Full Stack", "+380999999999", "jane@example.com",
                "jane#5678", "https://www.linkedin.com/janed", "San Francisco",
                True, [3], True, True, 3, 201,
                id="test_last_name_min_length",
            ),
            pytest.param(
                "Alice", "t"*50, "AI", "+380999999999",
                "alice@example.com", "alice#4321", "https://www.linkedin.com/alice", "Los Angeles",
                True, [3], True, True, 3, 201,
                id="test_last_name_max_length",
            ),
            pytest.param(
                "Mike", "Johnson", "UI", "+380999999999", "mike@example.com",
                "mike#9876", "https://www.linkedin.com/mikejohnson", "Chicago",
                True, [3], True, True, 3, 201,
                id="test_speciality_min_length",
            ),
            pytest.param(
                "Eve", "Smith", "Data Science" + "a" * 286, "+380999999999", "eve@example.com",
                "eve#5678", "https://www.linkedin.com/evesmith", "Seattle",
                True, [3], True, True, 3, 201,
                id="test_speciality_max_length",
            ),
            pytest.param(
                "Bob", "Johnson", "Data Science", "+380999999999", "bob@gmail.com",
                "bob#9876", "https://www.linkedin.com/bobjohnson", "Chicago",
                True, [3], True, True, 3, 201,
                id="test_email_min_length",
            ),
            pytest.param(
                "Eleanor", "Rigby", "Music", "+380999999999",
                "eleanor.rigby@example.com" + "a" * 45, "eleanor#5678",
                "https://www.linkedin.com/eleanorrigby", "Liverpool",
                True, [3], True, True, 3, 201,
                id="test_email_max_length",
            ),
            pytest.param(
                "Max", "Smith", "Gaming", "+380999999999", "max@example.com",
                "msgg#0000", "https://www.linkedin.com/maxsmith", "Los Angeles",
                True, [3], True, True, 3, 201,
                id="test_discord_min_length",
            ),
            pytest.param(
                "Olivia", "Johnson", "Art", "+380999999999", "olivia@example.com",
                "aaaaaaaaaaaaaaaaaaa#0000", "https://www.linkedin.com/oliviajohnson", "Chicago",
                True, [3], True, True, 3, 201,
                id="test_discord_max_length",
            ),
            pytest.param(
                "Alex", "Brown", "IT", "+380999999999", "alex@example.com",
                "alex#5678", "https://www.linkedin.com/a" + "a" * 10, "San Francisco",
                True, [3], True, True, 3, 201,
                id="test_linkedin_min_length",
            ),
            pytest.param(
                "Lucas", "Davis", "Networking", "+380999999999", "lucas@example.com",
                "lucas#9876", "https://www.linkedin.com/lucasdavis" + "a" * 92, "Chicago",
                True, [3], True, True, 3, 201,
                id="test_linkedin_max_length",
            ),
            pytest.param(
                "Sophia", "Smith", "Design", "+380999999999", "sophia@example.com",
                "sophia#5678", "https://www.linkedin.com/sophiasmith", "LA",
                True, [3], True, True, 3, 201,
                id="test_city_min_length",
            ),
            pytest.param(
                "Oliver", "Johnson", "Programming", "+380999999999", "oliver@example.com",
                "oliver#1234", "https://www.linkedin.com/oliverjohnson", "a" * 50,
                True, [3], True, True, 3, 201,
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

        assert response.status_code == status_code


    @pytest.mark.parametrize(
        "first_name, last_name, stack, phone_number, email, account_discord, "
        "account_linkedin, city, experience, project, conditions_participation, "
        "processing_personal_data, type_participant, status_code",
        [
            pytest.param("", "", "", "", "", "", "", "", True, 1, True, True, 3, 400,
                         id="test_empty_fields"),

            pytest.param(None, None, None, None, None, None, None, None, True, 1, True, True, "Regular", 400,
                         id="test_request_without_body"),

            pytest.param("A", "Doe", "Backend", "+380999999999", "a@example.com", "a#1234",
                         "https://www.linkedin.com/adoe",
                         "New York",
                         True, 1, True, True, 3, 400,
                         id="test_invalid_first_name_min_length"),

            pytest.param("JohnJohJohnJohnJohnJ", "Smith", "Frontend", "+380999999999", "john@example.com", "john#5678",
                         "https://www.linkedin.com/johnsmith", "San Francisco", True, 1, True, True, 3, 400,
                         id="test_invalid_first_name_max_length"),

            pytest.param("Jane", "D", "Full Stack", "+380999999999", "jane@example.com", "jane#5678",
                         "https://www.linkedin.com/janed",
                         "San Francisco", True, 1, True, True, 3, 400,
                         id="test_invalid_last_name_min_length"),

            pytest.param(
                "Alice", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "AI", "+380999999999",
                "alice@example.com",
                "alice#4321", "https://www.linkedin.com/alice", "Los Angeles", True, 1, True, True, 3, 400,
                id="test_invalid_last_name_max_length"),

            pytest.param("Mike", "Johnson", "U", "+380999999999", "mike@example.com", "mike#9876",
                         "https://www.linkedin.com/mikejohnson", "Chicago", True, 1, True, True, 3, 400,
                         id="test_invalid_stack_min_length"),

            pytest.param("Eve", "Smith", "Development" + "a" * 292, "+380999999999", "eve@example.com", "eve#5678",
                         "https://www.linkedin.com/evesmith", "Seattle", True, 1, True, True, 3, 400,
                         id="test_invalid_stack_max_length"),

            pytest.param("Max", "Smith", "Gaming", "+38099999999", "max@example.com", "ms",
                         "https://www.linkedin.com/maxsmith",
                         "Los Angeles", True, 1, True, True, 3, 400,
                         id="test_invalid_phone_number_min_length"),

            pytest.param("Olivia", "Johnson", "Art", "+3809999999999", "olivia@example.com", "olivia#1234" + "a" * 25,
                         "https://www.linkedin.com/oliviajohnson", "Chicago", True, 1, True, True, 3, 400,
                         id="test_invalid_phone_number_max_length"),

            pytest.param("Bob", "Johnson", "Data Science", "+380999999999", "bob@example", "bob#9876",
                         "https://www.linkedin.com/bobjohnson", "Chicago", True, 1, True, True, 3, 400,
                         id="test_invalid_email_min_length"),

            pytest.param("Eleanor", "Rigby", "Music", "+380999999999", "eleanor.rigby@example.com" + "a" * 50,
                         "eleanor#5678",
                         "https://www.linkedin.com/eleanorrigby", "Liverpool", True, 1, True, True, 3,
                         400,
                         id="test_invalid_email_max_length"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, 1, True, True, 3, 400,
                         id="test_invalid_email_format"),

            pytest.param("Sophia", "Smith", "Design", "+380999999999", "sophia@example.com", "soph",
                         "https://www.linkedin.com/sophiasmith", "LA", True, 1, True, True, 3, 400,
                         id="test_invalid_account_discord_min_length"),

            pytest.param("Oliver", "Johnson", "Programming", "+380999999999", "oliver@example.com", "oliver#1234",
                         "https://www.linkedin.com/oliverjohnson", "San Francisco" + "a" * 40, True, 1, True, True,
                         3, 400,
                         id="test_invalid_account_discord_max_length"),
            pytest.param("Alex", "Brown", "IT", "+380999999999", "alex@example.com", "alex#5678",
                         "https://www.linkedin.com/a" + "a" * 10, "San Francisco", True, 1, True, True, 3,
                         400,
                         id="test_invalid_account_linkedin_min_length"),

            pytest.param("Lucas", "Davis", "Networking", "+380999999999", "lucas@example.com", "lucas#9876",
                         "https://www.linkedin.com/lucasdavis" + "a" * 109, "Chicago", True, 1, True, True, 3,
                         400,
                         id="test_invalid_account_linkedin_max_length"),

            pytest.param("Sophia", "Smith", "Design", "+380999999999", "sophia@example.com", "sophia#5678",
                         "https://www.linkedin.com/sophiasmith", "LA", True, 1, True, True, 3, 400,
                         id="test_invalid_city_min_length"),

            pytest.param("Oliver", "Johnson", "Programming", "+380999999999", "oliver@example.com", "oliver#1234",
                         "https://www.linkedin.com/oliverjohnson", "San Francisco" + "a" * 40, True, 1, True, True,
                         3,
                         400,
                         id="test_invalid_city_max_length"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", "invalid_experience", 1, True, True,
                         3,
                         400,
                         id="test_invalid_experience_string"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", None, 1, True, True, 3, 400,
                         id="test_invalid_experience_null"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, "invalid_type", True, True, 3,
                         400,
                         id="test_invalid_type_participant_string"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, 4, True, True, 3, 400,
                         id="test_invalid_type_participant_non_allowed_number"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, None, True, True, 3,
                         400,
                         id="test_invalid_type_participant_null"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, 1, True, True, "invalid_project",
                         400,
                         id="test_invalid_project_string"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, 1, True, True, 3, 400,
                         id="test_invalid_project_non_allowed_number"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, 1, True, True, None, 400,
                         id="test_invalid_project_null"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, 1, True, True, "invalid_conditions",
                         400,
                         id="test_invalid_conditions_participation_string"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, 1, True, True, None, 400,
                         id="test_invalid_conditions_participation_null"),

            pytest.param("David", "Smith", "Analytics", "+380999999999", "david@example.com", "david#5678",
                         "https://www.linkedin.com/davidsmith", "New York", True, 1, True, True, False, 400,
                         id="test_invalid_conditions_participation_false"),
        ]
    )
    def test_participant_registration_errors(
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
        payload={
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

        assert response.status_code == status_code
        # try:
        #     JoinUserProjectResponse(**response.json())
        # except ValidationError as err:
        #     pytest.fail(f"Response validation failed: {err}")

