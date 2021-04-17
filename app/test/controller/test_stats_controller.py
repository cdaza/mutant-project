import pytest
from manage import app


@pytest.fixture
def client():
    app.config.from_object('app.main.config.TestingConfig')
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


def test_get_with_result_code_200(client, mocker):
    """Should be respond with a 200 code"""

    response_mock_200 = {
        'count_mutant_dna': 0,
        'count_human_dna': 0,
        'ratio': 0
    }

    get_stats_sequence_mock = mocker.patch('app.main.controller.stats_controller.get_stats')
    get_stats_sequence_mock.return_value = response_mock_200
    response = client.get('/api/v1/stats')

    assert get_stats_sequence_mock.called == True
    assert response.status_code == 200
