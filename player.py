# Player Klasse

class Player:
    def __init__(self, name, inventory, points, location=[0, 0]):
        self.name = name
        self.inventory = inventory
        self.points = points
        self.location = location

    def get_inventory(self):
        return self.inventory

    def get_points(self):
        return self.points

    # the map is a matrix so moving to the right increases the second coordinate by 1, moving to the left decreases it
    # moving up or down changes the first coordinate by 1

    def move_right(self):
        self.points -= 1
        self.location[1] += 1

    def move_left(self):
        self.points -= 1
        self.location[1] -= 1

    def move_up(self):
        self.points -= 1
        self.location[0] -= 1

    def move_down(self):
        self.points -= 1
        self.location[0] += 1

    def remove_object(self, object):
        """
        removes an object from the users inventory, eg. if he used a single use object
        """
        self.inventory.remove(object)


