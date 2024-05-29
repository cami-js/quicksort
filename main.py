def quicksort(lista):
    if len(lista) <= 1:  #Caso base: lista con 0 o 1 elementos
        return lista

    #Selección del pivote
    pivote = lista[0]

    #Partición de la lista
    izquierda = [x for x in lista[1:] if x < pivote]
    derecha = [x for x in lista[1:] if x >= pivote]

    #Llamadas recursivas
    if len(izquierda) > 0:  #Verificar si la sublista izquierda no está vacía
        lista_izquierda_ordenada = quicksort(izquierda)
    else:
        lista_izquierda_ordenada = []  #Si la sublista izquierda está vacía, se asigna una lista vacía

    if len(derecha) > 0:  #Verificar si la sublista derecha no está vacía
        lista_derecha_ordenada = quicksort(derecha)
    else:
        lista_derecha_ordenada = []  # Si la sublista derecha está vacía, se asigna una lista vacía

    #Combinación de resultados
    lista_ordenada = lista_izquierda_ordenada + [pivote] + lista_derecha_ordenada

    return lista_ordenada

#Ejemplo de uso
lista_ejemplo = [7, 3, 9, 5, 2, 67, 1]
lista_ordenada = quicksort(lista_ejemplo)
print(lista_ordenada)

#Asserts con ejemplos de uso
assert quicksort([4, 2, 7, 1, 3]) == [1, 2, 3, 4, 7], "Error: caso 1 fallido"
assert quicksort([10, 5, 2, 3, 7, 6, 4, 8, 9, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Error: caso 2 fallido"

print("Todos los asserts pasaron correctamente.")