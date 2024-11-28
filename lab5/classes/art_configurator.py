import math
from lab5.classes.color_utils import ColorUtils
from lab5.classes.file_saver import FileSaver

class ArtConfigurator:
    def __init__(self):
        self.color_utils = ColorUtils()

    def choose_color(self):
        return self.color_utils.choose_color()

    def reset_color(self):
        return self.color_utils.reset_color()

    def rotate_shape(self, shape):
        try:
            angle_x = float(input("Введіть кут обертання по X: "))
            angle_y = float(input("Введіть кут обертання по Y: "))
            angle_z = float(input("Введіть кут обертання по Z: "))
            shape.rotate(angle_x, angle_y, angle_z)
        except ValueError:
            raise ValueError("Кут має бути цілим числом.")

    def change_shape_size(self, shape):
        try:
            size = int(input("Введіть новий розмір: "))
            shape.size = size
        except ValueError:
            raise ValueError("Розмір має бути цілим числом.")


    def save_art(self, projection, shape):
        filename = input("Введіть ім'я файлу для збереження (без розширення): ") + ".txt"
        FileSaver.save_ascii_art(projection, filename)

    def display_art(self, projection, color_code):
        shape.render_ascii(projection, color_code)
