# ELIMINACIÓN GAUSSIANA

Métodos Numéricos — Ingeniería en Sistemas Automotrices

La eliminación gaussiana resuelve sistemas de ecuaciones lineales mediante operaciones entre filas. Primero elimina los coeficientes debajo de cada pivote para obtener una matriz triangular superior y después calcula las incógnitas por sustitución hacia atrás. En este programa se utiliza pivoteo parcial para intercambiar filas cuando conviene.

Referencia: Chapra y Canale, Métodos numéricos para ingenieros, 7.ª edición, capítulo 9.



ALGORITMO:

Algoritmo de eliminación gaussiana con pivoteo parcial

1. Inicio: Iniciar el programa.
2. Ingresar datos: Pedir al usuario el número de ecuaciones.
3. Crear matriz: Solicitar los coeficientes y resultados de cada ecuación.
4. Buscar pivote: Seleccionar el número de mayor valor absoluto en la columna.
5. Verificar pivote: Comprobar que no sea prácticamente cero.
6. Intercambiar filas: Colocar el mejor pivote en la posición correspondiente.
7. Eliminación hacia adelante: Calcular factores y hacer ceros debajo del pivote.
8. Repetir: Continuar hasta formar una matriz triangular superior.
9. Sustitución hacia atrás: Calcular las incógnitas comenzando por la última.
10. Mostrar resultados: Imprimir las soluciones con cuatro decimales.
11. Fin: Terminar el programa.


CÓDIGO FUENTE EN PYTHON:

```python
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
```

# Ejemplo de eliminación gaussiana en Python

## Sistema de ecuaciones

3x + 2y = 18  
-x + 2y = 2

## Datos ingresados por el usuario

Numero de ecuaciones: 2

Fila 1: 3 2 18  
Fila 2: -1 2 2

## Procedimiento del programa

1. Recibe el número de ecuaciones.
2. Solicita los valores de la matriz aumentada.
3. Selecciona el mejor pivote.
4. Realiza la eliminación hacia adelante.
5. Aplica la sustitución hacia atrás.
6. Muestra los resultados con cuatro decimales.

## Resultados obtenidos

x1 = 4.0000  
x2 = 3.0000

## Comprobación

Primera ecuación:

3(4) + 2(3) = 18  
12 + 6 = 18 ✓

Segunda ecuación:

-(4) + 2(3) = 2  
-4 + 6 = 2 ✓

## Conclusión

El usuario únicamente ingresó el número de ecuaciones y los valores de la matriz aumentada. El programa aplicó automáticamente el método de eliminación gaussiana con pivoteo parcial y obtuvo las soluciones correctas.




# Ejemplo automotriz: Distribución del peso de un automóvil

## 1. Planteamiento del problema

Un ingeniero automotriz necesita determinar la fuerza que soportan los ejes delantero y trasero de un automóvil.

Datos del vehículo:

- Peso total: 12,000 N
- Distancia entre ejes: 2.5 m
- Centro de gravedad: 1 m detrás del eje delantero

Se considera que el automóvil está en reposo sobre una superficie horizontal.

Se desea calcular la fuerza que soporta cada eje utilizando el método de eliminación gaussiana en Python.

## 2. Sistema de ecuaciones

Definimos:

x = Fuerza sobre el eje delantero (N)
y = Fuerza sobre el eje trasero (N)

Por equilibrio de fuerzas:

x + y = 12000

Por equilibrio de momentos respecto al eje delantero:

2.5y = 12000

Sistema:

x + y = 12000
0x + 2.5y = 12000

## 3. Datos ingresados por el usuario en Python

Numero de ecuaciones: 2

Fila 1: 1 1 12000
Fila 2: 0 2.5 12000

## 4. Procedimiento del programa

1. Recibe los valores de la matriz aumentada.
2. Selecciona el pivote.
3. Realiza la eliminación hacia adelante.
4. Aplica la sustitución hacia atrás.
5. Calcula las fuerzas de ambos ejes.

## 5. Resultados obtenidos

RESULTADOS:

x1 = 7200.0000
x2 = 4800.0000

Eje delantero = 7200 N
Eje trasero = 4800 N

## 6. Comprobación

Primera ecuación:

7200 + 4800 = 12000 ✓

Segunda ecuación:

2.5(4800) = 12000 ✓

## 7. Conclusión

Mediante el método de eliminación gaussiana se determinó que el eje delantero soporta 7200 N y el eje trasero 4800 N.

El usuario únicamente ingresó los valores de la matriz aumentada y el programa calculó automáticamente los resultados.

Este procedimiento permite analizar la distribución estática de cargas de un automóvil, información útil para el estudio de suspensiones y el diseño de componentes automotrices.

Referencia metodológica:
Chapra y Canale. Métodos numéricos para ingenieros, 7.ª edición, capítulo 9.

Ejemplo automotriz adaptado para fines educativos.






Referencia: Chapra y Canale, Métodos numéricos para ingenieros, 7.ª edición, capítulo 9.

