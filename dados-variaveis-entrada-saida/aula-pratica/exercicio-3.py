""" Exercício 3 """

'''
Crie uma variável de string que receba uma variável qualquer.
Crie uma segunda variável, agora contendo a metade da string digitada.
Imprima na tela somente os dois últimos caracteres da segunda variável do ripo string
'''

frase = input('Digite uma frase: ')
tam = len(frase)

frase_2 = frase[int(tam/2):]

print(frase_2[-2:])
