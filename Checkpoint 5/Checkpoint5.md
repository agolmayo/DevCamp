# Checkpoint 5

## ¿Qué es un condicional?

En Python, un condicional es una estructura que permite al programa ejecutar diferentes bloques de código dependiendo de si una condición es verdadera o falsa. Gracias a ellos, el código puede ejecutar acciones diferentes dependiendo de ciertas condiciones. Sin condicionales, un programa ejecutaría siempre las mismas instrucciones en el mismo orden.

Las condicionales que se usan principalmente son:

- `if`
- `elif`
- `else`

### Condicional `if`

Con la estructura `if`, Python basicamente evalua si una condición se cumple o no, si lo hace, ejecutará el bloque indentado, si no lo hace, lo ignora.

### Condicional `else`

Con la estructura `else`, estamos pidiendo que se ejecute algo en caso de que la condicinal `if` no se cumpla, básicamente le estamos diciendo que si no se cumple x condición, haga otra cosa.

### Ejemplo

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

En este caso, si la variable edad es igual o superior al valor 18, el programa nos devolvera el string "Eres mayor de edad", si eso no se cumple, nos mostrará "Eres menor de edad". Como en este caso si que se cumple, ocurrira el primer caso.

### Condicional `elif`:

La estructura `elif` es una combinación entre `else` e `if`, y sirve para evaluar varias condiciones. Básicamente, lo que estamos diciendo es: si no se cumple una condición, pero esta otra sí, entonces haz esto.

### Ejemplo

```python
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

En este caso `elif` nos sirve para evaluar distintas opciónes, si la condicion de que la variable nota no cumple el >=9, el programa pasará a observar si se cumple el siguiente, el >=5, y nos devolvera "Aprobado".

---

## ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

Los bucles  o loops, permiten repetir instrucciones varias veces sin escribir el mismo código repetidamente. Son útiles para automatizar tareas, recorrer colecciones de datos y crear programas más dinámicos.

### Bucle `for`

Se utiliza para recorrer elementos de una secuencia como listas, cadenas o rangos. Permite recorrer listas y collecciones de forma fácil, ejecutar una acción un número determinado de veces y procesar los datos uno por uno.

#### Ejemplo

```python
frutas = ["manzana", "pera", "uva"]

for fruta in frutas:
    print(fruta)
```

La respuesta que tendriamos sería la siguiente:

```python
manzana
pera
uva
```
También es común el usar rangos, range(). Esto nos indicara cada elemento que se encuentre dentro del rango asignado.

#### Ejemplo

```python
for numero in range(5):
    print(numero)
```
Resultado:

```python
0
1
2
3
4
```

### Bucle `while`

Con la estructura `while`, el bucle se ejecutará y repetirá instrucciones siempre y cuando la condición establecida sea verdadera:

#### Ejemplo

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```
En este caso, el bucle se ejecutará mientras el valor de contador sea inferior a 5.

### `Break`,`continue` y `pass`

Son instrucciones que permiten controlar la continuidad del bucle. Por ejemplo, `break` nos permite detener el bucle completamente y saltar a la siguiente iteración. Con `continue`, omitimos directamente la iteración actual y saltamos al inicio de la siguiente iteración. En cambio, la instrucción `pass` es una declaración nula que no hace nada y se usa como marcador de posición o para mantener la estructura del código sin ejecutar acciones.

#### Ejemplo

`Break`
```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Respuesta: 0, 1, 2, 3, 4
```

`Continue`
```python
for i in range(10):
    if i == 5:
        continue
    print(i)
# Respuesta: 0, 1, 2, 3, 4, 6, 7, 8, 9
```

`Pass`
```python
for i in range(5):
    if i == 2:
        pass
    print(i)
# Respuesta: 0, 1, 2, 3, 4
```

### ¿Por qué son útiles?

Los bucles permiten repetir instrucciones automáticamente sin tener que escribir el mismo código muchas veces. Gracias a ellos, es posible procesar grandes cantidades de datos de manera rápida y eficiente. También ayudan a simplificar los programas, haciendo que el código sea más corto, ordenado y fácil de mantener. Además, los bucles son fundamentales para tareas comunes como recorrer listas, realizar cálculos repetitivos o crear programas interactivos.

En resumen:

- Automatizan tareas repetitivas.
- Reducen la cantidad de código.
- Permiten recorrer datos fácilmente.
- Mejoran la eficiencia del programa.

---

## ¿Qué es una lista por comprensión en Python?

Una lista por comprensión en Python es una forma corta y sencilla de crear listas a partir de otras secuencias, como listas o rangos. Permite generar una nueva lista en una sola línea de código, haciendo los programas más claros y eficientes. Su estructura combina un bucle `for` y, opcionalmente, una condición `if`, lo que hace que el código sea más corto, limpio y fácil de entender. 

Mediante as listas por comprensión se pueden crear listas de una forma más rápida, simple y ordenada, ayudando a escribir menos código y haciendo que los programas sean más fáciles de leer y mantener. Además, permiten combinar bucles y condiciones en una sola línea, lo que mejora la eficiencia al trabajar con datos. Son muy utilizadas para transformar, filtrar o procesar elementos dentro de listas de manera práctica.

### Ejemplo

```python
numeros = [1, 2, 3, 4, 5]

cuadrados = [n**2 for n in numeros]

print(cuadrados)
```
El programa recorre los números del 1 al 5 y guarda en una nueva lista el cuadrado de cada número. El resultado sería el siguiente:

