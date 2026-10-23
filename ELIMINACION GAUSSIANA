# Metodos-Numericos-Apuntes
Libreta de apuntes de la materia Métodos Numéricos


ELIMINACION GAUSSIANA


    # ELIMINACION HACIA ADELANTE
    for i in range(n):

        # Buscar el mejor pivote
        pivote = max(range(i, n), key=lambda j: abs(A[j][i]))

        if abs(A[pivote][i]) < 1e-12:
            print("El sistema no tiene solucion unica.")
            return

        # Intercambiar filas
        A[i], A[pivote] = A[pivote], A[i]

        # Hacer ceros debajo del pivote
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]

            for k in range(i, n + 1):
                A[j][k] -= factor * A[i][k]

    # SUSTITUCION HACIA ATRAS
    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        suma = 0

        for j in range(i + 1, n):
            suma += A[i][j] * x[j]

        x[i] = (A[i][n] - suma) / A[i][i]

    # MOSTRAR RESULTADOS
    print("\nRESULTADOS:")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.4f}")


# PROGRAMA PRINCIPAL
while True:
    try:
        n = int(input("Numero de ecuaciones: "))
        if n > 0:
            break
        print("Ingresa un numero mayor que cero.")
    except ValueError:
        print("Ingresa un numero entero valido.")

A = []

print("\nIngresa la matriz aumentada.")
print("Escribe cada fila separada por espacios.")
print("Incluye el resultado al final de cada fila.\n")

for i in range(n):
    while True:
        try:
            fila = list(map(float, input(f"Fila {i+1}: ").split()))

            if len(fila) == n + 1:
                A.append(fila)
                break
            else:
                print(f"Debes ingresar {n+1} numeros.")

        except ValueError:
            print("Ingresa solamente numeros validos.")

eliminacion_gaussiana(A, n)
