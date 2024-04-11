def retrieve_html_lines(line_numbers):
    # Open the text file to read its content
    with open('html.txt', 'r', encoding='utf-8') as file:
        # Initialize a list to store the HTML lines
        html_lines = []
        
        # Iterate over each line in the file
        for line_num, line in enumerate(file, start=1):
            # Check if the current line number matches any of the given line numbers
            if line_num in line_numbers:
                html_lines.append(f"Line {line_num}: {line.strip()}")

    # Write the HTML lines to the output text file
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        output_file.write("\n".join(html_lines))

# Read line numbers from the lines.txt file
def read_line_numbers(filename):
    with open(filename, 'r', encoding='utf-8') as lines_file:
        return [int(line.strip()) for line in lines_file]

def retrive_data_start():
    line_numbers_file = 'lines.txt'

# Read line numbers from the file
    html_line_numbers = read_line_numbers(line_numbers_file)

# Call the function 
    retrieve_html_lines(html_line_numbers)