```python
[1, 4, 9, 16, 25]
```

---

## ¿Qué es un argumento en Python?

Los argumentos son los valores reales que se pasan a una función durante su llamada, mientras que los `parámetros` son las variables definidas en la declaración de la función que reciben dichos valores. Estos valores permiten que la función trabaje con datos específicos en cada ejecución, en lugar de usar siempre la misma información.

### Ejemplo

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Carlos")
```

En este ejemplo:

- `nombre` es el parámetro.
- `"Carlos"` es el argumento.

Los argumentos permiten que las funciones trabajen con diferentes datos.

Existen varios tipos de argumentos: 

- Argumentos posicionales
- Argumentos de palabras clave
- Argumentos obligatorios
- Argumentos opcionales

### Argumentos posicionales
Argumentos que se pueden llamar por su posición en la definición de la función:

```python
def saludar(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años")

saludar("Ana", 25)
```
"Ana" va a nombre y 25 va a edad por posición.

### Argumentos de palabras clave
Son argumentos que se pueden llamar por su nombre, esto es, se pasan usando el nombre del parámetro. Aquí el orden no importa porque se usan nombres.

```python
def saludar(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años")

saludar(edad=25, nombre="Ana")
```

### Argumentos obligatorios
Son argumentos que se deben pasar a la función.
```python
def sumar(a, b):
    return a + b

print(sumar(3, 5))
```
En este caso, a y b son obligatorios. Si no se pasan, no funciona.

### Argumentos opcionales
Son argumentos que no es necesario especificar. En Python, los argumentos opcionales tienen un valor predeterminado.
```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}")

saludar("Ana")
saludar("Ana", "Buenos días")
```
En este caso, si no envías saludo, se devolvera "Hola" por defecto.

---

## ¿Qué es una función Lambda en Python?

Una función `lambda` en Python es una función anónima,sin nombre, que se escribe en una sola línea y se usa para tareas simples. Típicamente se definen en una línea y suelen tener un código a ejecutar pequeño. Según la documentación oficial de Python: “las funciones lambda son simplemente una versión acortada, que puedes usar si te da pereza escribir una función” .

### Sintaxis

```python
lambda argumentos: expresión
```

### Ejemplo
Lo que sería una función que suma dos números como la siguiente.
```python
def suma(a, b):
    return a+b
```
Se podría expresar en forma de una función `lambda` de la siguiente manera:
```python
lambda a, b : a + b
```
### Características

Una función `lambda` no tiene un nombre, y por lo tanto salvo que sea asignada a una variable, es totalmente inútil. Para ello debemos asignarla para que sea posible llamarla como si de una función normal se tratase.

```python
suma = lambda a, b: a + b
```
Las funciones `lambda` pueden ser la entrada a una función normal, y viceversa.

```python
def mi_funcion(lambda_func):
    return lambda_func(2,4)

mi_funcion(lambda a, b: a + b)
```

```python
def mi_otra_funcion(a, b):
    return a + b

(lambda a, b: mi_otra_funcion(a, b))(2, 4)
```

En las funciones `lambda`, se puede tener argumentos con valor asignado por defecto, asi como pasar los parámetros indicando su nombre o tener un número variable de argumentos haciendo uso de *.

```python
(lambda a, b, c=3: a + b + c)(1, 2) # 6
```

```python
(lambda a, b, c: a + b + c)(a=1, b=2, c=3) # 6
```

```python
(lambda *args: sum(args))(1, 2, 3) # 6
```

---

## ¿Qué es un paquete pip?

`pip` es el gestor de paquetes estándar para  Python, diseñado para instalar, actualizar, desinstalar y gestionar bibliotecas de terceros. Un paquete pip sería cualquier biblioteca o módulo que está disponible en el repositorio de Python y se puede instalar con pip.

En otras palabras, un paquete pip:

- Es código reutilizable (funciones, clases, herramientas).
- Está preparado para instalarse con un solo comando.
- Suele estar publicado en el repositorio oficial de Python.


### Ejemplo de instalación

```bash
pip install [nombre-paquete]
```
En nombre-paquete tendriamos que incluir el paquete pip específico qeu queremos usar, por ejemplo:

```bash
pip install numpy
```

Además, cuando instalas un paquete, PIP también instala todas las librerías que ese paquete necesita para funcionar.


### Comandos pip:

Aparte de la instalación, con pip tenemos varios comandos distintos que nos permiten gestionar nuestros paquetes pip de distintas formas:

- Listar un paquete:
```bash
pip list
```
- Actualizar un paquete:
```bash
pip install --upgrade nombre_paquete
```
- Desinstalar un paquete:
```bash
pip uninstall nombre_paquete
```
- Verificar la versión de un paquete:
```bash
pip --version
```

### Ejemplos de paquetes pip

Varios de los paquetes más comunes que suelen instalarase con `pip` son:

- `requests`: permite hacer peticiones HTTP.
- `numpy`: para cálculos númericos.
- `pandas`: para análisis de datos.
- `flask`: para crear APIs web.
- `django`: para frameworks más completos.

Una vez instalados, estos paquetes se pueden importar al código para poder hacer uso de sus funcionalidades: 

```python
import pandas as pd

data = pd.DataFrame({"nombre": ["Ana", "Luis"], "edad": [25, 30]})
print(data)
```