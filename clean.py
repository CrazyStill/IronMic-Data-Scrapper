import re

def remove_duplicates(lines):
    unique_lines = []
    previous_line = None
    for line in lines:
        if line != previous_line:
            unique_lines.append(line)
        previous_line = line
    return unique_lines

def extract_info_after_colon(line):
    colon_index = line.find(':')
    if colon_index != -1:
        return line[colon_index + 1:].strip()
    else:
        return line

def clean_lines(html_lines):
    cleaned_lines = []
    for line in html_lines:
        clean_line = re.sub(r'<[^>]*>', '', line)
        clean_line = re.sub(r',\s*', ' ', clean_line)
        clean_line = re.sub(r'_\d+', '', clean_line)
        clean_line = re.sub(r'_', ' ', clean_line)
        cleaned_lines.append(clean_line.strip())

    cleaned_lines = remove_duplicates(cleaned_lines)
    cleaned_lines = [extract_info_after_colon(line) for line in cleaned_lines]
    
    return cleaned_lines

def main():
    with open("output.txt", "r") as file:
        html_lines = file.readlines()
        cleaned_lines = clean_lines(html_lines)
        for line in cleaned_lines:
            print(line)

if __name__ == "__main__":
    main()
