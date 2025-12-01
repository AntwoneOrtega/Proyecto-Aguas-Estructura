class NodoLinea:
    def __init__(self, texto):
        self.texto = texto
        self.next = None

class ListaLigada:
    def __init__(self):
        self.head = None
        self.tail = None

    def agregar(self, texto):
        nuevo = NodoLinea(texto)
        if not self.head:
            self.head = self.tail = nuevo
        else:
            self.tail.next = nuevo
            self.tail = nuevo

    def obtener_todas(self):
        actual = self.head
        lineas = []
        while actual:
            lineas.append(actual.texto)
            actual = actual.next
        return lineas
class HashMap:
    def __init__(self):
        self.frecuencias = {}        
        self.indice_invertido = {} 

    def agregar_palabra(self, palabra, linea):
        if palabra not in self.frecuencias:
            self.frecuencias[palabra] = 1
        else:
            self.frecuencias[palabra] += 1

        if palabra not in self.indice_invertido:
            self.indice_invertido[palabra] = []
        self.indice_invertido[palabra].append(linea)
class Nodo:
    def __init__(self, palabra):
        self.palabra = palabra
        self.frecuencia = 1
        self.izq = None
        self.der = None
        self.lineas = []  

class ArbolPalabras:
    def __init__(self):
        self.raiz = None

    # Insertar palabra en el árbol
    def insertar(self, palabra, linea):
        self.raiz = self._insertar(self.raiz, palabra, linea)

    def _insertar(self, nodo, palabra, linea):
        # Caso base: nodo vacío
        if nodo is None:
            nuevo = Nodo(palabra)
            nuevo.lineas.append(linea)
            return nuevo

        if palabra < nodo.palabra:
            nodo.izq = self._insertar(nodo.izq, palabra, linea)
        elif palabra > nodo.palabra:
            nodo.der = self._insertar(nodo.der, palabra, linea)
        else:
            nodo.frecuencia += 1
            nodo.lineas.append(linea)

        return nodo

    def buscar(self, palabra):
        nodo = self.raiz
        while nodo:
            if palabra == nodo.palabra:
                return nodo
            elif palabra < nodo.palabra:
                nodo = nodo.izq
            else:
                nodo = nodo.der
        return None


def procesar_archivo(nombre, arbol, hashmap, lista_lineas):
    try:
        with open(nombre, "r", encoding="utf-8") as f:
            linea_num = 1

            for linea in f:
                lista_lineas.agregar(linea.strip())

                palabras = linea.lower().strip().split()

                for p in palabras:
                    p = ''.join(c for c in p if c.isalnum())
                    if p:
                        # Árbol binario
                        arbol.insertar(p, linea_num)
                        # Hash map
                        hashmap.agregar_palabra(p, linea_num)

                linea_num += 1

        print("\nArchivo procesado correctamente.\n")

    except FileNotFoundError:
        print("\nERROR: No se encontró el archivo.\n")



def obtener_lista_palabras(nodo, lista):
    if nodo:
        obtener_lista_palabras(nodo.izq, lista)
        lista.append((nodo.palabra, nodo.frecuencia))
        obtener_lista_palabras(nodo.der, lista)


def top_k(arbol, k):
    lista = []
    obtener_lista_palabras(arbol.raiz, lista)
    lista.sort(key=lambda x: x[1], reverse=True)
    return lista[:k]

def lineas_de(arbol, palabra):
    nodo = arbol.buscar(palabra)
    if nodo:
        return nodo.lineas
    return []


#   Menú principal
def menu():
    arbol = ArbolPalabras()
    hashmap = HashMap()
    lista_lineas = ListaLigada()

    while True:
        print("\n=============== ANALIZADOR DE TEXTO ===============")
        print("1. Procesar archivo de texto")
        print("2. Buscar palabra")
        print("3. Top-K palabras (árbol binario)")
        print("4. Líneas donde aparece (árbol)")
        print("5. Frecuencias (hash map)")
        print("6. Índice invertido (hash map)")
        print("7. Mostrar líneas (lista ligada)")
        print("8. Salir")
        print("===================================================")

        opcion = input("Opción: ")

        if opcion == "1":
            archivo = input("Nombre del archivo: ")
            procesar_archivo(archivo, arbol, hashmap, lista_lineas)

        elif opcion == "2":
            palabra = input("Palabra: ").lower()
            nodo = arbol.buscar(palabra)
            if nodo:
                print(f"'{palabra}' aparece {nodo.frecuencia} veces.")
            else:
                print("No aparece.")

        elif opcion == "3":
            k = int(input("K: "))
            for palabra, freq in top_k(arbol, k):
                print(f"{palabra}: {freq}")

        elif opcion == "4":
            palabra = input("Palabra: ").lower()
            print(lineas_de(arbol, palabra))

        elif opcion == "5":
            print(hashmap.frecuencias)

        elif opcion == "6":
            print(hashmap.indice_invertido)

        elif opcion == "7":
            for linea in lista_lineas.obtener_todas():
                print(linea)

        elif opcion == "8":
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()