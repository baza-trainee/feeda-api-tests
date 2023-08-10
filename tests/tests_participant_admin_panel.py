import pytest
import json


class TestParticipantsPageOfTheAdminPanel:

    @pytest.mark.parametrize("first_name, last_name, speciality, phone_number, email, comment, account_discord,"
                             " account_linkedin, city, experience, project, stack, status_code_for_create", [
                                 # Test case 1: Invalid first_name (minlength - 1)
                                 pytest.param("A", "Doe", 1, "+380999999999", "a@example.com", "Comment", "a#1234",
                                              "https://www.linkedin.com/adoe",
                                              "New York", True, 1, "Regular", 400,
                                              id="test_invalid_first_name_min_length"),
                                 # Test case 2: Invalid first_name (maxlength + 1)
                                 pytest.param("JohnJohJohnJohnJohnJ", "Smith", 1, "+380999999999", "john@example.com",
                                              "Comment", "john#5678",
                                              "https://www.linkedin.com/johnsmith", "San Francisco", True, 1, "VIP",
                                              400,
                                              id="test_invalid_first_name_max_length"),
                                 # Test case 3: Invalid first_name (NULL)
                                 pytest.param(None, "Doe", 1, "+380999999999", "a@example.com", "Comment", "a#1234",
                                              "https://www.linkedin.com/adoe",
                                              "New York", True, 1, "Regular", 400,
                                              id="test_invalid_first_name_null"),
                                 # Test case 4: Invalid last_name (minlength - 1)
                                 pytest.param("Jane", "D", 1, "+380999999999", "jane@example.com", "Comment",
                                              "jane#5678",
                                              "https://www.linkedin.com/janed",
                                              "San Francisco", True, 1, "Regular", 400,
                                              id="test_invalid_last_name_min_length"),
                                 # Test case 5: Invalid last_name (maxlength + 1)
                                 pytest.param("Alice", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", 1,
                                              "+380999999999",
                                              "alice@example.com",
                                              "Comment", "alice#4321", "https://www.linkedin.com/alice", "Los Angeles",
                                              True, 1, "Regular", 400,
                                              id="test_invalid_last_name_max_length"),
                                 # Test case 6: Invalid last_name (NULL)
                                 pytest.param("John", None, 1, "+380999999999", "john@example.com", "Comment",
                                              "john#5678",
                                              "https://www.linkedin.com/johnsmith", "San Francisco", True, 1, "Regular",
                                              400,
                                              id="test_invalid_last_name_null"),
                                 # Test case 7: Invalid speciality (NULL)
                                 pytest.param("Mike", "Johnson", None, "+380999999999", "mike@example.com", "Comment",
                                              "mike#9876",
                                              "https://www.linkedin.com/mikejohnson", "Chicago", True, 1, "Regular",
                                              400,
                                              id="test_invalid_speciality_null"),
                                 # Test case 8: Invalid phone_number (minlength - 1)
                                 pytest.param("Max", "Smith", 1, "+38099999999", "max@example.com", "Comment", "ms",
                                              "https://www.linkedin.com/maxsmith",
                                              "Los Angeles", True, 1, "Regular", 400,
                                              id="test_invalid_phone_number_min_length"),
                                 # Test case 9: Invalid phone_number (maxlength + 1)
                                 pytest.param("Olivia", "Johnson", 1, "+3809999999999", "olivia@example.com", "Comment",
                                              "olivia#1234" + "a" * 25,
                                              "https://www.linkedin.com/oliviajohnson", "Chicago", True, 1, "Regular",
                                              400,
                                              id="test_invalid_phone_number_max_length"),
                                 # Test case 10: Invalid phone_number (NULL)
                                 pytest.param("Oliver", "Johnson", 1, None, "oliver@example.com", "Comment",
                                              "oliver#1234",
                                              "https://www.linkedin.com/oliverjohnson", "San Francisco", True, 1,
                                              "Regular", 400,
                                              id="test_invalid_phone_number_null"),
                                 # Test case 11: Invalid email (minlength - 1)
                                 pytest.param("Bob", "Johnson", 1, "+380999999999", "bob@example", "Comment",
                                              "bob#9876",
                                              "https://www.linkedin.com/bobjohnson", "Chicago", True, 1, "Regular", 400,
                                              id="test_invalid_email_min_length"),
                                 # Test case 12: Invalid email (maxlength + 1)
                                 pytest.param("Eleanor", "Rigby", 1, "+380999999999",
                                              "eleanor.rigby@example.com" + "a" * 50, "Comment",
                                              "eleanor#5678",
                                              "https://www.linkedin.com/eleanorrigby", "Liverpool", True, 1, "Regular",
                                              400,
                                              id="test_invalid_email_max_length"),
                                 # Test case 13: Invalid email (NULL)
                                 pytest.param("David", "Smith", 1, "+380999999999", None, "Comment", "david#5678",
                                              "https://www.linkedin.com/davidsmith", "New York", True, 1, "Regular",
                                              400,
                                              id="test_invalid_email_null"),
                                 # Test case 14: Invalid email (invalid format)
                                 pytest.param("David", "Smith", 1, "+380999999999", "david@example", "Comment",
                                              "david#5678",
                                              "https://www.linkedin.com/davidsmith", "New York", True, 1, "Regular",
                                              400,
                                              id="test_invalid_email_format"),
                                 # Test case 15: Invalid discord (minlength - 1)
                                 pytest.param("Sophia", "Smith", 1, "+380999999999", "sophia@example.com", "Comment",
                                              "soph",
                                              "https://www.linkedin.com/sophiasmith", "LA", True, 1, "Regular", 400,
                                              id="test_invalid_discord_min_length"),
                                 # Test case 16: Invalid discord (maxlength + 1)
                                 pytest.param("Oliver", "Johnson", 1, "+380999999999", "oliver@example.com", "Comment",
                                              "oliver#1234",
                                              "https://www.linkedin.com/oliverjohnson", "San Francisco" + "a" * 40,
                                              True, 1, "Regular", 400,
                                              id="test_invalid_discord_max_length"),
                                 # Test case 17: Invalid discord (NULL)
                                 pytest.param("Alex", "Brown", 1, "+380999999999", "alex@example.com", "Comment",
                                              "alex#5678",
                                              "https://www.linkedin.com/a" + "a" * 10, "San Francisco", True, 1,
                                              "Regular", 400,
                                              id="test_invalid_discord_null"),
                                 # Test case 18: Invalid city (minlength - 1)
                                 pytest.param("Sophia", "Smith", 1, "+380999999999", "sophia@example.com", "Comment",
                                              "sophia#5678",
                                              "https://www.linkedin.com/sophiasmith", "LA", True, 1, "Regular", 400,
                                              id="test_invalid_city_min_length"),
                                 # Test case 19: Invalid city (maxlength + 1)
                                 pytest.param("Oliver", "Johnson", 1, "+380999999999", "oliver@example.com", "Comment",
                                              "oliver#1234",
                                              "https://www.linkedin.com/oliverjohnson", "San Francisco" + "a" * 40,
                                              True, 1, "Regular", 400,
                                              id="test_invalid_city_max_length"),
                                 # Test case 20: Invalid city (NULL)
                                 pytest.param("Alex", "Brown", 1, "+380999999999", "alex@example.com", "Comment",
                                              "alex#5678",
                                              "https://www.linkedin.com/a" + "a" * 10, None, True, 1, "Regular", 400,
                                              id="test_invalid_city_null"),
                                 # Test case 21: Invalid experience (NULL)
                                 pytest.param("David", "Smith", 1, "+380999999999", "david@example.com", "Comment",
                                              "david#5678",
                                              "https://www.linkedin.com/davidsmith", "New York", True, None, "Regular",
                                              400,
                                              id="test_invalid_experience_null"),
                                 # Test case 22: Invalid stack (minlength - 1)
                                 pytest.param("David", "Smith", 1, "+380999999999", "david@example.com", "Comment",
                                              "david#5678",
                                              "https://www.linkedin.com/davidsmith", "New York", True, 1, "Regular",
                                              400,
                                              id="test_invalid_stack_min_length"),
                                 # Test case 23: Invalid stack (maxlength + 1)
                                 pytest.param("Lucas", "Davis", 1, "+380999999999", "lucas@example.com", "Comment",
                                              "lucas#9876",
                                              "https://www.linkedin.com/lucasdavis" + "a" * 109, "Chicago", True, 1,
                                              "Regular", 400,
                                              id="test_invalid_stack_max_length"),
                                 # Test case 24: Invalid stack (NULL)
                                 pytest.param("Lucas", "Davis", 1, "+380999999999", "lucas@example.com", "Comment",
                                              "lucas#9876",
                                              "https://www.linkedin.com/lucasdavis", "Chicago", True, 1, None, 400,
                                              id="test_invalid_stack_null"),
                                 # Test case 25: Adding participant to non-existent project
                                 pytest.param("David", "Smith", 1, "+380999999999", "david@example.com", "Comment",
                                              "david#5678",
                                              "https://www.linkedin.com/davidsmith", "New York", True, 1, "Regular",
                                              400,
                                              id="test_adding_to_nonexistent_project"),
                             ]
                             )
    def test_create_participant(
            self,
            user_project,
            first_name,
            last_name,
            speciality,
            phone_number,
            email,
            comment,
            account_discord,
            account_linkedin,
            city,
            experience,
            project,
            stack,
            status_code_for_create,
    ):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "speciality": speciality,
            "phone_number": phone_number,
            "email": email,
            "comment": comment,
            "account_discord": account_discord,
            "account_linkedin": account_linkedin,
            "city": city,
            "experience": experience,
            "project": project,
            "stack": stack
        }
        response = user_project.add_participant(payload)
        assert response.status_code == status_code_for_create



    def get_id_participant(self, participant):
        response = participant
        parsed_response = response.json()
        participant_id = parsed_response.get("id")
        return participant_id

    @pytest.mark.parametrize(
        "first_name, last_name, speciality, phone_number, email, comment, account_discord, account_linkedin, city,"
        " experience, project, stack, status_code",
         [
             pytest.param(
                 "Anna",
                 "Luzina",
                 1,
                 "+380999999999",
                 "testing@gmail.com",
                 "Valid comment",
                 "anastasiia#1234",
                 "https://www.linkedin.com/in/anastasiia",
                 "city",
                 True,
                 1,
                 "QA Manual",
                 201,
                 id="test_change_valid_id"
             ),
             # Test case 2: Change valid last_name (system should return 201)
             pytest.param(
                 "Anna",
                 "Luzina",
                 1,
                 "+380999999999",
                 "testing@gmail.com",
                 "Valid comment",
                 "anastasiia#1234",
                 "https://www.linkedin.com/in/anastasiia",
                 "city",
                 True,
                 1,
                 "QA Manual",
                 201,
                 id="test_change_valid_last_name"
             ),
             # Test case 3: Change valid role (system should return 201)
             pytest.param(
                 "Anna",
                 "Luzina",
                 1,
                 "+380999999999",
                 "testing@gmail.com",
                 "Valid comment",
                 "anastasiia#1234",
                 "https://www.linkedin.com/in/anastasiia",
                 "city",
                 True,
                 1,
                 "QA Manual",
                 201,
                 id="test_change_valid_role"
             ),
             # Test case 4: Change valid phone_number (system should return 201)
             pytest.param(
                 "Anna",
                 "Luzina",
                 1,
                 "+380999999999",
                 "testing@gmail.com",
                 "Valid comment",
                 "anastasiia#1234",
                 "https://www.linkedin.com/in/anastasiia",
                 "city",
                 True,
                 1,
                 "QA Manual",
                 201,
                 id="test_change_valid_phone_number"
             ),
             # Test case 5: Change valid email (system should return 201)
             pytest.param(
                 "Anna",
                 "Luzina",
                 1,
                 "+380999999999",
                 "testing@gmail.com",
                 "Valid comment",
                 "anastasiia#1234",
                 "https://www.linkedin.com/in/anastasiia",
                 "city",
                 True,
                 1,
                 "QA Manual",
                 201,
                 id="test_change_valid_email"
             ),
             # Test case 6: Change valid comment (system should return 201)
             pytest.param(
                 "Anna",
                 "Luzina",
                 1,
                 "+380999999999",
                 "testing@gmail.com",
                 "Valid comment",
                 "anastasiia#1234",
                 "https://www.linkedin.com/in/anastasiia",
                 "city",
                 True,
                 1,
                 "QA Manual",
                 201,
                 id="test_change_valid_comment"
             ),
             # Test case 7: Change valid account in discord (system should return 201)
             pytest.param(
                 "Anna",
                 "Luzina",
                 1,
                 "+380999999999",
                 "testing@gmail.com",
                 "Valid comment",
                 "anastasiia#1234",
                 "https://www.linkedin.com/in/anastasiia",
                 "city",
                 True,
                 1,
                 "QA Manual",
                 201,
                 id="test_change_valid_discord"
             ),
             # Test case 8: Change valid account in LinkedIn (system should return 201)
             pytest.param(
                 "Anna",
                 "Luzina",
                 1,
                 "+380999999999",
                 "testing@gmail.com",
                 "Valid comment",
                 "anastasiia#1234",
                 "https://www.linkedin.com/in/anastasiia",
                 "city",
                 True,
                 1,
                 "QA Manual",
                 201,
                 id="test_change_valid_linkedin"
             ),
             # Test case 9: Change valid city (system should return 201)
             pytest.param(
                 "Anna",
                 "Luzina",
                 1,
                 "+380999999999",
                 "testing@gmail.com",
                 "Valid comment",
                 "anastasiia#1234",
                 "https://www.linkedin.com/in/anastasiia",
                 "city",
                 True,
                 1,
                 "QA Manual",
                 201,
                 id="test_change_valid_city"
             ),
             # Test case 10: Change valid experience (system should return 201)
             pytest.param(
                 "Anna",
                 "Luzina",
                 1,
                 "+380999999999",
                 "testing@gmail.com",
                 "Valid comment",
                 "anastasiia#1234",
                 "https://www.linkedin.com/in/anastasiia",
                 "city",
                 True,
                 1,
                 "QA Manual",
                 201,
                 id="test_change_valid_experience"
             ),
             # Test case 11: Change valid project (system should return 201)
             pytest.param(
                 "Anna",
                 "Luzina",
                 1,
                 "+380999999999",
                 "testing@gmail.com",
                 "Valid comment",
                 "anastasiia#1234",
                 "https://www.linkedin.com/in/anastasiia",
                 "city",
                 True,
                 1,
                 "QA Manual",
                 201,
                 id="test_change_valid_project"
             ),
             # Test case 12: Change valid stack (system should return 201)
             pytest.param(
                 "Anna",
                 "Luzina",
                 1,
                 "+380999999999",
                 "testing@gmail.com",
                 "Valid comment",
                 "anastasiia#1234",
                 "https://www.linkedin.com/in/anastasiia",
                 "city",
                 True,
                 1,
                 "QA Manual",
                 201,
                 id="test_change_valid_stack"
             ),
         ]
    )
    def test_update_participant(
        self,
        user_project,
        create_participant,
        first_name,
        last_name,
        speciality,
        phone_number,
        email,
        comment,
        account_discord,
        account_linkedin,
        city,
        experience,
        project,
        stack,
        status_code,
    ):
        participant_id = self.get_id_participant(create_participant)
        payload = json.dumps(
            {
                "first_name": first_name,
                "last_name": last_name,
                "speciality": speciality,
                "phone_number": phone_number,
                "email": email,
                "comment": comment,
                "account_discord": account_discord,
                "account_linkedin": account_linkedin,
                "city": city,
                "experience": experience,
                "project": project,
                "stack": stack,
            }
        )

        response = user_project.update_participant(participant_id=participant_id, data=payload)
        assert response.status_code == status_code

    def test_get_participant_by_id(self, user_project, participant):
        participant_id = self.get_id_participant(participant)
        response = user_project.get_participant(participant_id=participant_id)
        response.raise_for_status()

    def test_get_all_participant(self, user_project):
        response = user_project.get_participants_list()
        response.raise_for_status()

    def test_delete(self, user_project, create_participant):
        participant_id = self.get_id_participant(create_participant)
        response_delete = user_project.delete_participant(participant_id=participant_id)
        response_delete.raise_for_status()
