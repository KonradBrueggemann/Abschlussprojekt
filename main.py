# Abgabe für PRO I Prüfungsprojekt
# Konrad Brüggemann; 808632

from player import Player
from text_art import Texts
from config import *


# Command handling
def interface():
    """
    This method defines how the game reacts to the commands
    cmd is the user input
    usually there is a corresponding method that is run when the user makes a command
    """
    if cmd == "move right":
        try:
            player.move_right()
            if map1.get_room(player.location[0], player.location[1]).door_locked:
                if schluessel in player.inventory:
                    print("The door was locked but fortunately you had the key.")
                    map1.get_room(player.location[0], player.location[1]).open_door()
                else:
                    print("You need to acquire the key.")
                    player.move_left()

            print(f"You are now in {map1.get_room(player.location[0], player.location[1])}.")
        except:
            print("There is no room to your right.")
            player.move_left()
    elif cmd == "move left":
        try:
            player.move_left()
            if map1.get_room(player.location[0], player.location[1]).door_locked:
                if schluessel in player.inventory:
                    print("The door was locked but fortunately you had the key.")
                    map1.get_room(player.location[0], player.location[1]).open_door()
                else:
                    print("This room's door is locked. You need to acquire the key.")
                    player.move_right()
            print(f"You are now in {map1.get_room(player.location[0], player.location[1])}.")
        except:
            print("There is no room to your left.")
            player.move_right()
    elif cmd == "move up":
        try:
            player.move_up()
            if map1.get_room(player.location[0], player.location[1]).door_locked:
                if schluessel in player.inventory:
                    print("The door was locked but fortunately you had the key.")
                    map1.get_room(player.location[0], player.location[1]).open_door()
                else:
                    print("This room's door is locked. You need to acquire the key.")
                    player.move_down()
            print(f"You are now in {map1.get_room(player.location[0], player.location[1])}.")
        except:
            print("There is no room upwards.")
            player.move_down()
    elif cmd == "move down":
        try:
            player.move_down()
            if map1.get_room(player.location[0], player.location[1]).door_locked:
                if schluessel in player.inventory:
                    print("The door was locked but fortunately you had the key.")
                    map1.get_room(player.location[0], player.location[1]).open_door()
                else:
                    print("This room's door is locked. You need to acquire the key.")
                    player.move_up()
            print(f"You are now in {map1.get_room(player.location[0], player.location[1])}.")
        except:
            print("There is no room downwards.")
            player.move_up()
    elif cmd == "get location":
        print(location)
    elif cmd == "show map":
        print(map1)
    elif cmd == "stats":
        print(
            f"You currently have {', '.join(map(str, player.inventory))} in your inventory and you have {player.points} points.")
    elif cmd == "show objects":
        print(location.objects)
    elif cmd == "pick up":
        obj = input(f"Which object would you like to pick up?\n{location.objects}\n")
        if obj in str(location.objects):
            player.inventory.append(location.remove_object(obj))
            print(f"You successfully picked up the {obj}.")
        else:
            print("You can't pick this up.")
    elif cmd == "use":
        obj = input(f"Which object would you like to use?\n{player.inventory}\n")
        if obj in str(player.inventory):
            obj = object_map.get(obj)
            obj.use()
            obj.age()
            if not obj.multiple_usage:
                player.remove_object(obj)
    else:
        print("This command doesn't exist.")


if __name__ == "__main__":
    print(Texts.art)
    # Create Player
    # points decrease whenever the player moves so the higher the number is, the easier the game
    # it is suggested that the number of points is a little higher than the product of the width and height of the map
    player = Player(input("What's your name?\n"), [hammer, streichholz], 10)
    # per default the player starts in the top left corner of the map (defined in the init function of the player class)
    location = map1.get_room(player.location[0], player.location[1])
    print(Texts.welcome % (player.name, location, needed_object, Texts.commands))
    while True:
        if player.points > 0:
            cmd = input("\nEnter your command:\n")
            location = map1.get_room(player.location[0], player.location[1])
            interface()
            if needed_object in player.inventory:
                break
        else:
            exit("You have no points left and lost the game.")
    print("You won the game.")
