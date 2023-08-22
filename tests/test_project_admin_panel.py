import json
import pytest
from assertpy import assert_that, soft_assertions


CREATE_PROJECT_ERRORS = {
    "test_invalid_type_project": "Incorrect type. Expected pk value, received str.",
    "test_empty_title": "This field may not be blank.",
    "test_wrong_format_end_date_project": "Date has wrong format. Use one of these formats instead: YYYY-MM-DD.",
    "test_invalid_start_date_format": "Date has wrong format. Use one of these formats instead: YYYY-MM-DD.",
    "test_invalid_end_date_before_start_date": "",
    "test_missing_address_site": "",
}
UPDATE_PROJECT_ERRORS = {
    "": ""
}


class TestProjectAdminPanel:


    @pytest.mark.parametrize(
        "title, comment, type_project, complexity, project_status, start_date_project,"
        "end_date_project, address_site, status_code",
        [
            # Test case 1: Valid project data (system should return 201)
            pytest.param(
                {
                    "title": "New Website Development",  # Title of the project
                    "comment": "This project involves creating a modern and user-friendly website.",
                    "type_project": 1,  # Type of the project (1 for Web Development)
                    "complexity": 2,  # Complexity level (1 for Low, 2 for Medium, 3 for High)
                    "project_status": 1,  # Project status (1 for Active, 2 for Completed, 3 for On Hold)
                    "start_date_project": "2023-08-15",  # Start date of the project
                    "end_date_project": "2023-12-31",  # Expected end date of the project
                    "address_site": "https://www.example.com"  # Website address
                },
                201,
                id="test_valid_project_data"
            )
        ]
    )
    def test_create_project_success(
        self,
        user_project,
        title,
        comment,
        type_project,
        complexity,
        project_status,
        start_date_project,
        end_date_project,
        address_site,
        status_code,
    ):
        payload = {
                "title": title,
                "comment": comment,
                "type_project": type_project,
                "complexity": complexity,
                "project_status": project_status,
                "start_date_project": start_date_project,
                "end_date_project": end_date_project,
                "address_site": address_site,
            }



        response = user_project.create_project(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)

    @pytest.mark.parametrize(
        "title, comment, type_project, complexity, project_status, start_date_project,"
        "end_date_project, address_site, status_code",
        [
            # Test case 1: Invalid type_project (system should return 400)
            pytest.param(
                "Mobile App Development",
                "Creating a mobile app for iOS and Android.",
                "str",  # Invalid type_project value (should be 1, 2, or 3)
                2,
                1,
                "2023-09-01",
                "2023-12-15",
                "https://www.mobileapp.com",
                400,
                id="test_invalid_type_project"
            ),

            # Test case 2: Empty title (system should return 400)
            pytest.param(
                "",
                "No title provided for the project.",
                3,
                1,
                1,
                "2023-08-15",
                "2023-09-30",
                "https://www.example.com",
                400,
                id="test_empty_title"
            ),

            # Test case 3: WRONG end_date_project (system should return 400)
            pytest.param(
                "Data Analysis Project",
                "Analyzing data trends and making recommendations.",
                2,
                2,
                1,
                "2023-07-01",
                False,
                "https://www.dataanalysis.com",
                400,
                id="test_wrong_format_end_date_project"
            ),

            # Test case 4: Invalid start_date_project format (system should return 400)
            pytest.param(
                "Testing Project",
                "Quality assurance testing for a software product.",
                1,
                1,
                1,
                "07-16-2023",  # Invalid date format (should be YYYY-MM-DD)
                "2023-08-31",
                "https://www.testingproject.com",
                400,
                id="test_invalid_start_date_format"
            ),

            # Test case 5: End date before start date (system should return 400)
            pytest.param(
                "Marketing Campaign",
                "Planning and executing a marketing campaign.",
                3,
                2,
                1,
                "2023-09-30",
                "2023-08-15",  # End date before start date
                "https://www.marketingcampaign.com",
                400,
                id="test_end_date_before_start_date"
            ),

            # Test case 6: Missing address_site (system should return 400)
            pytest.param(
                "Research Project",
                "Conducting research on emerging technologies.",
                2,
                3,
                1,
                "2023-10-01",
                "2024-03-31",
                400,
                id="test_missing_address_site"
            )
        ]
    )
    def test_create_project_errors(
        self,
        user_project,
        title,
        comment,
        type_project,
        complexity,
        project_status,
        start_date_project,
        end_date_project,
        address_site,
        status_code,
        test_id
    ):
        payload = {
                "title": title,
                "comment": comment,
                "type_project": type_project,
                "complexity": complexity,
                "project_status": project_status,
                "start_date_project": start_date_project,
                "end_date_project": end_date_project,
                "address_site": address_site,
            }



        response = user_project.create_project(data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["message"]).is_equal_to(CREATE_PROJECT_ERRORS[test_id])

    def get_id_participant(self, participant):
        response = participant
        parsed_response = response.json()
        participant_id = parsed_response.get("id")
        return participant_id

    def get_id_project(self, project):
        response = project
        parsed_response = response.json()
        project_id = parsed_response.get("id")
        return project_id

    def get_url(self, project):
        response = project
        parsed_response = response.json()
        url = parsed_response.get("url")
        return url

    def test_add_participant_to_project(self, user_project, project, participant):

        payload = json.dumps(
            {
                "user": [
                    self.get_id_participant(participant=participant)
                ],
                "project": self.get_id_project(project=project),
            }
        )
        response = user_project.create_command(payload)
        assert response.raise_for_status()

    def test_get_view_project(self, user_project):
        response = user_project.filter_project()
        assert response.raise_for_status()

    def test_get_projects(self, user_project):
        response = user_project.projects_list()
        assert response.raise_for_status()

    #TODO Тут помилка, зробити баг репорт!!
    def test_update_team(self, user_project, project, participant):


        payload = json.dumps(
            {
                "user": [
                    self.get_id_participant(participant=participant)
                ],
                "project": {
                    "title": "string",
                    "start_date_project": "2023-07-18",
                    "complexity": {"complexity": "string"},
                },
            }
        )
        response = user_project.command_update(cmd_id=self.get_id_project(project=project), data=payload)
        assert response.raise_for_status()

    @pytest.mark.parametrize(
        "first_name, last_name, email, project_type, complexity, status, title, comment,"
        " start_date_project, end_date_project, address_site, status_code",
        [
            # Test case 1: Valid project change data (system should return 200)
            pytest.param(
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "john.doe@example.com",
                    "project_type": 2,
                    "complexity": 3,
                    "status": 1,
                    "title": "Updated Research Project",
                    "comment": "Revised research goals and approach.",
                    "start_date_project": "2023-08-15",
                    "end_date_project": "2024-01-31",
                    "address_site": "https://www.updatedresearch.com"
                },
                200,
                id="test_valid_project_change_data"
            ),
        ]
    )
    def test_update_project_success(
        self,
        project,
        user_project,
        first_name,
        last_name,
        email,
        project_type,
        complexity,
        status,
        title,
        comment,
        start_date_project,
        end_date_project,
        address_site,
        status_code,
    ):
        payload = json.dumps(
            {
                "participants": [
                    {"first_name": first_name, "last_name": last_name, "email": email}
                ],
                "type_project": {"project_type": project_type},
                "complexity": {"complexity": complexity},
                "project_status": {"status": status},
                "title": title,
                "comment": comment,
                "start_date_project": start_date_project,
                "end_date_project": end_date_project,
                "address_site": address_site,
            }
        )

        response = user_project.project_update(project_url=self.get_url(project=project), data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)

    @pytest.mark.parametrize(
        "first_name, last_name, email, project_type, complexity, status, title, comment,"
        " start_date_project, end_date_project, address_site, status_code",
        [
            # Test case 2: Invalid project status (system should return 400)
            pytest.param(
                "Alice",
                "Smith",
                "alice.smith@example.com",
                "str",
                2,
                0,
                "Project Update",
                "Making adjustments based on feedback.",
                "2023-09-01",
                "2023-12-15",
                "https://www.projectupdate.com",
                400,
                id="test_invalid_project_status"
            ),

            # Test case 3: Empty title (system should return 400)
            pytest.param(
                "Emily",
                "Johnson",
                "emily.johnson@example.com",
                3,
                1,
                1,
                "",
                "No title provided for the updated project.",
                "2023-08-15",
                "2023-10-31",
                "https://www.updatedproject.com",
                400,
                id="test_empty_title"
            ),

            # Test case 4: Missing email (system should return 400)
            pytest.param(
                "Michael",
                "Brown",
                None,  # Missing email
                2,
                2,
                1,
                "Data Analysis Project",
                "Revised data analysis plan.",
                "2023-07-01",
                "2023-09-30",
                "https://www.dataanalysis.com",
                400,
                id="test_missing_email"
            ),

            # Test case 5: Invalid end_date_project format (system should return 400)
            pytest.param(
                "Sarah",
                "Miller",
                "sarah.miller@example.com",
                1,
                1,
                1,
                "Testing Project Update",
                "Revised testing approach.",
                "2023-08-01",
                "16-07-2023",  # Invalid date format (should be YYYY-MM-DD)
                "https://www.testingprojectupdate.com",
                400,
                id="test_invalid_end_date_format"
            ),

            # Test case 6: End date before start date (system should return 400)
            pytest.param(
                "William",
                "Davis",
                "william.davis@example.com",
                3,
                2,
                1,
                "Marketing Campaign Update",
                "Revised marketing strategy.",
                "2023-10-01",
                "2023-08-15",  # End date before start date
                "https://www.marketingcampaignupdate.com",
                400,
                id="test_end_date_before_start_date"
            ),

            # Test case 7: Missing address_site (system should return 400)
            pytest.param(
                "Daniel",
                "Taylor",
                "daniel.taylor@example.com",
                2,
                3,
                1,
                "Updated Research Project",
                "Revised research goals and approach.",
                "2023-10-01",
                "2024-03-31",
                400,
                id="test_missing_address_site"
            )
        ]
    )
    def test_update_project_errors(
        self,
        project,
        user_project,
        first_name,
        last_name,
        email,
        project_type,
        complexity,
        status,
        title,
        comment,
        start_date_project,
        end_date_project,
        address_site,
        status_code,
        test_id
    ):
        payload = json.dumps(
            {
                "participants": [
                    {"first_name": first_name, "last_name": last_name, "email": email}
                ],
                "type_project": {"project_type": project_type},
                "complexity": {"complexity": complexity},
                "project_status": {"status": status},
                "title": title,
                "comment": comment,
                "start_date_project": start_date_project,
                "end_date_project": end_date_project,
                "address_site": address_site,
            }
        )

        response = user_project.project_update(project_url=self.get_url(project=project), data=payload)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["message"]).is_equal_to(UPDATE_PROJECT_ERRORS[test_id])

    def test_delete_project(self, project, user_project):
        response = user_project.project_delete(project_url=self.get_url(project=project))
        assert response.raise_for_status()
