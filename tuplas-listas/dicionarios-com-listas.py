games = {
    'nome': ['Super Mario', 'Zelda Ocarina of Time', 'Pokemon Yellow'],
    'videogame': ['Nintendo', 'Nintendo 64', 'Game Boy'],
        'ano': [1990, 1998, 1998]
    }


games = {'nome': [], 'videogame': [], 'ano': []}

for i in range(3):
    nome = input('Qual é o nome do jogo?    ')
    videogame = input('Para qual videogame ele foi lançado? ')
    ano = int(input('Qual é o ano de lançamento?    '))
    games['nome'].append(nome)
    games['videogame'].append(videogame)
    games['ano'].append(ano)
print('-' * 20)
print(games)
