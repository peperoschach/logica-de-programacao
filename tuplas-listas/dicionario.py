game = {
        'nome': 'Super Mario',
        'desenvolvedora': 'Nintendo',
        'ano': 1990
        }

print(game)


print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])


print(game.values())  # dict_values(['Super Mario', 'Nintendo', 1990])

for i in game.values():
    print(i)

print(game.keys())  # dict_keys(['nome', 'desenvolvedora', 'ano'])

for i in game.keys():
    print(i)

print(game.items())  # dict_items([('nome', 'Super Mario'), ('desenvolvedora', 'Nintendo'), ('ano', 1990)])

for i, j in game.items():
    print('{} = {}'.format(i, j))


