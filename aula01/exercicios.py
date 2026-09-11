"""Aula 01 - De C para Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def soma_lista(lista):
    soma = 0
  for n in lista:
    soma = soma + n
  return soma


def conta_pares(lista):
  contador = 0
  for n in lista:
    if n%2 == 0:
      contador = contador + 1
  return contador

def maior_valor(lista):
  maior = lista[0]
  for n in lista:
    if n > maior:
      maior = n
  return maior
    

def existe(lista, alvo):
    for i in lista:
        if i == alvo:
            return True
      
      return False


def busca_linear(lista, alvo):
   for i in range (len ( lista ) ) :
      if lista [ i ] == alvo :
          return i 
   return -1


def segundo_maior(lista):
  maior = lista[0]
  segundo = lista[1]
  
  if maior < segundo:
      temp = maior
      maior = segundo
      segundo = temp

  for i in lista[2:]:
      if i > maior:
       segundo = maior
       maior = i

      elif i > segundo:
        segundo = i
  return segundo