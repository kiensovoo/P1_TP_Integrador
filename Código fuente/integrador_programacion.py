import time

def encontrar_valor(lista, valor):
    # Recorrer la lista secuencialmente
    for numero in lista: # se recorre n veces
        if numero == valor: # 1 operación n veces -> O(n)
            return True # O(1)
    return False # O(1)

def esta_en_lista(lista, valor):
    # El operador in realiza internamente una búsqueda secuencial optimizada
    return valor in lista # O(n)

# Creamos una lista con un rango de 10 millones
n = 10000000
mi_lista = list(range(n))

# Definimos los casos en un diccionario para luego recorrer cada caso.
casos = {
    "Mejor caso": mi_lista[0], #O(1) -> está al inicio
    "Caso promedio": mi_lista[n//2], #O(n) -> está a la mitad
    "Peor caso": -1 # O(n) -> inexistente
}

for caso, valor_a_buscar in casos.items():
    # Búsqueda manual con la primera función -> O(n)
    inicio = time.perf_counter() # Se guarda el tiempo preciso del inicio
    rta_encontrar = encontrar_valor(mi_lista, valor_a_buscar)
    fin = time.perf_counter() # Se guarda el tiempo preciso al finalizar
    tiempo_encontrar = (fin - inicio)*1000 # Convertir a ms

    # Búsqueda con la segunda función -> O(n)
    inicio = time.perf_counter()
    rta_lista = esta_en_lista(mi_lista, valor_a_buscar)
    fin = time.perf_counter()
    tiempo_esta_en_lista = (fin - inicio) * 1000

    # Imprimir los resultados e informar si se encontró o no el valor.
    print(f"{caso}-> 1ra Función: {tiempo_encontrar:.6f} ms | 2da Función: {tiempo_esta_en_lista:.6f} ms | ¿Encontrado? -> {rta_encontrar}")