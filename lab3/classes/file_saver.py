import os

class FileManager:
    def save_to_file(self, art):
        if not os.path.exists('../Lab3/data'):
            os.makedirs('../Lab3/data')
        file_name = input("Enter the file name to save ASCII art (e.g., art.txt): ")
        if not file_name:
            raise ValueError("File name cannot be empty.")
        full_path = os.path.join('../Lab3/data', file_name)
        with open(full_path, 'w') as file:
            file.write(art)
        print(f"ASCII art збережено в: {full_path}")
