def calcula_escola(lista):
    soma = 0
    i = 0
    while i < len(lista):
        quesito = lista[i]
        menor_valor = min(quesito)
        quesito.remove(menor_valor)
        soma += sum(quesito)
        #for nota in quesito:
        #    soma += nota
        #j = 0
        #while j < len(quesito):
        #    soma += quesito[j]
        #    j += 1
        i += 1
    return soma




def calcula_escola(lista):
    soma = 0
    for quesito in lista:
        menor_valor = min(quesito)
        quesito.remove(menor_valor)
        soma += sum(quesito)
        #for nota in quesito:
        #    soma += nota
    return soma



































'''def calcula_escola(lista):
    soma = 0
    for quesito in lista:
        #maior_nota = max(quesito)
        menor_nota = min(quesito)
        quesito.remove(menor_nota)
        '''i = 0
        while i < len(quesito):
            soma += quesito[i]
            i += 1'''
        soma += quesito[0] + quesito[1] + quesito[2] 
    return soma'''

'''
tom_maior = ...
print(calcula_escola(tom_maior))

def calcula_escola(lista):
    soma = 0
    for quesito in lista:
        menor_nota = min(quesito)
        quesito.remove(menor_nota)
        soma += sum(quesito)
    return soma
'''