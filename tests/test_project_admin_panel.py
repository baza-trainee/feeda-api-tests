import pytest
from assertpy import assert_that, soft_assertions

CREATE_PROJECT_ERRORS = {
    "test_invalid_type_project": "Incorrect type. Expected pk value, received str.",
    "test_empty_title": "This field may not be blank.",
    "test_wrong_format_end_date_project": "Date has wrong format. Use one of these formats instead: YYYY-MM-DD.",
    "test_invalid_start_date_format": "Date has wrong format. Use one of these formats instead: YYYY-MM-DD.",
    "test_invalid_address_site": "Enter a valid URL.",
}
UPDATE_PROJECT_ERRORS = {
    "test_invalid_project_type_format": "Incorrect type. Expected pk value, received str.",
    "test_invalid_project_type_1000": "Invalid pk \"1000\" - object does not exist.",
    "test_invalid_project_type_null": "This field may not be null.",
    "test_invalid_complexity_format": "Incorrect type. Expected pk value, received str.",
    "test_invalid_complexity_1000": "Invalid pk \"1000\" - object does not exist.",
    "test_invalid_complexity_null": "This field may not be null.",
    "test_invalid_project_status_format": "Incorrect type. Expected pk value, received str.",
    "test_invalid_project_status_1000": "Invalid pk \"1000\" - object does not exist.",
    "test_invalid_project_status_null": "This field may not be null.",
    "test_invalid_title_format": "Not a valid string.",
    "test_invalid_title_empty": "This field may not be blank.",
    "test_invalid_title_maxLength+1": "Ensure this field has no more than 30 characters.",
    "test_invalid_title_null": "This field may not be null.",
    "test_invalid_comment_format": "Not a valid string.",
    "test_invalid_comment_maxLength+1": "Ensure this field has no more than 50 characters.",
    "test_invalid_start_date_project_dateformat": "Date has wrong format. Use one of these formats instead: YYYY-MM-DD.",
    "test_invalid_start_date_project_empty": "Date has wrong format. Use one of these formats instead: YYYY-MM-DD.",
    "test_invalid_start_date_project_null": "This field may not be null.",
    "test_invalid_end_date_project_dateformat": "Date has wrong format. Use one of these formats instead: YYYY-MM-DD.",
    "test_invalid_end_date_project_empty": "Date has wrong format. Use one of these formats instead: YYYY-MM-DD.",
    "test_invalid_address_site_format": "Enter a valid URL.",
}


