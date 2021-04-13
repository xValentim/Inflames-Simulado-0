#Questão 1
#PI 2020.2

#Solução 1
import math
def will_it_float(p, R, r):
    volume = 2 * math.pi * math.pi * R * r * r 
    densidade = (p * 1000) / volume
    if densidade <= 0.997:
        return True
    else:
        return False

#Solução 2
import math
def will_it_float(p, R, r):
    if (p * 1000) / (2 * math.pi * math.pi * R * r * r) <= 0.997:
        return True
    else:
        return False


#Teste - Academia python