'''
-Dentro da esfera
Imagine uma esfera de raio 'r' cujo centro dela se encontra na posição (0, 0, 0) 
ou seja, na origem dos eixos (x, y, z).

Como medida de proteção aérea, o piloto de um avião localizado no centro da esfera deve
ficar em estado de alerta caso algum objeto se encontre dentro dessa esfera de raio 'r'.

Dessa forma, faça uma função que recebe uma lista com as posições x, y e z de um objeto, 
o raio da esfera e retorna True se o pilote precisa ficar alerta e False se ele estiver seguro.

OBS.: Considere que a casca é da parte de dentro da esfera.

Sua função deve se chamar alerta.

Exemplos:
Entrada: ([0, 3, 4], 10)
Saída: True

Entrada: ([1, 1, 1], 1)
Saída: False

Entrada: ([0, 0, 10], 30)
Saída: True

Entrada: ([0, 0, 1], 1)
Saída: True

'''

def alerta(coordenadas, raio):
    x = coordenadas[0]
    y = coordenadas[1]
    z = coordenadas[2]
    distancia = (x * x + y * y + z * z) ** 0.5
    if distancia <= raio:
        return True
    else:
        return False

#Testes:
print(alerta([0, 3, 4], 10))
print(alerta([1, 1, 1], 1))
print(alerta([0, 0, 10], 30))
print(alerta([0, 0, 1], 1))
