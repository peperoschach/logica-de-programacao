'''
    - Escreva uma função para validar uma string. Essa função recebe 
    como parâmetro a string, o número mínimo e máximo de caracteres.
    Retorne verdadeiro se o tamanho da string estiver entre os valores 
    de mínimo e máximo, e falso, caso contrário (elaborado com base em Menezes, s. d.) 

'''

def valida_string(pergunta, minimo, maximo):
    s1 = input(pergunta)
    tam = len(s1)
    while((tam < minimo) or (tam > maximo)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1


#Programa Principal
x = valida_string('Digite uma string: ', 10, 30)
print('Você digitou a string: {}. \nDado válido. \nEncerrando o Programa...'.format(x))