import PokemonBasics
import pypokedex

jerry= PokemonBasics.Pokemon(7,100,[])
print(jerry)
jerryhealth =int(pypokedex.get(dex=7).base_stats.hp*2*jerry.lvl/100+jerry.lvl+10)
print(jerryhealth)
def CalcHeath(Mon):
    return int(pypokedex.get(dex=Mon.dexnum).base_stats.hp*2*Mon.lvl/100+Mon.lvl+10)


print(CalcHeath(jerry))
print(pypokedex.get(dex=7).types)