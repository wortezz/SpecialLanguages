from lab5.classes.shape3d import Shape3D
import math

class Cone(Shape3D):

    def __init__(self, size):
        super().__init__(size)

    def project_to_2d(self):
        if self.size <= 0:
            raise ValueError("Розмір має бути додатнім числом.")
        projection_height = self.size * 2
        projection_width = self.size * 2
        projection = [[" " for _ in range(int(projection_width))] for _ in range(int(projection_height))]
        half = self.size // 2

        vertices = []
        for angle in range(0, 360, 10):
            rad = math.radians(angle)
            x = half * math.cos(rad)
            y = half * math.sin(rad)
            vertices.append((x, 0, y))
        vertices.append((0, -half, 0))

        rotated_vertices = [self.apply_rotation(x, y, z) for x, y, z in vertices]

        edges = []
        base_count = len(vertices) - 1
        for i in range(base_count):
            edges.append((i, (i + 1) % base_count))
            edges.append((i, base_count))

        for start, end in edges:
            x1, y1, z1 = rotated_vertices[start]
            x2, y2, z2 = rotated_vertices[end]
            x1 += self.size
            y1 += projection_height // 2
            x2 += self.size
            y2 += projection_height // 2
            symbol = "." if z1 > 0 and z2 > 0 else "#"
            self.draw_line(int(x1), int(y1), int(x2), int(y2), projection, symbol)

        return projection
