from app.main.service.stats_service import get_stats


def test_get_stats_with_zero(mocker):
    """Should be respond with values in zero"""

    result_expected = {
        'count_mutant_dna': 0,
        'count_human_dna': 0,
        'ratio': 0
    }

    get_dict_from_key_mock = mocker.patch('app.main.service.stats_service.get_dict_from_key')
    get_dict_from_key_mock.return_value = None

    result = get_stats()

    assert get_dict_from_key_mock.called == True
    assert result == result_expected


def test_get_stats_with_values_ratio_zero(mocker):
    """Should be respond with different values and ratio in zero"""

    result_expected = {
        'count_mutant_dna': 1,
        'count_human_dna': 0,
        'ratio': 0
    }

    dict_from_key_mock = {b'count_mutant_dna': b'1', b'count_human_dna': b'0'}

    get_dict_from_key_mock = mocker.patch('app.main.service.stats_service.get_dict_from_key')
    get_dict_from_key_mock.return_value = dict_from_key_mock

    result = get_stats()

    assert get_dict_from_key_mock.called == True
    assert result == result_expected


def test_get_stats_with_values_with_ratio_value(mocker):
    """Should be respond with different values """

    result_expected = {
        'count_mutant_dna': 1,
        'count_human_dna': 5,
        'ratio': 0.2
    }

    dict_from_key_mock = {b'count_mutant_dna': b'1', b'count_human_dna': b'5'}

    get_dict_from_key_mock = mocker.patch('app.main.service.stats_service.get_dict_from_key')
    get_dict_from_key_mock.return_value = dict_from_key_mock

    result = get_stats()

    assert get_dict_from_key_mock.called == True
    assert result == result_expected
