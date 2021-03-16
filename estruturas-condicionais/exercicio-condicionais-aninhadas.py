'''
    - Escreva um algoritmo em Python em que o usuário escolhe se quer comprar maçãs,
    laranjas ou bananas. Deverá ser apresentado na tela um mneu com as opções:
    1 - maçã
    2 - laranja
    3 - banana.
    
    - Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O algoritmo
    deve calcular o preço total a pagar do produto escolhido e mostrá-lo na tela.

    - Considere os custos:
    maçã    - R$ 2,30
    laranja - R$ 3,60
    banana  - R$ 1,85
'''

print('Escolha o que deseja comprar: ')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha? - '))
preco_maca = 2.3
preco_laranja = 3.60
preco_banana = 1.85

if ((produto == 1) or (produto == 2) or (produto == 3)):

    quantidade = int(input('Quantas unidades? - '))

    if (produto == 1):
        pagar = quantidade * preco_maca
        print('Você comprou {} maçãs. Total à pagar: {}'.format(quantidade, pagar))
    else:
        if (produto == 2):
            pagar = quantidade * preco_laranja
            print('Você comprou {} laranjas. Total à pagar: {}'.format(quantidade, pagar))
        else:
            if (produto == 3):
                pagar = quantidade * preco_banana
                print('Você comprou {} bananas. Total à pagar: {}'.format(quantidade, pagar))
else:
    print('O produto selecionado não existe!')
