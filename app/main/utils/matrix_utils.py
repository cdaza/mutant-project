from ..utils.operations_strategy_utils import get_dict_operations

NUM_SEQUENCE_MUTANT = 2


def validate_square_matrix(matrix):
    return all([len(row) == len(matrix) for row in matrix])


def get_matrix_from_list(dna_list):
    matrix = []
    for item in dna_list:
        matrix.append(list(item))
    return matrix


def get_sequences_detected(matrix, sequence_detected, row, column, validation):
    sequence = []
    range_list = [*range(0, 4)]
    dict_operations = get_dict_operations()

    for item in range_list:
        sequence.append(dict_operations[validation](matrix, row, column, item))

    sequence_detected = sequence_detected + validate_sequence(sequence)

    if sequence_detected == NUM_SEQUENCE_MUTANT:
        raise ValueError('Mutant detected')
    return sequence_detected


def validate_sequence(sequence):
    return len(set(sequence)) == 1



