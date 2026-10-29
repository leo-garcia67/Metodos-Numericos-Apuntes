
# MÉTODO DE GAUSS-SEIDEL

Métodos Numéricos — Ingeniería en Sistemas Automotrices

Referencia: Chapra y Canale, Métodos numéricos para ingenieros, 7.ª edición, capítulo 11, sección 11.2, páginas 241–243.

## 1. ¿Qué es el método de Gauss-Seidel?

El método de Gauss-Seidel es un procedimiento numérico iterativo que permite resolver sistemas de ecuaciones lineales mediante aproximaciones sucesivas.

Consiste en comenzar con valores iniciales, normalmente cero, y calcular nuevas aproximaciones hasta alcanzar una tolerancia de error.

A diferencia de la eliminación gaussiana, no necesitamos eliminar las incógnitas una por una.

**Diferencia con Jacobi:** Gauss-Seidel utiliza inmediatamente cada valor nuevo para calcular la siguiente incógnita. Jacobi espera hasta la siguiente iteración para utilizar los valores nuevos.

## 2. ¿Cómo funciona?

1. Ordenar las ecuaciones y despejar una incógnita en cada una.
2. Verificar que los elementos de la diagonal principal sean distintos de cero.
3. Asignar valores iniciales, normalmente cero.
4. Calcular una incógnita y utilizar inmediatamente su nuevo valor para calcular la siguiente.
5. Repetir hasta cumplir la tolerancia o alcanzar el máximo de iteraciones.

## 3. Fórmula general

Para el sistema:

a11*x1 + a12*x2 + a13*x3 = b1

a21*x1 + a22*x2 + a23*x3 = b2

a31*x1 + a32*x2 + a33*x3 = b3

Las fórmulas de Gauss-Seidel son:

x1(nuevo) = [b1 - a12*x2(anterior) - a13*x3(anterior)] / a11

x2(nuevo) = [b2 - a21*x1(nuevo) - a23*x3(anterior)] / a22

x3(nuevo) = [b3 - a31*x1(nuevo) - a32*x2(nuevo)] / a33

En una misma iteración se emplean los valores nuevos que ya se calcularon.

**Diagonal dominante:** si el valor absoluto del coeficiente diagonal de cada ecuación es mayor que la suma de los valores absolutos de los otros coeficientes de esa fila, se garantiza la convergencia.

Si no se cumple esta condición, el método todavía puede converger, pero no está garantizado.

---

# ALGORITMO DEL MÉTODO DE GAUSS-SEIDEL

Basado en el capítulo 11 del libro de Chapra y Canale.

1. Inicio: Iniciar el programa.

2. Ingresar datos: Solicitar el número de ecuaciones y los valores de la matriz aumentada.

3. Verificar matriz: Comprobar que los elementos de la diagonal principal sean diferentes de cero.

4. Asignar valores iniciales: Establecer las incógnitas inicialmente en cero.

5. Despejar incógnitas: Preparar las ecuaciones para calcular cada variable.

6. Calcular iteración: Obtener nuevos valores utilizando inmediatamente los resultados recién calculados.

7. Calcular error: Comparar los valores nuevos con los anteriores.

8. Verificar tolerancia: Comprobar si los errores son menores que el error permitido.

9. Repetir: Si no se cumple la tolerancia, realizar otra iteración hasta alcanzar el límite establecido.

10. Mostrar resultados: Imprimir los valores aproximados de las incógnitas o avisar si no se alcanzó la convergencia.

11. Fin: Terminar el programa.

## Resumen del algoritmo

Inicio → Ingresar matriz → Verificar diagonal → Asignar ceros → Despejar → Iterar → Calcular error → Verificar tolerancia → Mostrar resultados → Fin.

Importante: En Gauss-Seidel se utilizan inmediatamente los valores nuevos obtenidos durante la misma iteración.

---

# CÓDIGO EN PYTHON

Este código permite que el usuario ingrese la matriz desde el teclado.

```python
"""Metodo iterativo de Gauss-Seidel: matriz capturada por teclado."""


def gauss_seidel(matriz, tolerancia=0.01, max_iter=100):
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
        nuevo = anterior[:]
        for i in range(n):
            # Valores nuevos para j < i; anteriores para j > i.
            suma = sum(matriz[i][j] * (nuevo[j] if j < i else anterior[j])
                       for j in range(n) if j != i)
            nuevo[i] = (matriz[i][n] - suma) / matriz[i][i]
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
    resultado, iteraciones, mensaje, error = gauss_seidel(A)
    print('\n' + mensaje)
    if resultado is not None:
        print('RESULTADOS:')
        for i, valor in enumerate(resultado, 1):
            print(f'x{i} = {valor:.4f}')
    print(f'Iteraciones: {iteraciones}')
    if error is not None:
        print(f'Error relativo maximo: {error:.4f}%')
```

