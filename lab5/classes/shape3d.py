import math
from lab5.classes.color_utils import ColorUtils

class Shape3D:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Розмір має бути додатнім числом.")
        self.size = size
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0

    def rotate(self, angle_x=0, angle_y=0, angle_z=0):
        self.angle_x += math.radians(angle_x)
        self.angle_y += math.radians(angle_y)
        self.angle_z += math.radians(angle_z)

    def apply_rotation(self, x, y, z):
        y, z = (
            y * math.cos(self.angle_x) - z * math.sin(self.angle_x),
            y * math.sin(self.angle_x) + z * math.cos(self.angle_x)
        )
        x, z = (
            x * math.cos(self.angle_y) + z * math.sin(self.angle_y),
            -x * math.sin(self.angle_y) + z * math.cos(self.angle_y)
        )
        x, y = (
            x * math.cos(self.angle_z) - y * math.sin(self.angle_z),
            x * math.sin(self.angle_z) + y * math.cos(self.angle_z)
        )
        return int(x), int(y), int(z)

    def draw_line(self, x1, y1, x2, y2, canvas, symbol):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            if 0 <= y1 < len(canvas) and 0 <= x1 < len(canvas[0]):
                canvas[int(y1)][int(x1)] = symbol
            if x1 == x2 and y1 == y2:
                break
            e2 = err * 2
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

    def project_to_2d(self):
        raise NotImplementedError("Цей метод має бути імплементованим!")

    def render_ascii(self, projection, color_code):
        reset_color = ColorUtils().reset_color()
        for row in projection:
            print(color_code + "".join(row) + reset_color)
