import numpy as np


def compute_entropy(dist_values):
    return -np.sum(dist_values * np.log2(dist_values, where=np.abs(dist_values) > 1e-4))


def task():
    sum_outcomes = sorted({die1 + die2 for die1 in range(1, 7)
                          for die2 in range(1, 7)})
    product_outcomes = sorted(
        {die1 * die2 for die1 in range(1, 7) for die2 in range(1, 7)})

    sum_mapping = {val: index for index, val in enumerate(sum_outcomes)}
    product_mapping = {val: index for index,
                       val in enumerate(product_outcomes)}

    outcomes_matrix = np.zeros((len(sum_outcomes), len(product_outcomes)))
    for die1 in range(1, 7):
        for die2 in range(1, 7):
            outcomes_matrix[sum_mapping[die1 + die2],
                            product_mapping[die1 * die2]] += 1

    probabilities_matrix = outcomes_matrix / 36

    sum_probs = np.sum(probabilities_matrix, axis=1)
    product_probs = np.sum(probabilities_matrix, axis=0)

    total_entropy = compute_entropy(probabilities_matrix)
    sum_entropy = compute_entropy(sum_probs)
    product_entropy = compute_entropy(product_probs)
    conditional_entropy = total_entropy - sum_entropy
    mutual_information = product_entropy - conditional_entropy

    results = [round(num, 2) for num in [total_entropy, sum_entropy,
                                         product_entropy, conditional_entropy, mutual_information]]
    return results


if __name__ == "__main__":
    print(task())
