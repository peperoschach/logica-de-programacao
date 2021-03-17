'''
    - Faça um algoritmo que receba três valores, representando os lados
    de um triângulo fornecidos pelo usuário. Verifique se os valores formam 
    um trriângulo e classifique como:
    a) Equilátero (Três lados iguais)
    b) Isósceles (dois lados iguais)
    c) Escaleno (três lados diferentes)

    - Lembre-se de que, para formar um triângulo, nenhum dos lados pode ser
    igual a zero, e um lado não pode ser maior do que a soma dos outros dois.
'''

lado_a = float(input('Digite o lado A _'))
lado_b = float(input('Digite o lado B _'))
lado_c = float(input('Digite o lado C _'))

if ((lado_a > 0) and (lado_b > 0) and (lado_c > 0)):
    if ((lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a)):
        #Escaleno
        if ((lado_a != lado_b) and (lado_a != lado_c)):
            print('Triângulo Escaleno!')
        else:
            #Equilátero
            if ((lado_a == lado_b) and (lado_a == lado_c)):
                print('Triângulo Equilátero!')
            else:
                #Isósceles
                print('Triângulo Isósceles')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo')

