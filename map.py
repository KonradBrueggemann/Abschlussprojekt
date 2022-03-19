# Map Klasse
import random
class Map:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        """
        displays the map in 2d format
        """
        return '\n'.join([str(i) for i in self.matrix])

    def get_room(self, x, y):
        """
        returns the name of the room at a given set of variables
        """
        return self.matrix[x][y]

    def set_room(self, x, y, room):
        """
        this method is used if the user of the framework wants to assign rooms to the map manually
        x and y are the coordinates of the room inside the matrix
        """
        self.matrix[x][y] = room

    def autofill(self, height, width, rooms):
        """
        This method assigns the select rooms automatically to the map
        """
        n = 0
        while n < height:
            for m in range(0, width):
                self.set_room(n, m, random.choice(rooms))
            n += 1