class TestProjectAdminPanel:
    @pytest.mark.parametrize(
        "title, comment, type_project, complexity, project_status, start_date_project,"
        "end_date_project, address_site, status_code",
        [
            # Test case 3: Empty title (system should return 400)
            pytest.param(
                    "",
                    "No title provided for the project.",
                    1,
                    1,
                    1,
                    "2023-08-15",
                    "2023-09-30",
                    "https://www.example.com",
                    400,
                    id="test_empty_title",
            ),

        ],
    )
    def test_create_project_title_errors(
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
            assert_that(response.json()["title"][0]).is_equal_to(CREATE_PROJECT_ERRORS[test_id])

    @pytest.mark.parametrize(
        "title, comment, type_project, complexity, project_status, start_date_project,"
        "end_date_project, address_site, status_code",
        [
            # Test case 2: Invalid type_project (system should return 400)
            pytest.param(
                    "Mobile App Development",
                    "Creating a mobile app for iOS and Android.",
                    "strstr",  # Invalid type_project value (should be 1, 2, or 3)
                    2,
                    1,
                    "2023-09-01",
                    "2023-12-15",
                    "https://www.mobileapp.com",
                    400,
                    id="test_invalid_type_project",
            ),

        ],
    )
    def test_create_project_type_project_errors(
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
            assert_that(response.json()["type_project"][0]).is_equal_to(CREATE_PROJECT_ERRORS[test_id])

    @pytest.mark.parametrize(
        "title, comment, type_project, complexity, project_status, start_date_project,"
        "end_date_project, address_site, status_code",
        [
            pytest.param(
                "Mobile App Development",
                "Creating a mobile app for iOS and Android.",
                1,
                2,
                1,
                "01-09-2023",
                "2023-12-15",
                "https://www.mobileapp.com",
                400,
                id="test_invalid_start_date_format",
            ),

        ],
    )
    def test_create_project_start_date_project_errors(
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
            assert_that(response.json()["start_date_project"][0]).is_equal_to(CREATE_PROJECT_ERRORS[test_id])

    @pytest.mark.parametrize(
        "title, comment, type_project, complexity, project_status, start_date_project,"
        "end_date_project, address_site, status_code",
        [
            pytest.param(
                "Mobile App Development",
                "Creating a mobile app for iOS and Android.",
                1,
                2,
                1,
                "2023-08-15",
                "15-12-2023",
                "https://www.mobileapp.com",
                400,
                id="test_wrong_format_end_date_project",
            ),

        ],
    )
    def test_create_project_end_date_project_errors(
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
            assert_that(response.json()["end_date_project"][0]).is_equal_to(CREATE_PROJECT_ERRORS[test_id])

    @pytest.mark.parametrize(
        "title, comment, type_project, complexity, project_status, start_date_project,"
        "end_date_project, address_site, status_code",
        [
            pytest.param(
                "Mobile App Development",
                "Creating a mobile app for iOS and Android.",
                1,
                2,
                1,
                "2023-08-15",
                "2023-10-15",
                "mobileapp.c",
                400,
                id="test_invalid_address_site",
            ),

        ],
    )
    def test_create_project_address_site_errors(
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
            assert_that(response.json()["address_site"][0]).is_equal_to(CREATE_PROJECT_ERRORS[test_id])

    @pytest.mark.parametrize(
        "title, comment, type_project, complexity, project_status, start_date_project,"
        "end_date_project, address_site, status_code",
        [
            # Test case 1: Valid project data (system should return 201)
            pytest.param(
                "New Website Development",  # Title of the project
                "This project involves creating a modern website.",
                1,  # Type of the project (1 for Web Development)
                2,  # Complexity level (1 for Low, 2 for Medium, 3 for High)
                1,  # Project status (1 for Active, 2 for Completed, 3 for On Hold)
                "2023-08-15",  # Start date of the project
                "2023-12-31",  # Expected end date of the project
                "https://www.example.com",  # Website address
                201,
                id="test_valid_project_data",
            ),

        ],
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

    # def test_add_participant_to_project(self, user_project, project, participant):
    #     payload = json.dumps(
    #         {
    #             "user": [self.get_id_participant(participant=participant)],
    #             "project": self.get_id_project(project=project),
    #         }
    #     )
    #     response = user_project.create_command(payload)
    #     assert response.raise_for_status()

    def test_get_view_project(self, user_project):
        response = user_project.filter_project()
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)

    def test_get_projects(self, user_project):
        response = user_project.projects_list()
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)

    # #TODO Тут помилка, зробити баг репорт!!
    # def test_update_team(self, user_project, project, participant):
    #     payload = json.dumps(
    #         {
    #             "user": [self.get_id_participant(participant=participant)],
    #             "project": {
    #                 "title": "string",
    #                 "start_date_project": "2023-07-18",
    #                 "complexity": {"complexity": "string"},
    #             },
    #         }
    #     )
    #     response = user_project.command_update(
    #         cmd_id=self.get_id_project(project=project), data=payload
    #     )
    #     assert response.raise_for_status()
    @pytest.mark.parametrize(
        "project_type, complexity, status, title, comment, start_date_project, end_date_project,"
        " address_site, status_code",
        [
            pytest.param("strstr", 1, 1, "feeda1", "hr app", "2003-07-16", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_project_type_format"),
            pytest.param(1000, 1, 1, "feeda1", "hr app", "2003-07-16", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_project_type_1000"),
            pytest.param(None, 1, 1, "feeda1", "hr app", "2003-07-16", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_project_type_null"),
        ]
    )
    def test_update_project_project_type_errors(
        self,
        project,
        user_project,
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
        payload = {
                "type_project": project_type,
                "complexity": complexity,
                "project_status":  status,
                "title": title,
                "comment": comment,
                "start_date_project": start_date_project,
                "end_date_project": end_date_project,
                "address_site": address_site,
                "url": self.get_url(project=project)
            }
        response = user_project.project_update(
            project_url=self.get_url(project=project), data=payload
        )
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["type_project"][0]).is_equal_to(UPDATE_PROJECT_ERRORS[test_id])

    @pytest.mark.parametrize(
        "project_type, complexity, status, title, comment, start_date_project, end_date_project,"
        " address_site, status_code",
        [
            pytest.param(1, "strstr", 1, "feeda1", "hr app", "2003-07-16", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_complexity_format"),
            pytest.param(1, 1000, 1, "feeda1", "hr app", "2003-07-16", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_complexity_1000"),
            pytest.param(1, None, 1, "feeda1", "hr app", "2003-07-16", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_complexity_null"),
        ]
    )
    def test_update_project_complexity_errors(
            self,
            project,
            user_project,
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
        payload = {
            "type_project": project_type,
            "complexity": complexity,
            "project_status": status,
            "title": title,
            "comment": comment,
            "start_date_project": start_date_project,
            "end_date_project": end_date_project,
            "address_site": address_site,
            "url": self.get_url(project=project)
        }
        response = user_project.project_update(
            project_url=self.get_url(project=project), data=payload
        )
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["complexity"][0]).is_equal_to(UPDATE_PROJECT_ERRORS[test_id])

    @pytest.mark.parametrize(
        "project_type, complexity, status, title, comment, start_date_project, end_date_project,"
        " address_site, status_code",
        [
            pytest.param(1, 1, "strstr", "feeda1", "hr app", "2003-07-16", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_project_status_format"),
            pytest.param(1, 1, 1000, "feeda1", "hr app", "2003-07-16", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_project_status_1000"),
            pytest.param(1, 1, None, "feeda1", "hr app", "2003-07-16", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_project_status_null"),
        ]
    )
    def test_update_project_project_status_errors(
            self,
            project,
            user_project,
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
        payload = {
            "type_project": project_type,
            "complexity": complexity,
            "project_status": status,
            "title": title,
            "comment": comment,
            "start_date_project": start_date_project,
            "end_date_project": end_date_project,
            "address_site": address_site,
            "url": self.get_url(project=project)
        }
        response = user_project.project_update(
            project_url=self.get_url(project=project), data=payload
        )
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["project_status"][0]).is_equal_to(UPDATE_PROJECT_ERRORS[test_id])

    @pytest.mark.parametrize(
        "project_type, complexity, status, title, comment, start_date_project, end_date_project,"
        " address_site, status_code",
        [
            pytest.param(1, 1, 1, False, "hr app", "2003-07-16", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_title_format"),
            pytest.param(1, 1, 1, "", "hr app", "2003-07-16", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_title_empty"),
            pytest.param(1, 1, 1, "t"*31, "hr app", "2003-07-16", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_title_maxLength+1"),
            pytest.param(1, 1, 1, None, "hr app", "2003-07-16", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_title_null"),
        ]
    )
    def test_update_project_title_errors(
            self,
            project,
            user_project,
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
        payload = {
            "type_project": project_type,
            "complexity": complexity,
            "project_status": status,
            "title": title,
            "comment": comment,
            "start_date_project": start_date_project,
            "end_date_project": end_date_project,
            "address_site": address_site,
            "url": self.get_url(project=project)
        }
        response = user_project.project_update(
            project_url=self.get_url(project=project), data=payload
        )
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["title"][0]).is_equal_to(UPDATE_PROJECT_ERRORS[test_id])

    @pytest.mark.parametrize(
        "project_type, complexity, status, title, comment, start_date_project, end_date_project,"
        " address_site, status_code",
        [
            pytest.param(1, 1, 1, "feeda1", False, "2003-07-16", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_comment_format"),
            pytest.param(1, 1, 1, "feeda1", "t"*51, "2003-07-16", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_comment_maxLength+1"),

        ]
    )
    def test_update_project_comment_errors(
            self,
            project,
            user_project,
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
        payload = {
            "type_project": project_type,
            "complexity": complexity,
            "project_status": status,
            "title": title,
            "comment": comment,
            "start_date_project": start_date_project,
            "end_date_project": end_date_project,
            "address_site": address_site,
            "url": self.get_url(project=project)
        }
        response = user_project.project_update(
            project_url=self.get_url(project=project), data=payload
        )
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["comment"][0]).is_equal_to(UPDATE_PROJECT_ERRORS[test_id])

    @pytest.mark.parametrize(
        "project_type, complexity, status, title, comment, start_date_project, end_date_project,"
        " address_site, status_code",
        [
            pytest.param(1, 1, 1, "feeda1", "hr app", "16-07-2003", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_start_date_project_dateformat"),
            pytest.param(1, 1, 1, "feeda1", "hr app", "", "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_start_date_project_empty"),
            pytest.param(1, 1, 1, "feeda1", "hr app", None, "2003-07-19", "https://www.google.com/", 400,
                         id="test_invalid_title_null"),
        ]
    )
    def test_update_project_start_date_project_errors(
            self,
            project,
            user_project,
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
        payload = {
            "type_project": project_type,
            "complexity": complexity,
            "project_status": status,
            "title": title,
            "comment": comment,
            "start_date_project": start_date_project,
            "end_date_project": end_date_project,
            "address_site": address_site,
            "url": self.get_url(project=project)
        }
        response = user_project.project_update(
            project_url=self.get_url(project=project), data=payload
        )
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["start_date_project"][0]).is_equal_to(UPDATE_PROJECT_ERRORS[test_id])

    @pytest.mark.parametrize(
        "project_type, complexity, status, title, comment, start_date_project, end_date_project,"
        " address_site, status_code",
        [
            pytest.param(1, 1, 1, "feeda1", "hr app", "2003-07-13", "19-07-2003", "https://www.google.com/", 400,
                         id="test_invalid_start_date_project_dateformat"),
            pytest.param(1, 1, 1, "feeda1", "hr app", "2003-07-13", "", "https://www.google.com/", 400,
                         id="test_invalid_start_date_project_empty"),
        ]
    )
    def test_update_project_end_date_project_errors(
            self,
            project,
            user_project,
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
        payload = {
            "type_project": project_type,
            "complexity": complexity,
            "project_status": status,
            "title": title,
            "comment": comment,
            "start_date_project": start_date_project,
            "end_date_project": end_date_project,
            "address_site": address_site,
            "url": self.get_url(project=project)
        }
        response = user_project.project_update(
            project_url=self.get_url(project=project), data=payload
        )
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["end_date_project"][0]).is_equal_to(UPDATE_PROJECT_ERRORS[test_id])

    @pytest.mark.parametrize(
        "project_type, complexity, status, title, comment, start_date_project, end_date_project,"
        " address_site, status_code",
        [
            pytest.param(1, 1, 1, "feeda1", "hr app", "2003-07-16", "2003-07-19", "text", 400,
                         id="test_invalid_address_site_format"),
        ]
    )
    def test_update_project_address_site_errors(
            self,
            project,
            user_project,
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
        payload = {
            "type_project": project_type,
            "complexity": complexity,
            "project_status": status,
            "title": title,
            "comment": comment,
            "start_date_project": start_date_project,
            "end_date_project": end_date_project,
            "address_site": address_site,
            "url": self.get_url(project=project)
        }
        response = user_project.project_update(
            project_url=self.get_url(project=project), data=payload
        )
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.json()["address_site"][0]).is_equal_to(UPDATE_PROJECT_ERRORS[test_id])

    def test_delete_project(self, project, user_project):
        response = user_project.project_delete(
            project_url=self.get_url(project=project)
        )
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
