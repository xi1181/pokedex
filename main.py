from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["#", "Pokemon Name", "Type"]
table.add_row(["001", "Bulbasaur", "Grass/Poison"])
table.add_row(["002", "Ivysaur", "Grass/Poison"])
table.add_row(["003", "Venusaur", "Grass/Poison"])
table.add_row(["004", "Charmander", "Fire"])
table.add_row(["005", "Charmeleon", "Fire"])
table.add_row(["006", "Charizard", "Fire/Flying"])
print(table)
