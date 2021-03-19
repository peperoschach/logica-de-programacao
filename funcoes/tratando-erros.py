while True:
    try:
        x = int(input('Por favor digite um número: '))
        break
    except ValueError:
        print('Oops! Número inválido. Tente novamente... ')

def div():
    try:
        num1 = int(input('Digite um número: _ '))
        num2 = int(input('Digite um número: _ '))
        res = num1 / num2
    except ZeroDivisionError:
        print('Opps! Erro de divisão por zero ....')
    except:
        print('Algo de errado aconteceu...')
    else:
        return res
    finally:
        print('Executará sempre!')

#Programa Principal
print(div())
        