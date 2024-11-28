import os

class FileManager:
    def save_to_file(self, art):
        if not os.path.exists('../Lab4/data'):
            os.makedirs('../Lab4/data')
        file_name = input("Введіть назву файлу для збереження (Наприклад art.txt): ").strip()
        if not file_name:
            raise ValueError("Назва файлу не може бути пустою.")
        full_path = os.path.join('../Lab4/data', file_name)
        with open(full_path, 'w') as file:
             for line in art:
                file.write(line + '\n')
        print(f"ASCII art збережено в: {full_path}")
