

def bubble_sort_optimized(lista):
    n = len(lista)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        if not swapped:
            break
    return lista

