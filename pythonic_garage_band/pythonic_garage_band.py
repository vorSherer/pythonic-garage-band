
class Band:
    '''
    This class instantiates band instances.
    '''

    band_list = []
# A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.band_list.append(self)

# A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
    def play_solos(self, name):
        return [play_solo for member in self.members]
        
    def __str__(self):
        return f"Band(name: {self.name}, members: {self.members})"

    def __repr__(self):
        return f"'name' : {self.name}, 'members' : {self.members}"


class Musician:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return {self.name}

    def __repr__(self):
        return f'Musician {self.name}'


class Guitarist(Musician):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name's {self.name}, I play guitar"    

    def __repr__(self):
        return f"Guitarist, {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "power riff"


class Bassist(Musician):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name's {self.name}, I play bass"    

    def __repr__(self):
        return f"Bassist, {self.name}"

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bumpin' bottom beatz"




class Drummer(Musician):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name's {self.name}, I play drums"    

    def __repr__(self):
        return f"Drummer, {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "Dada-Dada-Dada BOOM! Crash!"







if __name__ == "__main__":
    toby = Guitarist('Toby')
    eddie = Bassist('Eddie')
    ox = Drummer('Ox')
    band1 = (Band("Flying Penguins", [toby, eddie, ox]))
    for member in band1.members:
        print("Member: ", member)
        print("Name: ", member.name)
    print(band1.band_list)

    # print(band1)
    # ax1 = Guitarist("Toby")
    # print(ax1)
    # bot1 = Bassist("Eddie")
    # print(bot1)
    # beat1 = Drummer("Ox")
    # print(beat1)

