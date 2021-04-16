def validate_square_matrix(matrix):
    return all([len(row) == len(matrix) for row in matrix])


def get_matrix_from_list(dna_list):
    matrix = []
    for item in dna_list:
        matrix.append(list(item))
    return matrix
