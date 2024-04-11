# This is used for adding data to the Lines file
# Run the Scrapper first
def search_file(search_query): 
    found_lines = []
    with open('html.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            for term in search_query:
                if term in line:
                    found_lines.append(i + 1)
    return found_lines 


def main():
    search_terms = ['SAN_TWR', 'SAN_GND','SEA_GND','SEA_TWR', 'LAX_55_CTR', 'SCT_APP', 'PDX_TWR', 'PDX_GND', 'SEA_16_CTR', 'LAS_E_TWR', 'SLC_C_TWR','SLC_33_CTR','JAX_30_CTR','JAX_TWR','HNL_02_CTR','DEN_TWR','DEN_17_CTR']
    found_lines = search_file(search_terms)

    with open('lines.txt', 'w') as output_file:
        for line_number in found_lines:
                output_file.write(f"{line_number}\n")
                next_line_number = line_number + 1
                output_file.write(f"{next_line_number}\n")
        print("Search results have been appended to 'lines.txt'.")

if __name__ == "__main__":
    main()
