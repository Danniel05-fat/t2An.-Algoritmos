import random

def crearMatriz(n):
   
    return [[random.randint(99, 999) for _ in range(n)] for _ in range(n)]

def mostrarMatriz(matriz):

    n = len(matriz)
    print("\n" + "=" * (n * 7))
    for fila in matriz:
        print(" ".join(f"{num:5d}" for num in fila))
    print("=" * (n * 7))

#divide y conquista
def contarMultiplosDv(matriz, fila_inicio, fila_fin, col_inicio, col_fin):
   
    
    if fila_inicio == fila_fin - 1 and col_inicio == col_fin - 1:
        num = matriz[fila_inicio][col_inicio]
        return 1 if (num % 5 == 0 or num % 7 == 0) else 0
    
   
    if (fila_fin - fila_inicio) <= 2 and (col_fin - col_inicio) <= 2:
        total = 0
        for i in range(fila_inicio, fila_fin):
            for j in range(col_inicio, col_fin):
                num = matriz[i][j]
                if num % 5 == 0 or num % 7 == 0:
                    total += 1
        return total
    
   
    fila_medio = (fila_inicio + fila_fin) // 2
    col_medio = (col_inicio + col_fin) // 2
    
    total = 0
    total += contarMultiplosDv(matriz, fila_inicio, fila_medio, col_inicio, col_medio)
    total += contarMultiplosDv(matriz, fila_inicio, fila_medio, col_medio, col_fin)
    total += contarMultiplosDv(matriz, fila_medio, fila_fin, col_inicio, col_medio)
    total += contarMultiplosDv(matriz, fila_medio, fila_fin, col_medio, col_fin)
    
    return total

#main
while True:
    try:
        n = int(input("Ingrese el tamaño de la matriz cuadrada N x N: "))
        if n > 0:
            break
        print("El tamaño debe ser un número positivo.")
    except ValueError:
        print("Debe ingresar un número entero válido.")

# Crear y llenar matriz
matriz = crearMatriz(n)

# Mostrar
mostrarMatriz(matriz)

#divide y conquista
resultado = contarMultiplosDv(matriz, 0, n, 0, n)


print(f"\nCantidad de números múltiplos de 5 o 7: {resultado}")

