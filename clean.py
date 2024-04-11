import re

def extract_info_after_colon(line):
    colon_index = line.find(':')
    if colon_index != -1:
        return line[colon_index + 1:].strip()
    else:
        return line

def clean_lines(html_lines):
    cleaned_lines = []
    previous_line = None
    for line in html_lines:
        clean_line = re.sub(r'<[^>]*>', '', line)
        clean_line = re.sub(r',\s*', ' ', clean_line)
        clean_line = re.sub(r'_\d+', '', clean_line)
        # Remove letters and numbers between double underscores and then remove underscores
        clean_line = re.sub(r'_\w+_', ' ', clean_line)
        clean_line = re.sub(r'_', ' ', clean_line)
        
        
        
        # Restrict names to 7 characters and remove consecutive duplicates
        if clean_line != previous_line:
            words = clean_line.split()
            restricted_words = [word[:7] for word in words]
            clean_line = ' '.join(restricted_words)
            cleaned_lines.append(clean_line.strip())
            previous_line = clean_line

    cleaned_lines = [extract_info_after_colon(line) for line in cleaned_lines]
    
    return cleaned_lines

def main():
    with open("output.txt", "r") as file:
        html_lines = file.readlines()
        cleaned_lines = clean_lines(html_lines)
        
        # Write cleaned output to clean.txt
        with open("clean.txt", "w") as clean_file:
            for line in cleaned_lines:
                clean_file.write(line + "\n")

if __name__ == "__main__":
    main()
