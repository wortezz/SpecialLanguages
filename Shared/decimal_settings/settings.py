class DecimalSettings:
    def __init__(self, initial_precision=1):
        if initial_precision < 0:
            raise ValueError("Кількість знаків після коми повинна бути невід'ємною.")
        self._decimal_precision = initial_precision

    def set_decimal_precision(self, precision=None):
        if precision is None:
            precision = input("Вкажіть кількість знаків після коми: ")

        try:
            precision = int(precision)
        except ValueError:
            raise TypeError("Введіть ціле (додатнє) число.")

        if precision < 0:
            raise ValueError("Кількість знаків повинна бути не від'ємною. Спробуйте ще раз.")

        self._decimal_precision = precision
        print(f"Кількість знаків після коми встановлено на {self._decimal_precision}.")

    def get_decimal_precision(self):
        return self._decimal_precision

