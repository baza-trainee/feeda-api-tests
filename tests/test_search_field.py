import pytest
from assertpy import assert_that, soft_assertions


class TestSearchField:
    @pytest.mark.parametrize(
        "lastname, status_code", [
            pytest.param("Luzina", 200, id="Valid lastname"),
            pytest.param("luzina", 200, id="Valid lowercase lastname"),
            pytest.param("Luz", 200, id="Valid lastname with a capital letter"),
        ]
    )
    def test_search_participant_by_lastname_success(self, user_project, lastname, status_code, participant):
        participant.raise_for_status()
        response = user_project.search_participant(param=lastname)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.text).contains('Anastasia')



    @pytest.mark.parametrize(
        "stack, status_code", [
            pytest.param("QA Manual, Postman", 200, id="Valid lastname"),
            pytest.param("QA", 200, id="Valid lowercase lastname"),
            pytest.param("postm", 200, id="Valid lastname with a capital letter"),
        ]
    )
    def test_search_participant_by_stack_success(self, user_project, stack, status_code, participant):
        participant.raise_for_status()
        response = user_project.search_participant(param=stack)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(status_code)
            assert_that(response.text).contains('Luzina')
