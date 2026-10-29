# Métodos Numéricos — Sistemas de ecuaciones lineales

Repositorio de apoyo para el **problemario T3–E2** de Ingeniería en Sistemas Automotrices.

## Métodos seleccionados

1. Eliminación gaussiana con pivoteo parcial.
2. Jacobi.
3. Gauss-Seidel.

Los tres programas están escritos en **Python**, permiten ingresar una matriz aumentada por teclado y muestran las incógnitas con cuatro decimales.

## Archivos

- [eliminacion_gaussiana.py](eliminacion_gaussiana.py): método directo con pivoteo parcial.
- [jacobi.py](jacobi.py): método iterativo que usa los valores anteriores.
- [gauss_seidel.py](gauss_seidel.py): método iterativo que actualiza cada incógnita inmediatamente.
- [pruebas.py](pruebas.py): 18 pruebas automatizadas.
- [PSEUDOCODIGOS.md](PSEUDOCODIGOS.md): pseudocódigo de los tres algoritmos.
- [Apunte de eliminación gaussiana](apuntes/eliminacion_gaussiana.md).
- [Apunte de Jacobi](apuntes/jacobi.md).
- [Apunte de Gauss-Seidel](apuntes/gauss_seidel.md).

## Cómo ejecutar

Se requiere Python 3. No hace falta instalar bibliotecas adicionales.

En una terminal, desde la carpeta del repositorio:

```bash
python eliminacion_gaussiana.py
python jacobi.py
python gauss_seidel.py
python pruebas.py
```

En algunos equipos debe utilizarse `python3` en lugar de `python`.

Al ejecutar cualquiera de los tres métodos, primero se ingresa el número de ecuaciones; después, una fila por línea con los coeficientes y el término independiente al final.

Ejemplo para el sistema `3x + 2y = 18` y `-x + 2y = 2`:

```text
Numero de ecuaciones: 2
Fila 1: 3 2 18
Fila 2: -1 2 2
```

Para comprobar los métodos:

```bash
python pruebas.py
```

## Casos de prueba

El archivo `pruebas.py` incluye **seis casos para cada método**:

- G1–G4, J1–J4 y S1–S4: resultados correctos.
- G5–G6, J5–J6 y S5–S6: casos que muestran limitaciones del método o del sistema.

**Total:** 18 casos; 12 correctos y 6 de limitación.

En los casos de limitación, `False` significa que se espera que el programa **no devuelva una solución numérica**. No representa una ejecución incorrecta del programa.

Las pruebas contemplan sistemas dependientes o incompatibles, diagonal cero y divergencia de las iteraciones.

Al ejecutar los cuatro archivos fuente equivalentes se obtuvo: `18 de 18 pruebas verificadas.`

## Notas para el problemario

- El código fuente se entrega como archivos de texto `.py`, no como imágenes.
- Los ejemplos automotrices son modelos didácticos; no representan mediciones reales.
- El **PDF del problemario** y el **análisis escrito en la libreta** se entregan según lo que indique el docente. Los archivos de GitHub no sustituyen esos requisitos.
- En la actividad se solicita más de cinco pruebas por método y también se menciona un máximo de diez ejercicios desarrollados. El problemario puede presentar 9 ejercicios completos y documentar las 18 pruebas adicionales, sujeto a confirmación del docente.

## Referencia

Chapra, S. C., y Canale, R. P. (2015). *Métodos numéricos para ingenieros* (7.ª ed.). McGraw-Hill.
