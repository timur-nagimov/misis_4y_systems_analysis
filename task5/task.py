import numpy as np
import json


def extract_elements(sequence):
    return [element for subsequence in sequence for element in subsequence]


def generate_matrix_from_json(json_input):
    data = json.loads(json_input)
    distinct_elements = set()
    size_of_matrix = len(extract_elements(data))
    adjacency_mat = np.zeros((size_of_matrix, size_of_matrix))

    for group_one in data:
        for element_one in group_one:
            for group_two in data:
                for element_two in group_two:
                    if element_two not in distinct_elements:
                        adjacency_mat[int(element_one) -
                                      1][int(element_two) - 1] = 1
        distinct_elements.update(group_one)

    return adjacency_mat


def compare_and_analyze(mat_a, mat_b):
    analysis_matrix = np.ones((len(mat_a[0]), len(mat_a[0])))

    for idx in range(len(mat_a[0]) - 1):
        if mat_a[idx + 1][idx] != mat_b[idx + 1][idx] and mat_a[idx][idx + 1] != mat_b[idx][idx + 1]:
            analysis_matrix[idx + 1][idx] = 0
            analysis_matrix[idx][idx + 1] = 0

    return analysis_matrix


def output_formatted_results(comp_mat):
    indices = []
    counter = 0

    while counter < len(comp_mat[0]):
        if counter > 0 and comp_mat[counter][counter - 1] == 0:
            indices.pop()
            indices.append([str(counter), str(counter + 1)])
        else:
            indices.append(str(counter + 1))
        counter += 1

    return json.dumps(indices)


def perform_task(input_data):
    input_data = json.loads(input_data)
    matrix_one = generate_matrix_from_json(json.dumps(input_data[0]))
    matrix_two = generate_matrix_from_json(json.dumps(input_data[1]))
    comparison_matrix = compare_and_analyze(matrix_one, matrix_two)
    return output_formatted_results(comparison_matrix)


if __name__ == "__main__":
    input_lines = '[["1","2"],["3","4","5"],"6","7","9",["8","10"]], ["1",["2","3"],"4",["5","6","7"],"8","9","10"]'
    print(perform_task('[' + input_lines + ']'))
