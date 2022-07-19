#!/usr/bin/python3

class Square:
    '''class Square that defines a square'''

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if(len(value) != 2 and not isinstance(value, tuple)
                and not all(isinstance(v, int) for v in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if(self.__size == 0):
            print(" ")
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                print("#"*self.__size)
