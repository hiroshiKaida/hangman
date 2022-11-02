"""Add a class valiable to a class.

Created on Tue Oct 11 13:10:46 2022

@author: hiroshi
"""


class Square:
    """The class has a class variable."""

    square_list = []

    def __init__(self, side):
        """Initialize the object with a instance variable.

        Instace variables
        ----------
        side : Float with the unit of cm
            Each side of the square.

        Returns
        -------
        None.

        """
        self.side = side
        print(f"create {self.side}cm by {self.side}cm of a square.")
        self.square_list.append(self.side)


square_one = Square(10)
square_two = Square(11)
square_three = Square(12)
print(Square.square_list)
