# Pseudocódigos de los tres métodos

**Materia:** Métodos Numéricos  
**Referencia:** Chapra y Canale, *Métodos numéricos para ingenieros*, 7.ª edición.

## 1. Eliminación gaussiana con pivoteo parcial

```text
INICIO
  LEER n
  LEER matriz aumentada A (n filas, n+1 columnas)
  PARA i = 0 HASTA n-1
    BUSCAR la fila con mayor valor absoluto en la columna i
    SI el pivote es prácticamente cero
      INFORMAR que no hay solución única
      TERMINAR
    FIN SI
    INTERCAMBIAR la fila i con la fila del mejor pivote
    PARA cada fila j debajo del pivote
      factor = A[j,i] / A[i,i]
      RESTAR factor * fila i a fila j
    FIN PARA
  FIN PARA
  PARA i = n-1 HASTA 0 (hacia atrás)
    CALCULAR x[i] usando las incógnitas conocidas
  FIN PARA
  MOSTRAR x
FIN
```

## 2. Jacobi

```text
INICIO
  LEER n y matriz aumentada A
  VERIFICAR que la diagonal no contenga ceros
  ASIGNAR x_anterior = [0, 0, ..., 0]
  REPETIR hasta max_iter veces
    PARA cada ecuación i
      CALCULAR x_nuevo[i] utilizando SOLO x_anterior
    FIN PARA
    CALCULAR errores porcentuales y residuos
    SI todos los errores y residuos cumplen la tolerancia
      MOSTRAR x_nuevo y TERMINAR
    FIN SI
    SI las aproximaciones crecen excesivamente
      INFORMAR divergencia y TERMINAR
    FIN SI
    x_anterior = x_nuevo
  FIN REPETIR
  INFORMAR que no se alcanzó la tolerancia
FIN
```

## 3. Gauss-Seidel

```text
INICIO
  LEER n y matriz aumentada A
  VERIFICAR que la diagonal no contenga ceros
  ASIGNAR x_anterior = [0, 0, ..., 0]
  REPETIR hasta max_iter veces
    COPIAR x_anterior en x_nuevo
    PARA cada ecuación i, de arriba hacia abajo
      CALCULAR x_nuevo[i] usando los nuevos valores YA
      calculados y los anteriores para los que faltan
    FIN PARA
    CALCULAR errores porcentuales y residuos
    SI todos los errores y residuos cumplen la tolerancia
      MOSTRAR x_nuevo y TERMINAR
    FIN SI
    SI las aproximaciones crecen excesivamente
      INFORMAR divergencia y TERMINAR
    FIN SI
    x_anterior = x_nuevo
  FIN REPETIR
  INFORMAR que no se alcanzó la tolerancia
FIN
```

**Diferencia principal:** Jacobi utiliza exclusivamente los valores de la iteración anterior. Gauss-Seidel actualiza las incógnitas en la misma iteración.

**Condición de convergencia:** la dominancia diagonal estricta garantiza convergencia para estos métodos; cuando falta, la convergencia no está garantizada. Una diagonal sin ceros es necesaria para las fórmulas tal como están programadas.

**Criterio empleado en los archivos Python:** tolerancia de error relativo aproximado de 0.01 %, residuo máximo menor que 0.0001 y máximo de 100 iteraciones.
