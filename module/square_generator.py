import math


class SquareGenerator:
    def e_squares(self, start, end):
        if start > end:
            raise ValueError("Start is greater than end")

        squares = [math.pow(x, 2) for x in range(start, end)]

        print("List of squares from 1 to 10: ", squares)
