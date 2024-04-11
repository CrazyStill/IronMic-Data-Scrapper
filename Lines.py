# This is used for adding data to the Lines file
# Run the Scrapper first
def search_file(search_query): 
    found_lines = []
    with open('html.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if search_query in line:
                found_lines.append(i + 1)
    return found_lines 

def check_existing_line_numbers(line_numbers):
    with open('lines.txt', 'r') as file:
        existing_lines = set(int(line.strip()) for line in file)
    for num in line_numbers:
        if num in existing_lines:
            return True
    return False

def main():
    while True:
        search_query = input("Enter the text to search for (Enter '0' to exit): ")
        if search_query == '0':
            print("Exiting...")
            break

        found_lines = search_file(search_query)

        if check_existing_line_numbers(found_lines):
            print("Error: Line numbers already exist in 'lines.txt'. Skipping...")
        else:
            with open('lines.txt', 'a') as output_file:
                for line_number in found_lines:
                    output_file.write(f"{line_number}\n")
                    next_line_number = line_number + 1
                    output_file.write(f"{next_line_number}\n")
            print("Search results have been appended to 'lines.txt'.")

if __name__ == "__main__":
    main()
