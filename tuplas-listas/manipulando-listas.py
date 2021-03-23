mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print('Lista :', mochila)  # Lista : ['Machado', 'Camisa', 'Bacon', 'Abacate']

mochila[2] = 'Laranja'
print('Lista :', mochila) #Lista : ['Machado', 'Camisa', 'Laranja', 'Abacate']

mochila.append('Ovos')
print('Lista :', mochila) # Lista : ['Machado', 'Camisa', 'Laranja', 'Abacate', 'Ovos']

mochila.insert(1, 'Canivete')
print('Lista :', mochila) # Lista : ['Machado', 'Canivete', 'Camisa', 'Laranja', 'Abacate', 'Ovos']

del mochila[1]
print('Lista :', mochila) # Lista : ['Machado', 'Camisa', 'Laranja', 'Abacate', 'Ovos']
mochila.remove('Ovos')
print('Lista :', mochila) # Lista : ['Machado', 'Camisa', 'Laranja', 'Abacate']
