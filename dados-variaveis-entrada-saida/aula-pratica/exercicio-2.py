""" Exercício 2 """

'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado pelo usuário, assim como a quantidade
de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60.00 por dia
e R$ 0.15 por Km rodado.
'''

km_rodados = float(input('Digite a quantidade de Km percorridos: '))
dias_alugados = int(input('Digite a quantidade de dias pelas quais o carro foi alugado: '))
valor_total_km = km_rodados * 0.15
valor_total_dias_alugados = dias_alugados * 60
valor_final = valor_total_km + valor_total_dias_alugados

print('O valor total pelos KM rodados é de R$ {}'.format(valor_total_km))
print('O valor total pelos dias alugados é de R$ {}'.format(valor_total_dias_alugados))
print('O valor total do aluguel é de R$ {}'.format(valor_final))