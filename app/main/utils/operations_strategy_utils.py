from ..enum.operations_enum import Operations


def horizontal_sequence(matrix, row, column, item):
    return matrix[row][column + item]


def vertical_sequence(matrix, row, column, item):
    return matrix[row + item][column]


def diagonal_right_sequence(matrix, row, column, item):
    return matrix[row + item][column + item]


def diagonal_left_sequence(matrix, row, column, item):
    return matrix[row + item][column - item]


def get_dict_operations():
    dict_operations = {
        Operations.HORIZONTALLY: horizontal_sequence,
        Operations.VERTICALLY: vertical_sequence,
        Operations.DIAGONALLY_RIGHT: diagonal_right_sequence,
        Operations.DIAGONALLY_LEFT: diagonal_left_sequence
    }

    return dict_operations