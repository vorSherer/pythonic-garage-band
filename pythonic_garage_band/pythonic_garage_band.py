class Band:

# A Band instance should have a name attribute which is a string.
# A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
    def __init__(self, name):
        self.name = name
        self.members = []

# A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
    def play_solos(self):
        pass


# STRETCH:  A Band should have a class method to_list which returns a list of previously created Band instances
    # def to_list(self):
    #     pass


# A Band instance should have appropriate __str__ and __repr__ methods.
    def __str__(self):
        return f"Name: {self.name}, members: {self.members}"

    def __repr__(self):
        return {'name' : self.name, 'members' : self.members}


class Musician:
    pass


class Guitarist(Musician):
    pass


class Bassist(Musician):
    pass


class Drummer(Musician):
    pass



