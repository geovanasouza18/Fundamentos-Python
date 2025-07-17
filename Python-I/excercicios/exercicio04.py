name = 'Fifa'

character = name[0].lower()
new = name.replace(character, '#')
new = character +  new[1:]
print(new)
