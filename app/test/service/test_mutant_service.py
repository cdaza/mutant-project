from app.main.service.mutant_service import validate_sequence, is_mutant, save_result_db
from app.main.utils.matrix_utils import get_matrix_from_list


def test_validate_sequence_mutant(mocker):
    """Should be respond with True and mutant detected"""

    dna_list = ["ATUCGA", "CAGTGC", "TRATGT", "AGAAGG", "CCCCTA", "TCACT9"]

    get_value_from_key_mock = mocker.patch('app.main.service.mutant_service.get_value_from_key')
    get_value_from_key_mock.return_value = None
    save_result_db_mock = mocker.patch('app.main.service.mutant_service.save_result_db')

    result = validate_sequence(dna_list)

    assert save_result_db_mock.called == True
    assert get_value_from_key_mock.called == True
    assert result == (True, 'Mutant detected')


def test_validate_sequence_human(mocker):
    """Should be respond with False and human detected"""

    dna_list = ["PTUCGA", "CAGTGC", "TRATGT", "AGAAGG", "CQCCTA", "TCACT9"]

    get_value_from_key_mock = mocker.patch('app.main.service.mutant_service.get_value_from_key')
    get_value_from_key_mock.return_value = None
    save_result_db_mock = mocker.patch('app.main.service.mutant_service.save_result_db')

    result = validate_sequence(dna_list)

    assert save_result_db_mock.called == True
    assert get_value_from_key_mock.called == True
    assert result == (False, 'Human detected')


def test_validate_sequence_not_square_matrix(mocker):
    """Should be respond with False and Looks like your DNA sequence is incomplete"""

    dna_list = ["PTUCGA", "CAGTGC", "TRATGT", "AGAAGG", "CQCCTA23", "TCACT9"]

    get_value_from_key_mock = mocker.patch('app.main.service.mutant_service.get_value_from_key')
    get_value_from_key_mock.return_value = None
    save_result_db_mock = mocker.patch('app.main.service.mutant_service.save_result_db')

    result = validate_sequence(dna_list)

    assert save_result_db_mock.called == False
    assert get_value_from_key_mock.called == False
    assert result == (False, 'Looks like your DNA sequence is incomplete')


def test_is_mutant_horizontally(mocker):
    """Should be respond True with horizontal sequence"""

    dna_list = ["AAAATG", "CCCCTQ", "TRATGT", "AGAAGG", "CQCCTA", "TCACT9"]
    matrix_test = get_matrix_from_list(dna_list)

    is_mutant_result = is_mutant(matrix_test)

    assert is_mutant_result == True


def test_is_mutant_vertically(mocker):
    """Should be respond True with vertical sequence"""

    dna_list = ["AYDATG", "ACDCTQ", "ARDTGT", "AGDAGG", "CQCCTA", "TCACT9"]
    matrix_test = get_matrix_from_list(dna_list)

    is_mutant_result = is_mutant(matrix_test)

    assert is_mutant_result == True


def test_save_result(mocker):
    """Should be save results"""

    key = 'any_key'
    result_is_mutant = True
    dict_from_key_mock = {b'count_mutant_dna': b'1', b'count_human_dna': b'5'}

    insert_key_value_mock = mocker.patch('app.main.service.mutant_service.insert_key_value')
    insert_key_value_mock.return_value = True
    get_dict_from_key_mock = mocker.patch('app.main.service.mutant_service.get_dict_from_key')
    get_dict_from_key_mock.return_value = dict_from_key_mock
    insert_key_dict_mock = mocker.patch('app.main.service.mutant_service.insert_key_dict')

    save_result_db(key, result_is_mutant)

    assert insert_key_value_mock.called == True
    assert get_dict_from_key_mock.called == True
    assert insert_key_dict_mock.called == True