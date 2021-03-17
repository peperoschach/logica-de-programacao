# Estrutura de repetição while(enquanto)
x = 1
while (x <= 5):
    print(x)
    x = x + 1

# Voltando
x = 0
while (x <= 99):
    print(x)
    x = x +1
    
'''
x = 0
while (x < 99):
    print(x)
    x = x +1
'''

inicial = int(input('Digite o valor inicial da contagem: _ '))
final = int(input('Digite o valor final da contagem: _ '))
x = inicial
while (x <= final):
    if (x % 2 == 0):
        print(x)
    x = x + 1


soma = 0
cont = 1
while (cont <= 5):
    x = float(input('Digite a {}ª nota: _'.format(cont)))
    soma = soma + x
    cont = cont + 1
media = soma / 5
print('Média final: {}'.format(media))