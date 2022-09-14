#!/usr/bin/python3
"""a square class"""


class Square:
    """Derives a square """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data
        Args:
            size (int): size of the square
            position (tuple): two positive integers
        Note:
            Do not include the `self` parameter in the ``Args`` section.
        Raises:
            TypeError: when `size` isn't an integer
            ValueError: `size` is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2 or not all(isinstance(v, int) for v in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def __str__(self):
        """Prints a square to stdout using `#`"""
        square = []
        if self.__size == 0:
            return ""

        [square.append("\n") for i in range(self.position[1])]
        for i in range(self.__size):
            for j in range(self.__position[0]):
                square.append(" ")
            for k in range(self.__size):
                square.append("#")
            if i < (self.__size - 1):
                square.append("\n")
        return "".join(square)

    def area(self):
        """Calculates the area of a square
        Returns: the area of the square
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieves the value of `size`"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of `size`

