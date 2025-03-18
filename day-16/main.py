# import turtle
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "fire"])
table.add_row(["Pikachu", "fire"])
table.add_row(["Pikachu", "fire"])


print(table)