from lab1.runner import main as lab1_main
from lab2.interfaces import main as lab2_main
from lab3.UI.user_interface import main as lab3_main
from lab4.UI.user_interface import main as lab4_main
from lab5.UI.user_interface import main as lab5_main
from lab6.coverage_check import main as lab6_main
from lab7.UI.user_interface import main as lab7_main
from lab8.Director.director import Director
from lab8.UI.user_interface import main as lab8_main

class Facade:
    def __init__(self):
        self.labs = {
            1: self.run_lab1,
            2: self.run_lab2,
            3: self.run_lab3,
            4: self.run_lab4,
            5: self.run_lab5,
            6: self.run_lab6,
            7: self.run_lab7,
            8: self.run_lab8,
        }

    def show_menu(self):
        print("\n== Доступні лабораторні роботи: ==")
        for lr_index in sorted(self.labs.keys()):
            print(f"{lr_index}: Лабораторна робота №{lr_index}")
        print("0: Вихід")

    def run_lab(self, choice):
        if choice in self.labs:
            print(f"Запуск лабораторної роботи №{choice}")
            self.labs[choice]()
        elif choice == 0:
            print("Вихід із програми.")
        else:
            print("Невірний вибір. Спробуйте ще раз.")

    def run_lab1(self):
        lab1_main()

    def run_lab2(self):
        lab2_main()

    def run_lab3(self):
        lab3_main()

    def run_lab4(self):
        lab4_main()

    def run_lab5(self):
        lab5_main()

    def run_lab6(self):
        lab6_main()

    def run_lab7(self):
        lab7_main()

    def run_lab8(self):
        director = Director()
        lab8_main(director=director)
