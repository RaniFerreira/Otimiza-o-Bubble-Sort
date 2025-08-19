
import time
from bubbleSort import bubble_sort
from bubbleSortOtimizado import bubble_sort_optimized


if __name__ == "__main__":
    
    
    #primeiro teste*************************************************
    primeiroTeste = [12, 4, 8, 15, 3, 7, 1, 10, 5, 9]
    print("\nBubble Sort Simples Teste 1")
    print(primeiroTeste)
    inicio = time.time()
    print(bubble_sort(primeiroTeste))
    fim = time.time()
    
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")
    
    primeiroTeste = [12, 4, 8, 15, 3, 7, 1, 10, 5, 9]
    print("\nBubble Sort Otimizado teste 1")
    print(primeiroTeste)
    inicio = time.time()
    print(bubble_sort_optimized(primeiroTeste))
    fim = time.time()
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")
    
    #segundo teste**********************************************************
    segundoTeste = [25, 17, 31, 13, 2, 29, 8, 19, 7, 11, 6]
    print("\nBubble Sort Simples Teste 2")
    print(segundoTeste)
    inicio = time.time()
    print(bubble_sort(segundoTeste))
    fim = time.time()
    
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")
    
    segundoTeste = [25, 17, 31, 13, 2, 29, 8, 19, 7, 11, 6]
    print("\nBubble Sort otimizado teste 2")
    print(segundoTeste)
    inicio = time.time()
    print(bubble_sort_optimized(segundoTeste))
    fim = time.time()
    
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")
    
    #terceiro teste************************************************
    terceiroTeste = [102, 57, 33, 88, 74, 91, 45, 60, 12, 80, 23, 39, 5, 67, 49, 1, 14, 72, 95, 81]
    print("\nBubble Sort Simples Teste 3")
    print(terceiroTeste)
    inicio = time.time()
    print(bubble_sort(terceiroTeste))
    fim = time.time()
   
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")
    
    terceiroTeste = [102, 57, 33, 88, 74, 91, 45, 60, 12, 80, 23, 39, 5, 67, 49, 1, 14, 72, 95, 81]
    print("\nBubble Sort otimizado teste 3")
    print(terceiroTeste)
    inicio = time.time()
    print(bubble_sort_optimized(terceiroTeste))
    fim = time.time()
    
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")

   
