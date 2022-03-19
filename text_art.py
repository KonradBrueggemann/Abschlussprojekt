class Texts:
    art = """
____ _  _ ____ ____ ___  ____ ____ _  _ ____
[__  |\ | |___ |___ |  \ | __ |__| |\/| |___
___] | \| |___ |___ |__/ |__] |  | |  | |___

"""
    welcome = "----- Welcome, %s! -----\n" \
              "You are currently at the %s in the top left corner of the map.\n" \
              "To win the game, you need to acquire this item: %s\n" \
              "To control the player, make use of the following commands:\n%s"

    commands = "Move your player by using 'move right', 'move up', etc\n" \
               "Whenever you move, you lose one point. Once your points reach 0 you lost.\n" \
               "'show map' displays the map and 'get location' tells you where you're at.\n" \
               "'pick up' lets you pick up objects that are inside the room you're currently in.\n" \
               "'stats' shows you your current inventory and how many points you have left."
