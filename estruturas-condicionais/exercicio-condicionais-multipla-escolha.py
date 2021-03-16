'''
    - Escreva um algoritmo em Python que lê um nome e uma idade.
        - Caso o nome digitado seja Samuel, escreva isso na tela.
        - Caso o usuário digite qualquer outro nome, verifique sua idade. 
        Se for menor que 18 anos, informe que é de menor. Se for maior que 
        100 anos, informe que esta pessoa possivelmente não existe.
'''

nome = input('escreva seu nome : ')
nome_padrao = 'Samuel'

if (nome == nome_padrao):
    print('O nome digitado foi {}'.format(nome))
else:
    idade = int(input('Digite a sua Idade: '))

    if (idade < 18):
        print('{} é menor de idade'.format(nome))
    elif (idade > 100):
        print('{} possuí 100 anos ou mais, possivelmente essa pessoa não existe!'.format(nome))
    else:
        print('{} é maior de idade'.format(nome))

