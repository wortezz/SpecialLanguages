import pandas as pd
import os
import matplotlib.pyplot as plt
from lab8.Builders.base_builder import DataVisualizationBuilder

class CSVDataVisualizationBuilder(DataVisualizationBuilder):
    def load_data(self, file_path: str):
        try:
            self._data = pd.read_csv(file_path)
            print("Дані завантажено успішно!")
        except FileNotFoundError:
            print(f"Файл за шляхом {file_path} не знайдено. Перевірте правильність шляху.")

    def explore_data(self):
        if self._data is not None:
            print("Огляд даних:")
            print(self._data.describe())
            print("\nЕкстремальні значення:")
            for column in self._data.select_dtypes(include='number'):
                print(f"{column} -> min: {self._data[column].min()}, max: {self._data[column].max()}")
        else:
            print("Дані не завантажені!")

    def process_data(self):
        if self._data is not None:
            self._processed_data = self._data.dropna()
            print("Дані оброблено успішно!")
        else:
            print("Дані не завантажені!")

    def create_basic_visualization(self):
        if self._processed_data is not None:
            date_column = 'Date'
            self._processed_data[date_column] = pd.to_datetime(self._processed_data[date_column])

            plt.figure(figsize=(10, 6))
            for column in ['Temperature', 'Humidity', 'Precipitation']:
                if column in self._processed_data.columns:
                    plt.plot(self._processed_data[date_column], self._processed_data[column], label=column)
            plt.xlabel("Дата")
            plt.ylabel("Значення")
            plt.legend()
            plt.title("Базова візуалізація: Температура, Вологість, Опади")
            self._last_figure = plt.gcf()
            plt.show()
        else:
            print("Дані не оброблені!")

    def create_line_chart(self, x_column=None, y_column=None):
        if self._processed_data is not None:
            x_column = x_column or self._processed_data.columns[0]
            y_column = y_column or self._processed_data.columns[1]
            plt.figure(figsize=(8, 6))
            plt.plot(self._processed_data[x_column], self._processed_data[y_column], label=f"{y_column} vs {x_column}")
            plt.title("Лінійний графік")
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.legend()
            self._last_figure = plt.gcf()
            plt.show()
        else:
            print("Дані не оброблені!")

    def create_bar_chart(self, x_column=None, y_column=None):
        if self._processed_data is not None:
            x_column = x_column or self._processed_data.columns[1]
            y_column = y_column or self._processed_data.columns[2]
            plt.figure(figsize=(8, 6))
            plt.bar(self._processed_data[x_column], self._processed_data[y_column], color='blue', alpha=0.7)
            plt.title("Стовпчикова діаграма")
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            self._last_figure = plt.gcf()
            plt.show()
        else:
            print("Дані не оброблені!")

    def create_scatter_plot(self, x_column=None, y_column=None):
        if self._processed_data is not None:
            x_column = x_column or self._processed_data.columns[2]
            y_column = y_column or self._processed_data.columns[3]
            plt.figure(figsize=(8, 6))
            plt.scatter(self._processed_data[x_column], self._processed_data[y_column], c='orange')
            plt.title("Діаграма розсіювання")
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            self._last_figure = plt.gcf()
            plt.show()
        else:
            print("Дані не оброблені!")

    def create_combined_visualization(self, x_column=None, y_column=None):
        if self._processed_data is not None:
            x_column = x_column or self._processed_data.columns[0]
            x1_column = self._processed_data.columns[2]
            x2_column = self._processed_data.columns[3]
            y_column = y_column or self._processed_data.columns[1]

            fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=False)

            axes[0].plot(self._processed_data[x_column], self._processed_data[y_column], color='blue')
            axes[0].set_title("Лінійний графік")
            axes[0].set_xlabel(x_column)
            axes[0].set_ylabel(y_column)

            axes[1].bar(self._processed_data[x1_column], self._processed_data[y_column], color='green', alpha=0.7)
            axes[1].set_title("Стовпчикова діаграма")
            axes[1].set_xlabel(x1_column)

            axes[2].scatter(self._processed_data[x2_column], self._processed_data[y_column], color='orange')
            axes[2].set_title("Діаграма розсіювання")
            axes[2].set_xlabel(x2_column)

            plt.tight_layout()
            self._last_figure = plt.gcf()
            plt.show()
        else:
            print("Дані не оброблені!")

    def export_visualization(self, filename: str, format: str):
        valid_types = ["png", "jpg", "svg"]

        if format not in valid_types:
            raise ValueError(f"Неправильний тип файлу. Доступні формати: {', '.join(valid_types)}")
        if self._last_figure:
            output_dir = "../Lab8/Data"
            os.makedirs(output_dir, exist_ok=True)

            file_path = os.path.join(output_dir, f"{filename}.{format}")

            self._last_figure.savefig(file_path, format=format)
            print(f"Візуалізація збережена як {file_path}")
        else:
            print("Немає активного графіка для збереження!")