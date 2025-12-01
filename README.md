# Analizador de Texto

Este proyecto implementa un **analizador de texto** en Python que procesa un archivo y permite realizar búsquedas, obtener frecuencias, localizar líneas y más, utilizando **tres estructuras de datos fundamentales**:

* **Lista ligada** (para almacenar líneas del archivo)
* **HashMap** (para frecuencias e índice invertido)
* **Árbol binario de búsqueda** (para almacenar palabras ordenadas, sus frecuencias y líneas)

El programa incluye un menú interactivo que permite al usuario ejecutar todas las funciones del analizador.

---

## Opciones de ejecución

### ✔ Procesamiento de archivo

* Lee un archivo de texto línea por línea.
* Limpia cada palabra (solo letras y números).
* Inserta cada palabra en:

  * Lista ligada (solo líneas completas)
  * HashMap (frecuencias e índice invertido)
  * Árbol binario de búsqueda (orden y líneas donde aparece)

### ✔ Búsqueda de palabras

* Busca una palabra en el **árbol binario**.
* Devuelve su frecuencia total.

### ✔ Top-K palabras (árbol binario)

* Obtiene las *k* palabras más frecuentes del árbol binario.

### ✔ Líneas donde aparece una palabra

* Devuelve la lista de números de línea donde aparece una palabra.

### ✔ HashMap

* Muestra:

  * Frecuencias generales
  * Índice invertido

### ✔ Lista ligada

* Permite mostrar todas las líneas del archivo en el orden original.

---

##  Estructuras utilizadas

###  1. Lista Ligada

Almacena las líneas del archivo en orden.

* Inserción O(1)
* Recorrido O(n)

###  2. HashMap

Almacena:

* Frecuencia total de cada palabra.
* Índice invertido: en qué líneas aparece cada palabra.

Búsqueda e inserción: O(1) promedio.

###  3. Árbol Binario de Búsqueda (BST)

Cada nodo contiene:

* Palabra
* Frecuencia
* Listado de líneas
* Apuntadores izquierdo y derecho

Permite:

* Recorrido en orden (palabras ordenadas alfabéticamente)
* Inserciones eficientes

---

##  Cómo usar el programa e instrucciones de ejecución

1. Clonar el repositorio
    git clone https://github.com/AntwoneOrtega/Proyecto-Aguas-Estructura

2. Sube un archivo a tu carpeta clonada, el que desees analizar.

2. Entrar al directorio del proyecto:
    cd Proyecto-Aguas-Estructura

3. Ejecutar el programa principal:
    python Proyecto_Estructura.py

4. Usar el menú para:

* Procesar un archivo
* Buscar palabras
* Ver top-K
* Ver índice invertido
* Mostrar líneas, etc.

---

##  Vista del menú

```
=============== ANALIZADOR DE TEXTO ===============
1. Procesar archivo de texto
2. Buscar palabra
3. Top-K palabras (árbol binario)
4. Líneas donde aparece (árbol)
5. Frecuencias (hash map)
6. Índice invertido (hash map)
7. Mostrar líneas (lista ligada)
8. Salir
===================================================
```

---

##  Casos borde considerados

* Archivos vacíos
* Palabras repetidas múltiples veces
* Palabras con caracteres especiales
* Líneas vacías
* Archivos que no existen
* Búsquedas de palabras no presentes

---

##  Requisitos

* Python 3.10 o superior
* Un sistema operativo como Windows, Mac o Linux
* Aviso: Como es python, este programa no se compila.

---

## Autor

Proyecto hecho por:
* Luis Fernando Manzanares Catalán 0272513@up.edu.mx
* Leonardo Aguirre Durán 0270914@up.edu.mx
* Antwone Ortega Martínez <0244285@up.edu.mx>
