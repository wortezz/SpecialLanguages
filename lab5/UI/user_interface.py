import os
import sys

lab5_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab5_root)

from lab5.classes.cube import Cube
from lab5.classes.cone import Cone
from lab5.classes.octahedron import Octahedron
from lab5.classes.art_configurator import ArtConfigurator

def main():
    art_configurator = ArtConfigurator()

    while True:
        try:
            shape_type = input("Виберіть 3D форму (cube, cone, octahedron): ").strip().lower()
            try:
                size = int(input("Введіть розмір: "))
            except ValueError:
                raise ValueError("Розмір має бути цілим числом.")
            match shape_type:
                case 'cube':
                    shape = Cube(size)
                case 'cone':
                    shape = Cone(size)
                case 'octahedron':
                    shape = Octahedron(size)
                case _:
                    raise ValueError("Невірний тип форми.")
            break
        except ValueError as e:
            print(e)

    default_color_code = art_configurator.reset_color()

    while True:
        try:
            print("\nВиберіть дію:")
            print("1. Повернути форму")
            print("2. Змінити розмір")
            print("3. Вибрати колір")
            print("4. Відобразити ASCII-арт")
            print("5. Змінити форму")
            print("6. Зберегти ASCII-арт в файл")
            print("7. Вийти")

            choice = input("Ваш вибір: ").strip()

            match choice:
                case '1':
                    art_configurator.rotate_shape(shape)

                case '2':
                    art_configurator.change_shape_size(shape)

                case '3':
                    color_code = art_configurator.choose_color()

                case '4':
                    projection = shape.project_to_2d()
                    shape.render_ascii(projection, color_code if 'color_code' in locals() else default_color_code)

                case '5':
                    shape_type = input("Виберіть нову 3D форму (cube, cone, octahedron): ").strip().lower()
                    try:
                        size = int(input("Введіть розмір для нової форми: "))
                    except ValueError as e:
                        raise ValueError("Розмір повинен бути цілим числом.")
                    match shape_type:
                        case 'cube':
                            shape = Cube(size)
                        case 'cone':
                            shape = Cone(size)
                        case 'octahedron':
                            shape = Octahedron(size)
                        case _:
                            raise ValueError("Невірний тип форми.")

                case '6':
                    projection = shape.project_to_2d()
                    art_configurator.save_art(projection, shape)

                case '7':
                    print("Вихід з програми.")
                    break

                case _:
                    print("Невірний вибір.")

        except (ValueError, FileNotFoundError, NotImplementedError) as e:
            print(f"Помилка: {e}")

