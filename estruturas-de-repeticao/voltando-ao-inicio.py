'''
    - Escreva um algoritmo que realize um login em um
    sistema
    - O usuário deve informar seu nome e senha
'''

while True:
    nome = input('Digite seu usuário: ')
    if (nome != 'yoda'):
        continue
    senha = input('Digite sua senha: ')
    if (senha == '12345'):
        break
print('Bem vindo {}!'.format(nome))