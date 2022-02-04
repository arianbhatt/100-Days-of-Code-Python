from prettytable import PrettyTable

table=PrettyTable()

# Method to add_column
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charizard","Geodude","Psyduck"])
table.add_column("Pokemon Type",["Electric","Water","Fire","Rock","Psychic"])
# aligning the table 'l' or 'r' 
#table.align='r'
table.align='l'
print(table)
