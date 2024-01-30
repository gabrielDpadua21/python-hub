from classes.pokemon import Pokemon
from random import randint

class FirePokemon(Pokemon):
    element = 'Fire'

    def __init__(self, species, level=None, name=None):
        super().__init__(element=self.element, level=level, species=species, name=name)
    
    
    def attack(self, target) -> str:
        return f"{self.name} use fire ball on {target.name}"