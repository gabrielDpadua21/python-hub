from prettytable import PrettyTable


pokemons = ["Pikachu", "Squirtle", "Charmarder"]
types = ["Eletric", "Water", "Fire"]


table = PrettyTable()
table.add_column("Pokemon Name", pokemons)
table.add_column("Type", types)
table.align = "l"


print(table)