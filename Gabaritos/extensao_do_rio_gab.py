#Questão 2
#PI 2020.2

#Solução 1
def calcula_extensão(x, y):
    total = 0
    for i in range(1, len(x)):
        total += ((x[i] - x[i - 1])**2 + (y[i] - y[i - 1])**2)**0.5
    return total

#Solução 2
import math
def calcula_extensao(x, y):
    i = 1
    d = 0
    while i < len(x):
        d += math.sqrt((x[i] - x[i - 1]) * (x[i] - x[i - 1]) + (y[i] - y[i - 1]) * (y[i] - y[i - 1]))
        i += 1
    return d


#Teste - Academia python