# Room Klasse
from object import Object


class Room:

    def __init__(self, name, objects=[], door_locked=False):
        self.name = name
        self.objects = objects
        self.door_locked = door_locked

    def remove_object(self, object):
        """
        this method removes a given object from the room
        its used whenever the user picks up an object and transfers it into his inventory
        """
        for i in range(len(self.objects)):
            if repr(self.objects[i]) == object:
                return self.objects.pop(i)

    def __repr__(self):
        """
        rooms are represented by their name
        """
        return self.name

    def open_door(self):
        self.door_locked = False
