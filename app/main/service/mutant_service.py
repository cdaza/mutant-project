from ..utils.matrix_utils import get_matrix_from_list, validate_square_matrix, get_sequences_detected
from ..enum.operations_enum import Operations


def validate_sequence(dna_list):
    matrix = get_matrix_from_list(dna_list)
    square_matrix = validate_square_matrix(matrix)
    if square_matrix:
        return is_mutant(matrix)
    else:
        return False, "Looks like your DNA sequence is incomplete"


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
        return True, str(e)

    return False, 'is ok'
