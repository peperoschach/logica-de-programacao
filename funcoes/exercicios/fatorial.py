def fatorial(num):
    """[Calcula a Fatorial]

    Args:
        num ([type]): [description]

    Returns:
        [type]: [description]
    """
    fat = 1
    if (num == 0):
        return fat

    for i in range(1, num+1, 1):
        fat *= i # fat = fat * i
    
    return fat


#Programa principal
x = int(input('Digite um valor para calcular a fatorial: -- '))
print('{}! = {}'.format(x, fatorial(x)))
help(fatorial)