import random
import time

def bubble_sort(lista):
    n = len(lista)
    total_iteracoes = 0  # contador de iterações
    for i in range(n - 1):
        for j in range(n - i - 1):
            total_iteracoes += 1  # incrementa a cada iteração
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    print("Total de iterações:", total_iteracoes)
    return lista


