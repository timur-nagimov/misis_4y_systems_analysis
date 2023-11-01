import io
import csv
import numpy as np


def read_csv_to_string(filepath: str, delimiter=';') -> str:
    with open(filepath, 'r') as csvfile:
        content = [line for line in csv.reader(csvfile, delimiter=delimiter)]

    output_buffer = io.StringIO()
    csv_writer = csv.writer(output_buffer, delimiter=delimiter)
    csv_writer.writerows(content)

    return output_buffer.getvalue().strip()


csv_path = "./task3.csv"
csv_content = read_csv_to_string(csv_path)


def task(csv_content: str) -> float:
    buffer = io.StringIO(csv_content)
    csv_reader = csv.reader(buffer, delimiter=';')
    data = np.array([[int(value) for value in row]
                    for row in csv_reader], dtype=int)

    row_count, col_count = data.shape

    total_entropy = 0
    for row in range(row_count):
        for col in range(col_count):
            value = data[row, col]
            if value != 0:
                probability = value / (row_count - 1)
                total_entropy -= probability * np.log2(probability)

    return round(total_entropy, 1)


result = task(csv_content)
print(result)
