#Questão 2
#Simulado Inflames
#Gabarito

#Solução 1
def calcula_cm(coordenadas_x, coordenadas_y):
    if coordenadas_x == [] and coordenadas_y == []:
        return []
    else:
        soma_x = 0
        soma_y = 0
        n = len(coordenadas_x)
        i = 0
        while i < n:
            soma_x += coordenadas_x[i]
            soma_y += coordenadas_y[i]
            i += 1
        media_x = soma_x / n
        media_y = soma_y / n
        return [media_x, media_y]

#Solução 2
def calcula_cm(coordenadas_x, coordenadas_y):
    if coordenadas_x == [] and coordenadas_y == []:
        return []
    else:
        soma_x = 0
        soma_y = 0
        n = len(coordenadas_y)
        for xi, yi in zip(coordenadas_x, coordenadas_y):
            soma_x += xi
            soma_y += yi
        media_x = soma_x / n
        media_y = soma_y / n
        return [media_x, media_y]

#Solução 3
def calcula_cm(coordenadas_x, coordenadas_y):
    if coordenadas_x == [] and coordenadas_y == []:
        return []
    else:
        soma_x = 0
        soma_y = 0
        n = len(coordenadas_y)
        for xi, yi in zip(coordenadas_x, coordenadas_y):
            soma_x += xi
            soma_y += yi
        media_x = soma_x / n
        media_y = soma_y / n
        return [media_x, media_y]

#Solução 4
def calcula_cm(coordenadas_x, coordenadas_y):
    if coordenadas_x == [] and coordenadas_y == []:
        return []
    else:
        soma_x = 0
        soma_y = 0
        n = len(coordenadas_x)
        for i in range(n):
            soma_x += coordenadas_x[i]
            soma_y += coordenadas_y[i]
        media_x = soma_x / n
        media_y = soma_y / n
        return [media_x, media_y]

#Solução 5
def calcula_cm(coordenadas_x, coordenadas_y):
    if coordenadas_x != [] and coordenadas_y != []:
        n = len(coordenadas_x) #Poderia ser len(coordenadas_y), elas tem o mesmo tamanho
        soma_x = sum(coordenadas_x)
        soma_y = sum(coordenadas_y)
        media_x = soma_x / n
        media_y = soma_y / n
        return [media_x, media_y]
    else:
        return []

#Solução 6 (ideal para a prova)
def calcula_cm(coordenadas_x, coordenadas_y):
    if coordenadas_x != [] and coordenadas_y != []:
        media_x = sum(coordenadas_x) / len(coordenadas_x)
        media_y = sum(coordenadas_y) / len(coordenadas_y)
        return [media_x, media_y]
    else:
        return []

#Solução 7 (ideal para a prova)
def calcula_cm(coordenadas_x, coordenadas_y):
    if coordenadas_x != [] and coordenadas_y != []:
        return [sum(coordenadas_x) / len(coordenadas_x), sum(coordenadas_y) / len(coordenadas_y)]
    else:
        return []


#Testes
lista_x = [1, 1, 1, 1]
lista_y = [0, 0, 0, 0]
print(calcula_cm(lista_x, lista_y)) #Saída: [1.0, 0.0]
lista_x = [15, 20, 25]
lista_y = [0, 1, 14]
print(calcula_cm(lista_x, lista_y)) #Saída: [20.0, 5.0]
lista_x = []
lista_y = []
print(calcula_cm(lista_x, lista_y)) #Saída: []
