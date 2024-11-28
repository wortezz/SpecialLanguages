import json
import csv
import os

class DataSaver:
    @staticmethod
    def save_data(data, filename, format_choice):
        data_folder = "../Lab7/Data"
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

        full_path = os.path.join(data_folder, filename)

        if format_choice == 'json':
            DataSaver.save_as_json(data, full_path)
        elif format_choice == 'csv':
            DataSaver.save_as_csv(data, full_path)
        elif format_choice == 'txt':
            DataSaver.save_as_txt(data, full_path)
        else:
            print("Неправильний формат. Будь ласка, спробуйте ще раз.")

    @staticmethod
    def save_as_json(data, filename):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}.")

    @staticmethod
    def save_as_csv(data, filename):
        keys = data[0].keys()
        with open(filename, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data saved to {filename}.")

    @staticmethod
    def save_as_txt(data, filename):
        with open(filename, "w") as f:
            for item in data:
                f.write(str(item) + "\n")
        print(f"Data saved to {filename}.")