

def bubble_sort_optimized(lista):
    n = len(lista)
    total_iteracoes = 0  # contador de iterações
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            total_iteracoes += 1  # incrementa a cada iteração
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        if not swapped:
            break
    print("Total de iterações:", total_iteracoes)
    return lista


