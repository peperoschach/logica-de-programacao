'''
    - Escreva um programa que calcule o preço a pagar pelo
    fornecimento de energia elétrica. Pergunte a quantidade 
    de kWh consumida e o tipo de instalação: 
    R - residencial
    I - Industrial
    C - Comercios
'''

kwh = float(input('Por favor digite a quantidade de kWh gastos: _ '))
tipo = input('Digite o tipo de instalação:\n  R - residencial\n I - Industrial\n C - Comercios\n __ ')


if (tipo == 'R'):
    if (kwh <= 500):
        preco = 0.40
    else:
        preco = 0.65
elif (tipo == 'I'):
    if (kwh <= 1000):
        preco = 0.55
    else:
        preco = 0.60
elif (tipo == 'C'):
    if (kwh <= 5000):
        preco = 0.55
    else:
        preco = 0.60
else:
    print('Opção inválida!')

print('O valor total da sua fatura de energia elétrica é de R$ {}'.format(kwh * preco))