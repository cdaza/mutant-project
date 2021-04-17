import pytest
from manage import app


@pytest.fixture
def client():
    app.config.from_object('app.main.config.TestingConfig')
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


def test_post_with_result_code_200(client, mocker):
    """Should be respond with a 200 code"""

    json = {
        "dna": ["ATUCGA", "CAGTGC", "TRATGT", "AGAAGG", "CCCCTA", "TCACT9"]
    }
    response_mock_200 = True, 'Mutant detected'

    validate_sequence_mock = mocker.patch('app.main.controller.mutant_controller.validate_sequence')
    validate_sequence_mock.return_value = response_mock_200
    response = client.post('/api/v1/mutant', json=json)

    assert validate_sequence_mock.called == True
    assert response.status_code == 200


def test_post_with_result_code_403(client, mocker):
    """Should be respond with a 403 code"""

    json = {
        "dna": ["MTUCGA", "CAGTGC", "TRATGT", "AGAAGG", "CUCCTA", "TCACT9"]
    }
    response_mock_403 = False, 'Human detected'

    validate_sequence_mock = mocker.patch('app.main.controller.mutant_controller.validate_sequence')
    validate_sequence_mock.return_value = response_mock_403
    response = client.post('/api/v1/mutant', json=json)

    assert validate_sequence_mock.called == True
    assert response.status_code == 403


def test_post_with_result_code_400_bad_request(client, mocker):
    """Should be respond with a 400 code"""

    json = {
        "dna43": ["MTUCGA", "CAGTGC", "TRATGT", "AGAAGG", "CUCCTA", "TCACT9"]
    }
    response_mock_403 = False, 'Human detected'

    validate_sequence_mock = mocker.patch('app.main.controller.mutant_controller.validate_sequence')
    validate_sequence_mock.return_value = response_mock_403
    response = client.post('/api/v1/mutant', json=json)

    assert validate_sequence_mock.called == False
    assert response.status_code == 400