El programa utiliza una tolerancia de error del 0.01%, comprueba los residuos con un límite de 0.0001 y permite un máximo de 100 iteraciones.

---

# EJEMPLO 1. SISTEMA DE ECUACIONES LINEALES

## 1. Planteamiento del problema

Un usuario necesita resolver un sistema de dos ecuaciones lineales utilizando el método de Gauss-Seidel en Python.

Sistema de ecuaciones:

3x + 2y = 18

-x + 2y = 2

## 2. Datos ingresados por el usuario

Numero de ecuaciones: 2

Fila 1: 3 2 18

Fila 2: -1 2 2

## 3. Procedimiento del programa

1. Recibe el número de ecuaciones.
2. Solicita los valores de la matriz aumentada.
3. Verifica la diagonal principal.
4. Asigna valores iniciales de cero.
5. Calcula las aproximaciones utilizando inmediatamente los nuevos resultados.
6. Calcula el error porcentual.
7. Repite hasta alcanzar la tolerancia del 0.01%.
8. Muestra los resultados.

### Desarrollo matemático

Despejamos:

x = (18 - 2y) / 3

y = (2 + x) / 2

Valores iniciales:

x = 0

y = 0

**Primera iteración:**

x1 = (18 - 2(0)) / 3

x1 = 6.0000

y1 = (2 + 6.0000) / 2

y1 = 4.0000

**Segunda iteración:**

x2 = (18 - 2(4.0000)) / 3

x2 = 3.3333

y2 = (2 + 3.3333...) / 2

y2 = 2.6667

El programa continúa realizando el mismo procedimiento hasta cumplir la tolerancia.

## 4. Resultados obtenidos

Convergencia alcanzada.

RESULTADOS:

x1 = 4.0000

x2 = 3.0000

Iteraciones: 12

Error relativo máximo: 0.0011%

## 5. Comprobación

Los resultados se aproximan a:

x = 4

y = 3

Primera ecuación:

3(4) + 2(3) = 18

12 + 6 = 18 ✓

Segunda ecuación:

-(4) + 2(3) = 2

-4 + 6 = 2 ✓

## 6. Conclusión

El usuario ingresó únicamente los valores de la matriz aumentada. El programa realizó 12 iteraciones mediante el método de Gauss-Seidel hasta alcanzar la tolerancia establecida.

El método permitió obtener una solución aproximada correcta, utilizando inmediatamente los resultados nuevos en cada iteración.

---

# EJEMPLO 2. APLICACIÓN EN SISTEMAS AUTOMOTRICES

## ANÁLISIS DE CORRIENTES ELÉCTRICAS DE UN AUTOMÓVIL

### 1. Planteamiento del problema

Un ingeniero automotriz necesita calcular las corrientes eléctricas de dos mallas de un circuito alimentado por una batería de 12 V.

El circuito tiene:

- Una resistencia de 3 ohmios en la primera malla.
- Una resistencia de 2 ohmios en la segunda malla.
- Una resistencia compartida de 1 ohmio.
- Una batería de 12 V en la primera malla.

Mediante las leyes de Kirchhoff se obtiene el siguiente sistema:

4I1 - I2 = 12

-I1 + 3I2 = 0

Donde:

I1 = Corriente de la primera malla (A).

I2 = Corriente de la segunda malla (A).

### 2. Datos ingresados por el usuario

Numero de ecuaciones: 2

Fila 1: 4 -1 12

Fila 2: -1 3 0

### 3. Procedimiento del programa

1. Recibe los valores de la matriz aumentada.
2. Verifica los elementos de la diagonal.
3. Asigna valores iniciales de cero.
4. Realiza las iteraciones del método de Gauss-Seidel.
5. Utiliza inmediatamente los nuevos resultados.
6. Calcula el error porcentual.
7. Repite hasta alcanzar la tolerancia del 0.01%.
8. Muestra las corrientes calculadas.

### Desarrollo matemático

Despejamos:

I1 = (12 + I2) / 4

I2 = I1 / 3

Valores iniciales:

I1 = 0

I2 = 0

**Primera iteración:**

I1 = (12 + 0) / 4

I1 = 3.0000 A

I2 = 3.0000 / 3

I2 = 1.0000 A

**Segunda iteración:**

I1 = (12 + 1.0000) / 4

I1 = 3.2500 A

I2 = 3.2500 / 3

I2 = 1.0833 A

Se continúa con las siguientes iteraciones.

### 4. Resultados obtenidos

Convergencia alcanzada.

RESULTADOS:

x1 = 3.2727

x2 = 1.0909

Iteraciones: 5

Error relativo máximo: 0.0044%

### 5. Comprobación

Soluciones aproximadas a cuatro decimales:

I1 = 3.2727 A

I2 = 1.0909 A

Primera ecuación:

4(3.2727) - 1.0909 = 12

13.0908 - 1.0909 = 11.9999 ≈ 12 ✓

Segunda ecuación:

-(3.2727) + 3(1.0909) = 0

