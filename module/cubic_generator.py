import math
from module.square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def e_squares(self, start, end):
        if start > end:
            raise ValueError("Start is greater than end")

        cubes = [math.pow(x, 3) for x in range(start, end)]

        print("List of cubes from 1 to 10: ", cubes)

