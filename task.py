import numpy as np
import json


def calculate_variance(first_seq, second_seq, third_seq):
    first_seq = json.loads(first_seq)
    second_seq = json.loads(second_seq)
    third_seq = json.loads(third_seq)

    sequence_length = len(first_seq)
    combined_values = np.array([int(first_seq[idx][1]) + int(
        second_seq[idx][1]) + int(third_seq[idx][1]) for idx in range(sequence_length)])
    average_value = np.mean(combined_values)

    variance = np.sum((combined_values - average_value) ** 2) / (2 * 9 *
                                                                 (sequence_length ** 3 - sequence_length) / (12 * (sequence_length - 1)))

    return variance


if __name__ == "__main__":
    first_order_input = '["O1","O2","O3"]'
    second_order_input = '["O1","O3","O2"]'
    third_order_input = '["O1","O3","O2"]'
    print(calculate_variance(first_order_input,
          second_order_input, third_order_input))
