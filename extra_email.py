import os
import re


def is_email(s):
    # Simple regex to check if the string is an email
    return re.match(r"[^@]+@[^@]+\.[^@]+", s)


def extract_emails_from_file(filename):
    emails = []
    folder_path = os.path.join('extra')
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f'emails.txt')
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
            if format_type == 1:
                parts = line.strip().split(':')
                if len(parts) == 4:  # Ensure the line is correctly formatted
                    protocol, url, email, password = parts
                    if is_email(email):
                        emails.append(email)
                        with open(file_path, 'a') as file2:
                            file2.write(email + ":" + password + "\n")



def main():
    print("Please drag and drop your text file into this window or type the file path, then press Enter:")
    input_file_path = input().strip().strip('"')
    extract_emails_from_file(input_file_path)


if __name__ == "__main__":
    main()
