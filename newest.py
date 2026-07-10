from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon", "Type", "Country"]
# table.add_column("Pokemon", ["pikkachu", "bublbasaur", "charmander"])
# table.add_column("Type", ["electric", "grass", "fire"])
# table.add_column("Country" ,["QUWAIT", "IRAN", "DUBAI"])

# table.add_row(["pilachu", "electric" , "QUWAIT"])
table.add_row(["bulbasaur", "grass" , "IRAN"])
table.add_row(["charmander", "fire" , "DUBAI"])
print(table)

# table.align = "r"
# print(table)
# about dictionaries!
# set = {"lion":"Lion is a wild animal",
#        "tiger":"Tiger is a fierce predator",
#        "elephant":"Elephant is the largest land animal"}
# set["lion"] = "Lion belongs to the cat family !!!"
# set["fox"]= "Fox is a clever animal"


# set={}