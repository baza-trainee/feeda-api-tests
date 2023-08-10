import pytest


class TestSearchField:
    #TODO перероби апі потрібно передавати параметр

    @pytest.mark.parametrize("lastname, status_code",
                             pytest.param("Luzina", 200, id="Valid lastname"),
                             pytest.param("invalid", 400, id="Invalid lastname"),
                             pytest.param("invalid2", 400, id="Invalid lastname2"),
                             )
    def test_search_participant_by_lastname(self, user_project, lastname, status_code, participant):
        participant.raise_for_status()
        response = user_project.filter_participant(lastname=lastname)
        assert response.status_code == status_code

    #TODO НАгадати владу зробити цей запит

    @pytest.mark.parametrize("speciality, status_code",
                             pytest.param("QA", 200, id="Valid speciality"),
                             pytest.param("Gamer", 400, id="Invalid speciality"),
                             )
    def test_search_participant_by_speciality(self, user_project, speciality, status_code):
        response = user_project.filter_participant(speciality=speciality)
        assert response.status_code == status_code



    @pytest.mark.parametrize("title, status_code",
                             pytest.param("Feeda", 200, id="Valid title"),
                             pytest.param("Test", 400, id="Invalid title"),
                             )
    def test_search_project_by_title(self, user_project, title, status_code):
        response = user_project.filter_project(title=title)
        assert response.status_code == status_code
