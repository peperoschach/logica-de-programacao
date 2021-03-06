""" Concatenação de String """

concat_string = 'Lógica de Programação'
concat_string = concat_string + ' e Algoritmos!'
print(concat_string) #Lógica de Programação e Algoritmos!

# Repetindo strings na concatenação
concat_string = 'A' + '-' * 10 + 'B'
print(concat_string)  #A----------B

""" Composição """
nota = 8.5
resultado = 'Você tirou %f na disciplina de Algoritmos!' % nota
print(resultado)  #Você tirou 8.500000 na disciplina de Algoritmos!

#Limitando as casas decimais
nota = 7.5
resultado = 'Você tirou %.2f na disciplina de Algoritmos!' % nota
print(resultado)  #Você tirou 7.50 na disciplina de Algoritmos!


#Várias variáveis
nota = 8.5
disciplina = 'Algoritmos'
resultado = 'Você tirou %.2f na disciplina de %s!' % (nota, disciplina)
print(resultado)  #Você tirou 8.50 na disciplina de Algoritmos!

#Composição Mais Mdoerna
nota = 9.5
disciplina = 'Algoritmos'
resultado = 'Você tirou {} na disciplina de {}!'.format(nota, disciplina)
print(resultado)  #Você tirou 9.5 na disciplina de Algoritmos!


""" Fatiamento """

minha_string = 'Lógica de Programação e Algoritmos!'
print(minha_string[0:6]) #Lógica
print(minha_string[24:34]) #Algoritmos
print(minha_string[:6]) #Lógica

""" Tamanho (length) """
minha_string = 'Lógica de Programação e Algoritmos!'
tamanho = len(minha_string)
print(tamanho) #35