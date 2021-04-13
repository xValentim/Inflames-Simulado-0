def calcula_extensao(x, y):
    distancia_total = 0
    i = 1 # Condição inicial do while
    while i < len(x):
        distancia_total += ((x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2) ** 0.5
        i += 1
    return distancia_total


'''def calcula_extensao(x, y):
    distancia_total = 0
    for i in range(1, len(x)):
        distancia_total += ((x[i] - x[i - 1])**2 + (y[i] - y[i - 1])**2)**0.5
    return distancia_total

def calcula_extensao(x, y):
    distancia_total = 0
    i = 0
    while i < len(x) - 1:
        distancia_total += ((x[i] - x[i + 1])**2 + (y[i] - y[i + 1])**2)**0.5
        i += 1
    return distancia_total'''