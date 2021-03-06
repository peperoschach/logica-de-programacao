""" Função de entrada """

idade = input('Qual a sua idade?')
print(idade)

nome = input('Qual o seu nome? ')
print('Olá {}, seja bem-vindo!'.format(nome))

""" Convertendo dados de entrada """

nota = float(input('Qual nota você recebeu na disciplina? '))
print('Você tirou nota {}.'.format(nota))

""" Exercício """

#Exercício 2.1
""" Desenvolva um algoritmo que solicite ao usuário dois números inteiros.
Imprima a soma destes dois números na tela """

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
soma = numero_1 + numero_2
print('A soma de {} + {} é {}'.format(numero_1, numero_1, soma))