def conta_frequencias(lista):
    frequencias = {}

    for item in lista:
        if item in frequencias:
            frequencias[item] = frequencias[item] + 1
        else:
            frequencias[item] = 1

    return frequencias

def hash_soma(palavra, tamanho):
    total = 0

    for letra in palavra:
        total = total + ord(letra)

    return total % tamanho

def gavetas_com_colisao(palavras, tamanho):
    gavetas = {}

    for palavra in palavras:
        indice = hash_soma(palavra, tamanho)

        if indice not in gavetas:
            gavetas[indice] = []
        if palavra not in gavetas[indice]:
            gavetas[indice].append(palavra)

    resultado = []

    for indice in gavetas:
        if len(gavetas[indice]) >= 2:
            resultado.append(gavetas[indice])

    return resultado

def mais_frequente(lista):
    if len(lista) == 0:
        return None

    frequencias = conta_frequencias(lista)
    maior = 0
    resultado = None

    for item in lista:
        if frequencias[item] > maior:
            maior = frequencias[item]
            resultado = item

    return resultado