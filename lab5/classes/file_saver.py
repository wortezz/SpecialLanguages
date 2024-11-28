import os

class FileSaver:
    @staticmethod
    def save_ascii_art(projection, filename):
        os.makedirs('../Lab5/data', exist_ok=True)
        file_path = os.path.join('../Lab5/data', filename)

        with open(file_path, 'w', encoding='utf-8') as f:
            for row in projection:
                f.write("".join(row) + "\n")
        print(f"ASCII-арт збережено в: {file_path}")
