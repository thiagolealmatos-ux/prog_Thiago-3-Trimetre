def bubble_sort(lista):
    lista = lista.copy()
    comparacoes = 0
    trocas = 0

    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):
            comparacoes += 1

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1

    return lista, comparacoes, trocas


def selection_sort(lista):
    lista = lista.copy()
    comparacoes = 0
    trocas = 0

    for i in range(len(lista) - 1):
        menor = i

        for j in range(i + 1, len(lista)):
            comparacoes += 1

            if lista[j] < lista[menor]:
                menor = j

        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
            trocas += 1

    return lista, comparacoes, trocas


def insertion_sort(lista):
    lista = lista.copy()

    for i in range(1, len(lista)):
        valor = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valor:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = valor

    return lista


def quicksort(lista):
    if len(lista) <= 1:
        return lista.copy()

    pivo = lista[len(lista) // 2]
    menores = []
    iguais = []
    maiores = []

    for numero in lista:
        if numero < pivo:
            menores.append(numero)
        elif numero == pivo:
            iguais.append(numero)
        else:
            maiores.append(numero)

    return quicksort(menores) + iguais + quicksort(maiores)