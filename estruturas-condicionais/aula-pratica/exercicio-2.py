'''
    - Escreva um algoritmo que leia dois valores numéricos e que pergunte ao
    usuário qual operação ele deseja realizar: adição (+), subtração (-),
    multiplicação(*) ou divisão(/). Exiba na tela o resultado da operação desejada

'''

number1 = float(input('Digite um número: _ '))
number2 = float(input('Digite outro número: _ '))

operation = int(input('Digite um número referente a opeção desejada:\n 1- Adição(+)\n 2- Subtração(-) \n 3 - Multiplicação(*)\n 4 - Divisão(/)\n _ '))


if (operation == 1):
    print('Resultado =  {}'.format(number1 + number2))
elif (operation == 2):
    print('Resultado =  {}'.format(number1 - number2))
elif (operation == 3):
    print('Resultado =  {}'.format(number1 * number2))
elif (operation == 4):
    print('Resultado =  {}'.format(number1 / number2))
else:
    print('Operação inválida!')