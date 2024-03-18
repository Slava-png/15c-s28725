import math
# =================== THIRD TASK ===================


class SquareGenerator:
    def e_squares(self, start, end):
        squares = [math.pow(x, 2) for x in range(start, end)]

        print("List of squares from 1 to 10: ", squares)


SquareGenerator().e_squares(1, 10)
