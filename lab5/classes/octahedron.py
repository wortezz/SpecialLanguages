from lab5.classes.shape3d import Shape3D

class Octahedron(Shape3D):
    def __init__(self, size):
        super().__init__(size)

    def project_to_2d(self):
        if self.size <= 0:
            raise ValueError("Розмір має бути додатнім числом.")
        projection_height = self.size * 2
        projection_width = self.size * 2
        projection = [[" " for _ in range(int(projection_width))] for _ in range(int(projection_height))]
        half = self.size // 2

        vertices = [
            (0, half, 0), (0, -half, 0),
            (half, 0, half), (-half, 0, half),
            (half, 0, -half), (-half, 0, -half),
        ]

        rotated_vertices = [self.apply_rotation(x, y, z) for x, y, z in vertices]

        edges = [
            (0, 2), (0, 3), (0, 4), (0, 5),
            (1, 2), (1, 3), (1, 4), (1, 5),
            (2, 3), (3, 4), (4, 5), (5, 2)
        ]

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
