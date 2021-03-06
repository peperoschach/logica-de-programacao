""" Strings """

'''
Execute as seguintes atribuições:
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
'''

s1 = 'ant'

s2 = 'bat'

s3 = 'cod'


'''
Agora, utilizando operadores + e *, crie as saídas a seguir:

a) 'ant bat cod'
b) 'ant ant ant ant ant ant ant ant ant ant' 
c) 'ant bat bat cod cod cod'
d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
e) 'batbatcod batbatcod batbatcod batbatcod batbatcod'
'''

#A
print(s1 + ' ' + s2 + ' ' + s3)

#B
print((s1 + ' ') * 10)

#C
print((s1 + ' ') + (s2 + ' ') * 2 + (s3 + ' ') * 3)

#D
print(((s1 + ' ') + (s2 + ' ')) * 7)

#E
print(((s2 * 2)+ s3 + ' ') * 5 )
