import json
import pytest


class TestProjectAdminPanel:
    data = []
    ids = []

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
            ),
            # Test case 2: Invalid type_project (system should return 400)
            pytest.param(
                {
                    "title": "Mobile App Development",
                    "comment": "Creating a mobile app for iOS and Android.",
                    "type_project": 0,  # Invalid type_project value (should be 1, 2, or 3)
                    "complexity": 2,
                    "project_status": 1,
                    "start_date_project": "2023-09-01",
                    "end_date_project": "2023-12-15",
                    "address_site": "https://www.mobileapp.com"
                },
                400,
                id="test_invalid_type_project"
            ),
            # Test case 3: Empty title (system should return 400)
            pytest.param(
                {
                    "title": "",  # Empty title
                    "comment": "No title provided for the project.",
                    "type_project": 3,
                    "complexity": 1,
                    "project_status": 1,
                    "start_date_project": "2023-08-15",
                    "end_date_project": "2023-09-30",
                    "address_site": "https://www.example.com"
                },
                400,
                id="test_empty_title"
            ),
            # Test case 4: Missing end_date_project (system should return 400)
            pytest.param(
                {
                    "title": "Data Analysis Project",
                    "comment": "Analyzing data trends and making recommendations.",
                    "type_project": 2,
                    "complexity": 2,
                    "project_status": 1,
                    "start_date_project": "2023-07-01",
                    "address_site": "https://www.dataanalysis.com"
                },
                400,
                id="test_missing_end_date_project"
            ),
            # Test case 5: Invalid start_date_project format (system should return 400)
            pytest.param(
                {
                    "title": "Testing Project",
                    "comment": "Quality assurance testing for a software product.",
                    "type_project": 1,
                    "complexity": 1,
                    "project_status": 1,
                    "start_date_project": "07-16-2023",  # Invalid date format (should be YYYY-MM-DD)
                    "end_date_project": "2023-08-31",
                    "address_site": "https://www.testingproject.com"
                },
                400,
                id="test_invalid_start_date_format"
            ),
            # Test case 6: End date before start date (system should return 400)
            pytest.param(
                {
                    "title": "Marketing Campaign",
                    "comment": "Planning and executing a marketing campaign.",
                    "type_project": 3,
                    "complexity": 2,
                    "project_status": 1,
                    "start_date_project": "2023-09-30",
                    "end_date_project": "2023-08-15",  # End date before start date
                    "address_site": "https://www.marketingcampaign.com"
                },
                400,
                id="test_end_date_before_start_date"
            ),
            # Test case 7: Missing address_site (system should return 400)
            pytest.param(
                {
                    "title": "Research Project",
                    "comment": "Conducting research on emerging technologies.",
                    "type_project": 2,
                    "complexity": 3,
                    "project_status": 1,
                    "start_date_project": "2023-10-01",
                    "end_date_project": "2024-03-31",
                },
                400,
                id="test_missing_address_site"
            )
        ]
    )
    def test_create_project(
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
        assert response.status_code == status_code

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
            # Test case 2: Invalid project status (system should return 400)
            pytest.param(
                {
                    "first_name": "Alice",
                    "last_name": "Smith",
                    "email": "alice.smith@example.com",
                    "project_type": 1,
                    "complexity": 2,
                    "status": 0,
                    "title": "Project Update",
                    "comment": "Making adjustments based on feedback.",
                    "start_date_project": "2023-09-01",
                    "end_date_project": "2023-12-15",
                    "address_site": "https://www.projectupdate.com"
                },
                400,
                id="test_invalid_project_status"
            ),
            # Test case 3: Empty title (system should return 400)
            pytest.param(
                {
                    "first_name": "Emily",
                    "last_name": "Johnson",
                    "email": "emily.johnson@example.com",
                    "project_type": 3,
                    "complexity": 1,
                    "status": 1,
                    "title": "",
                    "comment": "No title provided for the updated project.",
                    "start_date_project": "2023-08-15",
                    "end_date_project": "2023-10-31",
                    "address_site": "https://www.updatedproject.com"
                },
                400,
                id="test_empty_title"
            ),
            # Test case 4: Missing email (system should return 400)
            pytest.param(
                {
                    "first_name": "Michael",
                    "last_name": "Brown",
                    "project_type": 2,
                    "complexity": 2,
                    "status": 1,
                    "title": "Data Analysis Project",
                    "comment": "Revised data analysis plan.",
                    "start_date_project": "2023-07-01",
                    "end_date_project": "2023-09-30",
                    "address_site": "https://www.dataanalysis.com"
                },
                400,
                id="test_missing_email"
            ),
            # Test case 5: Invalid end_date_project format (system should return 400)
            pytest.param(
                {
                    "first_name": "Sarah",
                    "last_name": "Miller",
                    "email": "sarah.miller@example.com",
                    "project_type": 1,
                    "complexity": 1,
                    "status": 1,
                    "title": "Testing Project Update",
                    "comment": "Revised testing approach.",
                    "start_date_project": "2023-08-01",
                    "end_date_project": "16-07-2023",
                    "address_site": "https://www.testingprojectupdate.com"
                },
                400,
                id="test_invalid_end_date_format"
            ),
            # Test case 6: End date before start date (system should return 400)
            pytest.param(
                {
                    "first_name": "William",
                    "last_name": "Davis",
                    "email": "william.davis@example.com",
                    "project_type": 3,
                    "complexity": 2,
                    "status": 1,
                    "title": "Marketing Campaign Update",
                    "comment": "Revised marketing strategy.",
                    "start_date_project": "2023-10-01",
                    "end_date_project": "2023-08-15",
                    "address_site": "https://www.marketingcampaignupdate.com"
                },
                400,
                id="test_end_date_before_start_date"
            ),
            # Test case 7: Missing address_site (system should return 400)
            pytest.param(
                {
                    "first_name": "Daniel",
                    "last_name": "Taylor",
                    "email": "daniel.taylor@example.com",
                    "project_type": 2,
                    "complexity": 3,
                    "status": 1,
                    "title": "Updated Research Project",
                    "comment": "Revised research goals and approach.",
                    "start_date_project": "2023-10-01",
                    "end_date_project": "2024-03-31",
                },
                400,
                id="test_missing_address_site"
            )
        ]
    )
    def test_update_project(
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
        assert response.status_code == status_code

    def test_delete_project(self, project, user_project):
        response = user_project.project_delete(project_url=self.get_url(project=project))
        assert response.raise_for_status()
