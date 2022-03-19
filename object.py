# Object Klasse


class Object:
    def __init__(self, name, condition, multiple_usage):
        self.name = name
        self.condition = condition
        self.multiple_usage = multiple_usage

    def use(self):
        if self.multiple_usage:
            print(f"You used {self.name}. You can use it again.")
        else:
            print(f"You used {self.name}. You can not reuse it.")

    def age(self):
        if self.condition == "new" and self.multiple_usage:
            self.condition = "used"

    def __repr__(self):
        """
        objects are represented by their name
        """
        return self.name
