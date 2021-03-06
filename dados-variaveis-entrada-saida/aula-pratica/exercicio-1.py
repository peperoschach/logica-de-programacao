""" Exercício 1 """

'''
Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele.
Calcule e exiba o valor do desconto e o preço final do produto (exercício da apostila - aula 2)

'''

preco = float(input('Digite o preço do produto : R$ '))
percentual_desconto = float(input('Digite a porcentagem de desconto: (0-100%) '))


desconto = preco * (percentual_desconto / 100)
final = preco - desconto

print('O preço do produto é R$ {}. Desconto de {}%'.format(preco, percentual_desconto))
print('Valor calculado de desconto: {}%. Valor final do Produto: R$ {}'.format(desconto, final))