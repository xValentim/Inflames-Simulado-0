import math
def will_it_float(p, R, r):
    volume = 2 * (math.pi ** 2) * R * (r ** 2)
    d = (p * 1000) / volume
    if d <= 0.997:
        return True
    else:
        return False


'''#from math import *
import math
def will_it_float(p, R, r):
    # Calcula volume
    volume = 2 * math.pi * math.pi * R * r * r 
    # Calcula densidade
    densidade = (p * 1000) / volume
    # Checa condições
    if densidade <= 0.997:
        return True
    else:
        return False

print('Olá')
print('Tudo bem?')
print('Tchau')
variavel = will_it_float(1000, 10, 10)
print(variavel)

#Testes no academia python'''