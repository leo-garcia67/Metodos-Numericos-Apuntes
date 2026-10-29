"""Eliminacion gaussiana con pivoteo parcial. Entrada por teclado."""


def rango(matriz, tolerancia=1e-12):
    a = [fila[:] for fila in matriz]
    filas, columnas = len(a), len(a[0])
    fila_pivote = 0
    for col in range(columnas):
        if fila_pivote == filas:
            break
        mejor = max(range(fila_pivote, filas), key=lambda f: abs(a[f][col]))
        if abs(a[mejor][col]) < tolerancia:
            continue
        a[fila_pivote], a[mejor] = a[mejor], a[fila_pivote]
        for f in range(fila_pivote + 1, filas):
            factor = a[f][col] / a[fila_pivote][col]
            for j in range(col, columnas):
                a[f][j] -= factor * a[fila_pivote][j]
        fila_pivote += 1
    return fila_pivote


def eliminacion_gaussiana(matriz):
    n = len(matriz)
    a = [fila[:] for fila in matriz]

    # Eliminacion hacia adelante con pivoteo parcial.
    for i in range(n):
        pivote = max(range(i, n), key=lambda f: abs(a[f][i]))
        if abs(a[pivote][i]) < 1e-12:
            rango_a = rango([fila[:n] for fila in matriz])
            rango_ampliada = rango(matriz)
            if rango_a < rango_ampliada:
                return None, 'Sistema incompatible: no tiene solucion.'
            return None, 'Sistema dependiente: tiene infinitas soluciones.'
        a[i], a[pivote] = a[pivote], a[i]
        for j in range(i + 1, n):
            factor = a[j][i] / a[i][i]
            for k in range(i, n + 1):
                a[j][k] -= factor * a[i][k]

    # Sustitucion hacia atras.
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        suma = sum(a[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (a[i][n] - suma) / a[i][i]
    return x, 'Solucion unica encontrada.'


def leer_matriz():
    while True:
        try:
            n = int(input('Numero de ecuaciones: '))
            if n > 0:
                break
        except ValueError:
            pass
        print('Ingresa un numero entero positivo.')
    print('Matriz aumentada: escribe cada fila separada por espacios.')
    matriz = []
    for i in range(n):
        while True:
            try:
                fila = [float(v) for v in input(f'Fila {i+1}: ').split()]
                if len(fila) == n + 1:
                    matriz.append(fila)
                    break
            except ValueError:
                pass
            print(f'Ingresa exactamente {n+1} numeros validos.')
    return matriz


if __name__ == '__main__':
    A = leer_matriz()
    solucion, mensaje = eliminacion_gaussiana(A)
    print('\n' + mensaje)
    if solucion is not None:
        print('RESULTADOS:')
        for i, valor in enumerate(solucion, 1):
            print(f'x{i} = {valor:.4f}')
