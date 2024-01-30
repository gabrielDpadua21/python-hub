from random import choice, randint
from classes.person import Person
from classes.pokemons_list import POKEMONS

class Player(Person):
    type = "player"

    def battle(self, enemy) -> None:
        print(f"PokeBattle {self.name} VS {enemy.name}")
        self.choose()
        print('________________________________________')
        print(f"{self.name} chooses: {self.pokemon_choose}")
        enemy_choice = choice(enemy.pokemons)
        print(f"{enemy.name} chooses: {enemy_choice}")
        print("BATTLE")
        print(self.pokemon_choose.attack(enemy_choice))
        print(enemy_choice.attack(self.pokemon_choose))
        winner = randint(1, 2)
        if winner == 1:
            print(f"{self.pokemon_choose.name} win battle - {self.name} is the winner")
            self.win_battle(enemy_choice.level * 5)
        else:
            print(f"{enemy_choice.name} win battle - {enemy.name} is the winner")
            enemy.win_battle(self.pokemon_choose.level * 5)
        print('________________________________________')


    def to_explore(self) -> None:
        pokemon = choice(POKEMONS)
        print("You find a pokemon: ")
        print(pokemon)
        option = input("You want catch? y/n: ")
        if option == 'y':
            print("Lets try to catch!!!")
            print("throw pokeball")
            percent = randint(1, 2)
            if percent > 1:
                self.catch(pokemon)
                print(f"You catch: {pokemon.name}")
            else:
                print(f"Sorry, {pokemon.name} leave!!!")
        else:
            print(f"You freed: {pokemon}")