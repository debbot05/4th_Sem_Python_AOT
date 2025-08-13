input_file_path = 'input_file.txt'
output_file_path = 'output_file.txt'
def add_line_numbers(input_path, output_path):
    with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
        for line_number, line in enumerate(input_file, start=1):
            output_file.write(f"{line_number}: {line}")

add_line_numbers(input_file_path, output_file_path)