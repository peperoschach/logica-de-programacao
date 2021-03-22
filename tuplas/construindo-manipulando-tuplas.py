mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')

print(mochila)  # ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila[0]) # Machado
print(mochila[2]) # Bacon
print(mochila[0:2])  # ('Machado', 'Camisa')
print(mochila[2:])  # ('Bacon', 'Abacate')
print(mochila[-1]) # Abacate

# mochila[2] = 'Ovos'

for item in mochila:
    print('Na minha mochila tem: {}'.format(item))

tam = len(mochila)
for i in range (0, tam, 1):
    print('Na minha mochila tem: {}'.format(mochila[i]))

'''
    Na minha mochila tem: Machado
    Na minha mochila tem: Camisa
    Na minha mochila tem: Bacon
    Na minha mochila tem: Abacate
'''

upgrade = ('Queijo', 'Canivete')
mochila_grande = mochila + upgrade

print(mochila)  # ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(upgrade)  # ('Queijo', 'Canivete')
print(mochila_grande) # ('Machado', 'Camisa', 'Bacon', 'Abacate', 'Queijo', 'Canivete')


mochila_grande_invertida = upgrade + mochila

print(mochila_grande) #('Machado', 'Camisa', 'Bacon', 'Abacate', 'Queijo', 'Canivete')
print(mochila_grande_invertida) #('Queijo', 'Canivete', 'Machado', 'Camisa', 'Bacon', 'Abacate')
