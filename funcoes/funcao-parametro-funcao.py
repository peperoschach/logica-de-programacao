def imprime_com_condicao(num, fcond):
    if fcond(num):
        print(num)

def par(x):
    return x % 2 == 0

def impar(x):
    return not par(x)

#Programa Principal
imprime_com_condicao(5, par)
imprime_com_condicao(5, impar)