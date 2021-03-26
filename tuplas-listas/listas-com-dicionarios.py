games = []

game1 = {
    'nome': 'Super Mario',
    'videogame': 'Nintendo',
    'ano': 1990
    }

game2 = {
    'nome': 'Zelda Ocarina of Time',
    'videogame': 'Nintendo 64',
    'ano': 1998
    }

game3 = {
    'nome': 'Pokemon Yellow',
    'videogame': 'Game Boy',
    'ano': 1999
    }


games1 = [game1, game2, game3]
print(games1)

game = {}
games = []
for i in range(3):
    game['nome'] = input('Qual é o nome do jogo?    ')
    game['videogame'] = input('Para qual videogame ele foi lançado? ')
    game['ano'] = int(input('Qual é o ano de lançamento?    '))
    games.append(game.copy())
print('-' * 20)

for e in games:
    for i,j in e.items():
        print('O campo {} tem o valor {}.'.format(i,j))