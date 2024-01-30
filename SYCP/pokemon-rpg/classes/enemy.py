from random import choice
from classes.person import Person
from classes.pokemons_list import POKEMONS



class Enemy(Person):
    type = 'Enemy'

    def __init__(self, name=None, pokemons=[]):
        if pokemons:
            super().__init__(name=name, pokemons=pokemons)
        else:
            aleatory_pokemons = []
            for _ in range(2):
                aleatory_pokemons.append(choice(POKEMONS))
            super().__init__(name=name, pokemons=aleatory_pokemons)
        