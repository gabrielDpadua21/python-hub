from random import choice, randint
NAMES = ['Brok', 'Misty', 'Gary', 'John']

class Person:
    pokemon_choose = None
    money = 0

    def __init__(self, name=None, pokemons=[]) -> None:
        self.name = name if name else choice(NAMES)
        self.pokemons = pokemons


    def __str__(self) -> str:
        return f"Name: {self.name}"


    def catch(self, pokemon) -> None:
        self.pokemons.append(pokemon)
        print(f"{self.name} catch {pokemon.name} lvl {pokemon.level}")


    def pokemons_list(self) -> None:
        if self.pokemons:
            for index, pokemon in enumerate(self.pokemons):
                print(f"{index + 1} - {pokemon}")
        else:
            print(f"{self.name} not have pokemons!!!")
    

    def choose(self) -> None:
        print('________________________________________')
        print('Choice a pokemon')
        self.pokemons_list()
        print('________________________________________')
        while len(self.pokemons):
            try:
                option = int(input('Type the option: '))
                self.pokemon_choose = self.pokemons[(option - 1)]
                break
            except: 
                print('Wrong option, try again')


    def win_battle(self, value=1) -> None:
        self.money += value

    
    def report(self) -> None:
        print(f"Name: {self.name}")
        print(f"Pokemons: {len(self.pokemons)}")
        print(f"Money: {self.money}")


