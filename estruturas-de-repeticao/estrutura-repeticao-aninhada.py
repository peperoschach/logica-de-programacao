'''
    - Escreva um algoritmo em Python que calcule a 
    tabuada de todos os números de 1 até 10, e, 
    para cada número, vamos calcular a tabuada 
    multiplicando-o pelo intervalo de 1 até 10

    - Vamos resolver no Python diferentes implementações
    2-while
    2-for
    while+for

'''

#2 While
print('UTILIZANDO 2 WHILE')

tabuada = 1
while (tabuada <= 10):
    print('\nTABUADA DO {}: '.format(tabuada))
    i = 1
    while (i <= 10):
        print('{} X {} = {}'.format(tabuada, i, tabuada * i))
        i += 1
    tabuada += 1

print('=========')


#2 for
print('UTILIZANDO 2 FOR')

for tabuada in range(1, 11, 1):
    print('\nTABUADA DO {}: '.format(tabuada))
    for i in range(1, 11, 1):
        print('{} X {} = {}'.format(tabuada, i, tabuada * i))

print('=========')

#while + for
print('UTILIZANDO WHILE + FOR')

tabuada = 1
while (tabuada <= 10):
    print('\nTABUADA DO {}: '.format(tabuada))
    for i in range(1, 11, 1):
        print('{} X {} = {}'.format(tabuada, i, tabuada * i))
    tabuada += 1
print('=========')
