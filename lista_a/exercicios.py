"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

def conta_negativos(lista):
    
    contador = 0
    
    for numero in lista:
        if numero < 0:
            contador += 1
            
    return contador


def media(lista):
    
    if len(lista) == 0:
        return 0
    
    return sum(lista) / len(lista)



def sem_o_maior(lista):

    lista_nova = lista.copy()

    if len(lista_nova) >0:
        maior = max(lista_nova)
        lista_nova.remove(maior)

    return lista_nova


def acumulada(lista):
    resultado = []
    soma = 0

    for numero in lista:
        soma += numero
        resultado.append(soma)

    return resultado

def achata(lista_de_listas):
   resultado = []

   for sublista in lista_de_listas:
       for numero in sublista:
           resultado.append(numero)
    
   return resultado


# ---------- Bloco 2: busca ----------

def busca_ultima(lista, alvo):

    posicao = -1

    for i in range(len(lista)):
        if lista[i] == alvo:
            posicao = i

    return posicao


def conta_ocorrencias(lista, alvo):

    contador = 0

    for numero in lista:
        if numero == alvo:
            contador += 1

    return contador 


def primeiro_maior_que(lista, limite):

    for i in range(len(lista)):
        if lista[i] > limite:
            return i

    return -1


def busca_binaria_primeira(lista, alvo):

    inicio = 0
    fim = len(lista) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim)// 2

        if lista[meio] == alvo:
            resultado = meio
            fim = meio - 1

        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return resultado


# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):

    soma = 0
    comparacoes = 0

    for numero in lista:
        comparacoes += 1
        if numero % 2 == 0:
            soma += numero

    return soma, comparacoes

    
def maior_contando(lista):
    
    maior = lista[0]
    comparacoes = 0

    for i in range(1, len(lista)):
        comparacoes += 1
        if lista[i] > maior:
            maior = lista[i]

    return maior, comparacoes
    


def tem_soma_contando(lista, alvo):
    comparacoes = 0

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            comparacoes += 1

            if lista[i] + lista[j] == alvo:
                return True, comparacoes

    return False, comparacoes

     

def ordenada_contando(lista):

    comparacoes = 0

    for i in range(len(lista) - 1):
        comparacoes += 1
        if lista[i] > lista[i + 1]:
            return False, comparacoes

    return True, comparacoes


# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):

    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1

    return None


def eh_palindromo(lista):

    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        if lista[inicio] != lista[fim]:
            return False
        
        inicio += 1
        fim -= 1

    return True




def par_que_soma(lista, alvo):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                return i, j

    return -1, -1




def soma_maxima_janela(lista, k):
    if k <= 0 or k > len(lista):
        return None

    soma_atual = sum(lista[:k])
    maior_soma = soma_atual

    for i in range(k, len(lista)):
        soma_atual = soma_atual - lista[i - k] + lista[i]
        if soma_atual > maior_soma:
            maior_soma = soma_atual

    return maior_soma




def parenteses_balanceados(texto):
    pilha = []

    for caractere in texto:
        if caractere in "([":
            pilha.append(caractere)

        elif caractere in ")]":
            if len(pilha) == 0:
                return False

            abertura = pilha.pop()

            if abertura == "(" and caractere != ")":
                return False
            if abertura == "[" and caractere != "]":
                return False

    return len(pilha) == 0