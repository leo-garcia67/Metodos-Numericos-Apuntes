"""Pruebas reproducibles: seis casos por cada metodo."""
from eliminacion_gaussiana import eliminacion_gaussiana
from jacobi import jacobi
from gauss_seidel import gauss_seidel

CASOS = {
    'Gauss': [
        ('G1', [[3, 2, 18], [-1, 2, 2]], True),
        ('G2', [[1, 1, 12000], [0, 2.5, 12000]], True),
        ('G3', [[40, -10, 0, 20], [-10, 50, -10, 60], [0, -10, 40, 100]], True),
        ('G4', [[4, -1, 12], [-1, 3, 0]], True),
        ('G5', [[1, 2, 3], [2, 4, 6]], False),
        ('G6', [[1, 2, 3], [2, 4, 7]], False),
    ],
    'Jacobi': [
        ('J1', [[4, -1, 3], [-1, 3, 2]], True),
        ('J2', [[40, -10, 0, 20], [-10, 50, -10, 60], [0, -10, 40, 100]], True),
        ('J3', [[6, -1, 140], [-1, 5, 170]], True),
        ('J4', [[8, -1, 0, 13], [-1, 7, -1, 15], [0, -1, 6, 21]], True),
        ('J5', [[0, 1, 1], [2, 3, 5]], False),
        ('J6', [[1, 3, 4], [4, 1, 5]], False),
    ],
    'Gauss-Seidel': [
        ('S1', [[4, -1, 3], [-1, 3, 2]], True),
        ('S2', [[40, -10, 0, 20], [-10, 50, -10, 60], [0, -10, 40, 100]], True),
        ('S3', [[4, -1, 12], [-1, 3, 0]], True),
        ('S4', [[8, -1, 0, 13], [-1, 7, -1, 15], [0, -1, 6, 21]], True),
        ('S5', [[0, 1, 1], [2, 3, 5]], False),
        ('S6', [[1, 4, 5], [3, 1, 4]], False),
    ]
}

def residuo(matriz, solucion):
    n = len(matriz)
    return max(abs(sum(fila[j] * solucion[j] for j in range(n)) - fila[n]) for fila in matriz)

def ejecutar():
    cuenta = 0
    for metodo, casos in CASOS.items():
        print('\n' + metodo.upper())
        for nombre, matriz, exitoso in casos:
            if metodo == 'Gauss':
                solucion, mensaje = eliminacion_gaussiana(matriz)
                iteraciones = '-'
            else:
                funcion = jacobi if metodo == 'Jacobi' else gauss_seidel
                solucion, iteraciones, mensaje, error = funcion(matriz)
            assert (solucion is not None) == exitoso, f'{nombre} inesperado'
            if solucion is not None:
                assert residuo(matriz, solucion) < 1e-4, f'{nombre}: residuo alto'
            cuenta += 1
            print(f'{nombre}: {"CORRECTO" if exitoso else "LIMITACION"} | iteraciones={iteraciones} | {mensaje}')
    print(f'\n{cuenta} de 18 pruebas verificadas.')

if __name__ == '__main__':
    ejecutar()
