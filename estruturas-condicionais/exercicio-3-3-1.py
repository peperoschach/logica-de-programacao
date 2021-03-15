'''
- Um aluno, para passar de anos, precisa ser aprovado em todas as 
  matérias que está cursando.

- Assuma que a média para aprovação é a partir de 7, e que o aluno 
  cursa 3 matérias, somente. Escreva um algoritmo que leia a nota final 
  do aluno em cada matéria e informe, na tela, se ele passou de ano ou não. 

- Fonte: Menezes, Nilo, p.60, adaptado
'''

#Exercício 3.3.1
media1 = float(input('Digite a nota da 1ª matéria: '))
media2 = float(input('Digite a nota da 2ª matéria: '))
media3 = float(input('Digite a nota da 3ª matéria: '))

if media1 >= 7 and media2 >= 7 and media3 >= 7:
    print('O aluno está aprovado de ano!')
else:
    print('O aluno não passou de ano!')