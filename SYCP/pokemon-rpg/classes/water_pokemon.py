from random import randint
from classes.pokemon import Pokemon

class WaterPokemon(Pokemon):
    element = 'Water'

    def __init__(self, species, level=None, name=None):
        super().__init__(element=self.element, level=level, species=species, name=name)
    
    
    def attack(self, target) -> str:
        return f"{self.name} use Bubble Gun on {target.name}"