-3.2727 + 3.2727 = 0 ✓

### 6. Conclusión

Mediante el método de Gauss-Seidel se calcularon las corrientes eléctricas aproximadas de un circuito automotriz.

La primera malla presentó una corriente de 3.2727 A y la segunda de 1.0909 A.

El usuario solamente ingresó los valores de la matriz y el programa realizó automáticamente cinco iteraciones hasta alcanzar la tolerancia.

Este método resulta útil para analizar circuitos eléctricos y resolver sistemas de ecuaciones relacionados con Ingeniería en Sistemas Automotrices.

---

# EJEMPLO 3. MÉTODO DE GAUSS-SEIDEL APLICADO A SISTEMAS AUTOMOTRICES

## ANÁLISIS DE UNA SUSPENSIÓN AUTOMOTRIZ

### 1. Planteamiento del problema

Un ingeniero automotriz necesita determinar los desplazamientos verticales de tres puntos de un sistema de suspensión mediante un modelo simplificado de resortes acoplados.

Los resortes tienen rigideces conocidas y reciben diferentes fuerzas.

Se obtiene el siguiente sistema de ecuaciones:

40x1 - 10x2 = 20

-10x1 + 50x2 - 10x3 = 60

-10x2 + 40x3 = 100

Donde:

x1 = Desplazamiento del primer punto (mm).

x2 = Desplazamiento del segundo punto (mm).

x3 = Desplazamiento del tercer punto (mm).

Los coeficientes de rigidez están expresados en N/mm y las fuerzas en N.

Se desea resolver el sistema mediante el método de Gauss-Seidel en Python.

### 2. Datos ingresados por el usuario

Numero de ecuaciones: 3

Fila 1: 40 -10 0 20

Fila 2: -10 50 -10 60

Fila 3: 0 -10 40 100

### 3. Procedimiento del programa

1. Recibe el número de ecuaciones.
2. Solicita los valores de la matriz aumentada.
3. Verifica los elementos de la diagonal principal.
4. Asigna valores iniciales de cero.
5. Realiza las iteraciones del método de Gauss-Seidel.
6. Utiliza inmediatamente cada nuevo valor calculado.
7. Calcula el error porcentual.
8. Repite hasta alcanzar la tolerancia del 0.01%.
9. Muestra los desplazamientos calculados.

### Desarrollo matemático

Despejamos:

x1 = (20 + 10x2) / 40

x2 = (60 + 10x1 + 10x3) / 50

x3 = (100 + 10x2) / 40

Valores iniciales:

x1 = 0

x2 = 0

x3 = 0

**Primera iteración:**

x1 = (20 + 10(0)) / 40

x1 = 0.5000

x2 = (60 + 10(0.5) + 10(0)) / 50

x2 = 1.3000

x3 = (100 + 10(1.3)) / 40

x3 = 2.8250

**Segunda iteración:**

x1 = (20 + 10(1.3)) / 40

x1 = 0.8250

x2 = (60 + 10(0.825) + 10(2.825)) / 50

x2 = 1.9300

x3 = (100 + 10(1.93)) / 40

x3 = 2.9825

Se continúa con las siguientes iteraciones hasta obtener resultados estables.

### 4. Resultados obtenidos

Convergencia alcanzada.

RESULTADOS:

x1 = 1.0000

x2 = 2.0000

x3 = 3.0000

Iteraciones: 7

Error relativo máximo: 0.0016%

### 5. Comprobación

Primera ecuación:

40(1) - 10(2) = 20

40 - 20 = 20 ✓

Segunda ecuación:

-10(1) + 50(2) - 10(3) = 60

-10 + 100 - 30 = 60 ✓

Tercera ecuación:

-10(2) + 40(3) = 100

-20 + 120 = 100 ✓

### 6. Interpretación automotriz

Los desplazamientos calculados son:

Punto 1 = 1 mm

Punto 2 = 2 mm

Punto 3 = 3 mm

Estos resultados representan las deformaciones de los tres puntos del modelo simplificado de suspensión bajo las fuerzas aplicadas.

### 7. Conclusión

Mediante el método de Gauss-Seidel se determinaron los desplazamientos de tres puntos de un sistema de resortes acoplados.

El usuario únicamente ingresó los valores de la matriz aumentada y el programa realizó automáticamente siete iteraciones hasta alcanzar la tolerancia establecida.

Este método puede utilizarse para analizar modelos matemáticos de suspensiones y otros sistemas mecánicos automotrices.

---

# REFERENCIA BIBLIOGRÁFICA

Chapra, S. C., y Canale, R. P. (2015). Métodos numéricos para ingenieros (7.ª edición). McGraw-Hill.

Capítulo 11: Matrices especiales y el método de Gauss-Seidel.

Sección 11.2: Método de Gauss-Seidel.

Nota: Los ejemplos automotrices son modelos didácticos adaptados para fines educativos, no mediciones realizadas en un vehículo real.
