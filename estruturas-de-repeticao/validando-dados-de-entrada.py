'''
    - Crie um algoritmo que receba um valor do tipo inteiro via teclado

    - No entanto, o programa só deve aceitar, obrigatoriamente,valores 
    inteiros e positivos

    - Qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo 
    programa e um novo valor deve ser solicitado
'''

# Validando a entrada
x = int(input('Digite um valor maior que zero: _ '))

while (x <= 0):
    x = int(input('Digite um valor maior que zero: _'))
print('Você digitou {}. Encerrando o programa'.format(x))

