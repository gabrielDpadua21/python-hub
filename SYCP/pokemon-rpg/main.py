from classes.eletric_pokemon import EletricPokemon
from classes.fire_pokemon import FirePokemon
from classes.water_pokemon import WaterPokemon
from classes.wind_pokemon import WindPokemon
import pickle
from classes.player import Player
from classes.enemy import Enemy
from assets.banner import art
import os

first_catch = {
    "1": WindPokemon("Bulbassauro", 1),
    "2": FirePokemon("Charmarder", 1),
    "3": WaterPokemon("Squardle", 1)
}

def save_game(player):
    try:
        with open("database.db", "wb") as file:
            pickle.dump(player, file)
            print("Game saved!!!")
    except:
        print("Error to save the game")

def load_game():
    try:
        with open("database.db", "rb") as file:
            player = pickle.load(file)
            return player
    except:
        print("Error to load the game")


def init_game(player):
    print("------------------------------------------------------------------------------")
    print(f"Hello {player.name}, i am professor rocket!")
    print("Choose your first Pokemon: ")
    print("1 - Bulbassauro - lvl 1")
    print("2 - Charmarder - lvl 1")
    print("3 - Squardle - lvl 1")
    while True:
        try:
            option = input("Type the pokemon choose: ")
            first_pokemon = first_catch[option]
            player.catch(first_pokemon)
            break
        except:
            print("Wrong option, try again!!!")
    print("Great now you are ready to start your jorney!")
    print("------------------------------------------------------------------------------")


def gameplay():
    print("------------------------------------------------------------------------------")
    print(" 1 - New game")
    if os.path.exists('database.db'):
        print(" 2 - Load game")
    game_option = int(input("Select one option: "))
    print("------------------------------------------------------------------------------")

    if game_option == 1:
        player_name = input('Type your name: ')
        player = Player(player_name)
        init_game(player)
    else:
        player = load_game()

    print("Lets start: what do you want to do?")
    while True:
        print("------------------------------------------------------------------------------")
        print("1 - To explore")
        print("2 - Battle")
        print("3 - Pokemons list")
        print("4 - Player Status")
        print("5 - Save Game")
        print("0 - Exit")
        print("------------------------------------------------------------------------------")
        try:
            option = int(input("Type one option: "))
            if option < 1 or option > 5:
                print("Bye")
                break
            elif option == 1:
                player.to_explore()
            elif option == 2:
                enemy = Enemy()
                player.battle(enemy)
            elif option == 3:
                print("You pokemons list: ")
                player.pokemons_list()
            elif option == 4:
                player.report()
            else:
                save_game(player)
        except:
            print("Wrong option, try again")


if __name__ == '__main__':
    print(art)
    print('Welcome to Pokemon RPG')
    gameplay()

