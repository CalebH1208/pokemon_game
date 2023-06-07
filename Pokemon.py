pokedex = [
    ["name", "type1", "type2"],
    ["Bulbasaur", "grass", "poison"],
    ["Ivysaur", "grass", "poison"],
    ["Venusaur", "grass", "poison"],
    ["Charmander", "fire", ""],
    ["Charmeleon", "fire", ""],
    ["Charizard", "fire", "flying"],
    ["Squirtle", "water", ""],
    ["Wartortle", "water", ""],
    ["Blastoise", "water", ""]

]


class move:
    def __init__(self, name, type, cat, power, accuracy):
        self.name = name
        self.type = type
        self.cat = cat
        self.pwr = power
        self.acc = accuracy

    def __str__(self):
        return self.name



class Pokemon:
    def __init__(self, dexnum, level, moveset):
        self.name = pokedex[dexnum][0]
        self.type1 = pokedex[dexnum][1]
        self.type2 = pokedex[dexnum][2]
        self.lvl = level
        self.moveset = moveset

    def __str__(self):
        return self.name + ", " + self.type1 + ", " + self.type2 + ", " + str(self.lvl)


Tackle = move("Tackle", "Normal", "physical", 40, 100)
Take_Down = move("Take_Down", "Normal", "physical", 90, 85)


class MoveSet:
    def __init__(self, move1, move2, move3, move4):
        self.Moveset = [move1, move2, move3, move4]

    def __str__(self):
        return (
            "Moves:\n1:" + str(self.Moveset[0]) + "     2:" + str(self.Moveset[1]) + "\n3:" + str(self.Moveset[2]) +
            "     4:" + str(self.Moveset[3]) + "\n")


jmoves = MoveSet(Tackle, Take_Down, Tackle, Take_Down)

jeremy = Pokemon(2, 84, jmoves)
print(jeremy)
print(Tackle)
print(jmoves)
print(434)
N = Pokemon(5, 34, [])
print(N)
