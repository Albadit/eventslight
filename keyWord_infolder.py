import os
import json

def find_keywords_in_files(folder_path, keywords, output_file):
    found_files = {}
    
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    matches = [kw for kw in keywords if kw in content]
                    if matches:
                        found_files[file_path] = matches
            except Exception as e:
                print(f'Error reading {file_path}: {e}')

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(found_files, f, indent=4)
    print(f'Results saved to: {output_file}')


folder_path = 'C:/Users/Albadit/Documents/GitHub/eventslight/odoo'  # Replace with your folder path
keywords = ['subscription', 'Enterprise', 'superuser', 'super_user']  # Replace with the keywords you want to search for
output_file = 'found_files.json'  # The output file name (saved in the script's directory)
find_keywords_in_files(folder_path, keywords, output_file)
