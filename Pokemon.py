pokedex=[
    ["name","type1","type2"],
    ["Bulbasaur","grass","poison"],
    ["Ivysaur","grass","poison"],
    ["Venusaur","grass","poison"],
    ["Charmander","fire","" ],
    ["Charmeleon","fire",""],
    ["Charizard","fire","flying"],
    ["Squirtle","water",""],
    ["Wartortle","water",""],
    ["Blastoise","water",""]


]
class move:
    def __init__(self,name,type,cat,power,accuracy):
        self.name=name
        self.type=type
        self.cat=cat
        self.pwr=power
        self.acc=accuracy
    def __str__(self):

        return(self.name)


class Pokemon:
    def __init__(self,dexnum,level,moveset):
        self.name=pokedex[dexnum][0]
        self.type1=pokedex[dexnum][1]
        self.type2=pokedex[dexnum][2]
        self.lvl=level
        self.moveset=moveset

    def __str__(self):
        return (self.name+", "+self.type1+", "+self.type2+", "+str(self.lvl))

jmoves=[
    move("Tackle","Normal","physical",40,100),
    move("Take Down","Normal","physical",90,85)

]


jeremy = Pokemon(2, 84,jmoves)
print(jeremy)
print(jeremy.moveset)
N = Pokemon(5,34,[])
print(N)
