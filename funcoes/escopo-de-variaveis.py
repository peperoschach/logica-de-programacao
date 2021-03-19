def comida():
    ovos = 12

#Programa Principal
comida()
#print(ovos)

def comida2():
    print(ovos)

#Programa Principal
ovos = 12
comida2()

def comida3():
    ovos = 12
    bacon()
    print(ovos)

def bacon():
    ovos = 6

#Prograna Principal
comida3()

def comida4():
    ovos = 'Varável local de comida'
    print(ovos)

def bacon2():
    ovos = 'Variável local de bacon'
    print(ovos)
    comida4()
    print(ovos)


#Programa Principal
ovos = 'variável Global'
bacon2()
print(ovos)