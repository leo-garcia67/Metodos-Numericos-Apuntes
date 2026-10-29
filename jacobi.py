"""Metodo iterativo de Jacobi: matriz capturada por teclado."""


def jacobi(matriz, tolerancia=0.01, max_iter=100):
    n = len(matriz)
    if any(abs(matriz[i][i]) < 1e-12 for i in range(n)):
        return None, 0, 'Error: cero en la diagonal principal.', None

    dominante = all(
        abs(matriz[i][i]) > sum(abs(matriz[i][j]) for j in range(n) if j != i)
        for i in range(n)
    )
    advertencia = '' if dominante else 'Aviso: diagonal no dominante. '
    anterior = [0.0] * n

    for paso in range(1, max_iter + 1):
        # Todos los nuevos valores usan SOLO la iteracion anterior.
        nuevo = [
            (matriz[i][n] - sum(matriz[i][j] * anterior[j]
             for j in range(n) if j != i)) / matriz[i][i]
            for i in range(n)
        ]
        errores = [
            100 * abs(nuevo[i] - anterior[i]) / abs(nuevo[i])
            if abs(nuevo[i]) > 1e-12
            else (0.0 if abs(nuevo[i] - anterior[i]) < 1e-12 else float('inf'))
            for i in range(n)
        ]
        residuos = [
            abs(sum(matriz[i][j] * nuevo[j] for j in range(n)) - matriz[i][n])
            for i in range(n)
        ]
        if max(errores) < tolerancia and max(residuos) < 1e-4:
            return nuevo, paso, advertencia + 'Convergencia alcanzada.', max(errores)
        if max(abs(v) for v in nuevo) > 1e8:
            return None, paso, advertencia + 'Divergencia detectada: valores crecientes.', max(errores)
        anterior = nuevo
    return None, max_iter, advertencia + 'No alcanzo la tolerancia.', max(errores)


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
    resultado, iteraciones, mensaje, error = jacobi(A)
    print('\n' + mensaje)
    if resultado is not None:
        print('RESULTADOS:')
        for i, valor in enumerate(resultado, 1):
            print(f'x{i} = {valor:.4f}')
    print(f'Iteraciones: {iteraciones}')
    if error is not None:
        print(f'Error relativo maximo: {error:.4f}%')
