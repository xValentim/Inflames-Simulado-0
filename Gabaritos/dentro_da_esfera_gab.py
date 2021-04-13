#Questão 1
#Simulado Inflames
#Gabarito

#Solução 1
import math
def alerta(coordenadas, raio):
    x = coordenadas[0]
    y = coordenadas[1]
    z = coordenadas[2]
    distancia = math.sqrt(x**2 + y**2 + z**2)
    if distancia < raio:
        return True
    else:
        return False

#Solução 2
#Sem usar o math
def alerta(coordenadas, raio):
    x = coordenadas[0]
    y = coordenadas[1]
    z = coordenadas[2]
    distancia = (x**2 + y**2 + z**2)**0.5
    if distancia < raio:
        return True
    else:
        return False

#Testes
print(alerta([0, 3, 4], 10)) #Saida: True
print(alerta([1, 1, 1], 1)) #Saida: False
print(alerta([0, 0, 10], 30)) #Saida: True
