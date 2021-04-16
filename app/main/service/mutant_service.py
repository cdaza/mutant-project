from ..utils.matrix_utils import get_matrix_from_list, validate_square_matrix


def validate_sequence(dna_list):
    matrix = get_matrix_from_list(dna_list)
    square_matrix = validate_square_matrix(matrix)
    if square_matrix:
        return is_mutant(matrix)
    else:
        return "Tu secuencia de ADN parece incompleta"


def is_mutant(matrix):
    return "is mutant"
