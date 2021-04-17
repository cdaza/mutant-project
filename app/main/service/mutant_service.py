from ..utils.matrix_utils import get_matrix_from_list, validate_square_matrix, get_sequences_detected
from ..utils.redis_utils import insert_key_value, get_value_from_key, insert_key_dict, get_dict_from_key
from ..enum.operations_enum import Operations


def validate_sequence(dna_list):
    matrix = get_matrix_from_list(dna_list)
    square_matrix = validate_square_matrix(matrix)
    if square_matrix:
        key = get_key_from_list(dna_list)
        previous_value = get_value_from_key(key)
        if previous_value is None:
            result_is_mutant = is_mutant(matrix)
            save_result_db(key, result_is_mutant)
        else:
            result_is_mutant = bool(previous_value)

        message = 'Mutant detected' if result_is_mutant else 'Human detected'

        return result_is_mutant, message
    else:
        return False, "Looks like your DNA sequence is incomplete"


def save_result_db(key, result_is_mutant):
    is_mutant_value = result_is_mutant
    value = int(result_is_mutant)
    success = insert_key_value(key, value)
    if success:
        key_stats = "stats"
        result = get_dict_from_key(key_stats)
        count_mutant_dna_value = 1 if is_mutant_value else 0
        count_human_dna_value = 0 if is_mutant_value else 1

        if any(result.values()):
            count_mutant_dna = int(result[b'count_mutant_dna']) + count_mutant_dna_value
            count_human_dna = int(result[b'count_human_dna']) + count_human_dna_value
            insert_dict_stats(key_stats, count_mutant_dna, count_human_dna)
        else:
            insert_dict_stats(key_stats, count_mutant_dna_value, count_human_dna_value)


def insert_dict_stats(key_stats, count_mutant_dna, count_human_dna):
    dict_stats = {
        "count_mutant_dna": count_mutant_dna,
        "count_human_dna": count_human_dna,
    }

    insert_key_dict(key_stats, dict_stats)


def get_key_from_list(dna_list):
    return ''.join(dna_list)


def is_mutant(matrix):
    matrix_length = len(matrix)
    row = 0
    sequence_detected = 0
    try:
        while row < matrix_length:
            column = 0
            row_movement_down = row + 3
            while column < matrix_length:
                value = matrix[row][column]
                column_movement_right = column + 3
                column_movement_left = column - 3
                validations = []

                # Validate horizontally
                if column_movement_right < matrix_length and value == matrix[row][column_movement_right]:
                    validations.append(Operations.HORIZONTALLY)

                if row_movement_down < matrix_length:

                    # Validate vertically
                    if value == matrix[row_movement_down][column]:
                        validations.append(Operations.VERTICALLY)

                    # Validate diagonally right
                    if column_movement_right < matrix_length and value == matrix[row_movement_down][column_movement_right]:
                        validations.append(Operations.DIAGONALLY_RIGHT)

                    # Validate diagonally left
                    if column_movement_left >= 0 and value == matrix[row_movement_down][column_movement_left]:
                        validations.append(Operations.DIAGONALLY_LEFT)

                for validation in validations:
                    sequence_detected = get_sequences_detected(matrix, sequence_detected, row, column, validation)

                column = column + 1

            row = row + 1
    except ValueError as e:
        print(e)
        return True

    return False
