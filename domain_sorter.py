import os


def process_file(input_file_path):
    domain_dict = {}
    with open('./domain.txt', 'r') as domain:
        for line in domain:
            folder_path = os.path.join('sorted_emails', line.strip())
            os.makedirs(folder_path, exist_ok=True)
            file_path = os.path.join(folder_path, f'emails.txt')
            domain_dict[line.strip()] = file_path
    # Read and process the file
    with open(input_file_path, 'r') as file:
        for line in file:
            print('proccess line: ' + line)
            if ':' in line:
                try:
                    email, password = line.strip().split(':')
                    domain_str = email.split('@')[-1]
                    for key, value in domain_dict.items():
                        if key in domain_str:
                            with open(domain_dict[key], 'a') as file2:
                                print('write: ' + email)
                                file2.write(line)
                except Exception as ex:
                    print(ex)


if __name__ == '__main__':
    print("Please drag and drop your text file into this window or type the file path, then press Enter:")
    input_file_path = input().strip().strip('"')  # Remove any extra whitespace or quotes
    process_file(input_file_path)
    input("Press Enter to exit...")  # Keeps the console window open until user presses Enter
