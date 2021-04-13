'''
-Centro de massa
Para calcular o centro de massa de objetos pontuais de massas iguais em posições
(xi, yi) no plano cartesiano, basta fazermos a média aritmética nos dois eixos:

xcm = (x1 + x2 + ... + xn) / n
ycm = (y1 + y2 + ... + yn) / n

Imagine um plano cartesiano que nele contém "n" objetos de massas iguais, respectivamente,
com as posições (x1, y1), (x2, y2), (x3, y3), ..., (xn, yn).

Faça uma função que recebe duas lista,
A primeira lista guarda todos os valores de x: [x1, x2, ..., xn]
A segunda lista guarda todos os valores de y: [y1, y2, ..., yn]
,
e devolve uma lista de dois valores, respectivamente xcm e ycm: [xcm, ycm].

Sua função deve se chamar calcula_cm.

OBS.: As listas sempre têm tamanhos iguais e caso a função receba listas vazias, devolva [].

Exemplos,

Entrada: [1, 1, 1, 1], [0, 0, 0, 0]
Saída: [1.0, 0.0]

Entrada: [15, 20, 25], [0, 1, 14]
Saída: [20.0, 5.0]

Entrada: [], []
Saída: []

'''


'''
def calcula_cm(listax, listay):
    if listax == []:
        return []
    else:
        return [sum(listax) / len(listax), sum(listay) / len(listay)]



def calcula_cm(listax, listay):
    if listax == []:
        return []
    else:
        xcm = sum(listax) / len(listax)
        ycm = sum(listay) / len(listay)
        return [xcm, ycm]
'''
'''
def calcula_cm(listax, listay):
    if listax == []:
        return []
    else:
        soma_x = sum(listax)
        soma_y = sum(listay)
        n = len(listax)
        return [(soma_x / n), (soma_y / n)]


def calcula_cm(listax, listay):
    if listax == []:
        return []
    else:
        soma_x = 0
        soma_y = 0
        n = len(listax)
        for i in range(n):
            soma_x += listax[i]
            soma_y += listay[i]
        x_cm = soma_x / n
        y_cm = soma_y / n
        return [x_cm, y_cm]

'''

'''def calcula_cm(x, y):
    if x != [] and y != []:
        return [sum(x) / len(x), sum(y) / len(y)]
    else:
        return []'''


'''def calcula_cm(x, y):
    if x != [] and y != []:
        soma_x = 0
        soma_y = 0
        n = len(x) # ou len(y)
        for i in range(n):
            soma_x += x[i]
            soma_y += y[i]
        x_cm = soma_x / n
        y_cm = soma_y / n
        X_Y_cm = [x_cm, y_cm]
        return X_Y_cm
    else:
        return []'''


'''def calcula_cm(x, y):
    if x != [] and y != []:
        soma_x = 0
        soma_y = 0
        n = len(x) # ou len(y)
        i = 0
        while i < len(x):
            soma_x += x[i]
            soma_y += y[i]
            i += 1
        x_cm = soma_x / n
        y_cm = soma_y / n
        X_Y_cm = [x_cm, y_cm]
        return X_Y_cm
    else:
        return []'''

#Testes 
print(calcula_cm([1, 1, 1, 1], [0, 0, 0, 0]))
print(calcula_cm([15, 20, 25], [0, 1, 14]))
print(calcula_cm([], []))
