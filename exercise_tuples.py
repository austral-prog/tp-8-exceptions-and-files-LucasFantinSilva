# Ejercicios de tuplas: búsqueda del tesoro pirata


def get_coordinate(registro):
    """
    Retorna la coordenada del mapa desde una tupla (tesoro, coordenada).

    Args:
        registro: Una tupla con el formato (tesoro, coordenada)

    Returns:
        Un string con la coordenada del mapa
    """
    tesoro=registro[0]
    coordenada=registro[1]
    return str(coordenada)


def convert_coordinate(coordenada):
    """
    Separa una coordenada de formato "2A" en sus componentes ("2", "A").

    Args:
        coordenada: Un string con la coordenada (ej: "2A", "7F")

    Returns:
        Una tupla con los componentes individuales (ej: ("2", "A"))
    """
    n=coordenada[:1]
    l=coordenada[1:]
    return (n, l)


def create_record(registro_azara, registro_rui):
    """
    Combina los registros de Azara y Rui si sus coordenadas coinciden.

    - Registro de Azara: (tesoro, coordenada) -> ej: ('Brass Spyglass', '4B')
    - Registro de Rui: (ubicacion, coordenada, cuadrante) ->
      ej: ('Abandoned Lighthouse', ('4', 'B'), 'Blue')

    Si las coordenadas coinciden, retornar una tupla combinada:
    (tesoro, coordenada_azara, ubicacion, coordenada_rui, cuadrante)

    Si NO coinciden, retornar el string "not a match".

    Args:
        registro_azara: Tupla (tesoro, coordenada)
        registro_rui: Tupla (ubicacion, coordenada, cuadrante)

    Returns:
        Tupla combinada si las coordenadas coinciden, o "not a match" si no.
    """
    c1=convert_coordinate(registro_azara[1])
    c2=registro_rui[1]
    if c1[0]==c2[0] and c1[1] ==c2[1]:
        dupla = (registro_azara[0], registro_azara[1], registro_rui[0], registro_rui[1], registro_rui[2])
        return dupla
    else:
        return "not a match"


def sum_tuple(numeros):
    """
    Recorre una tupla de números y retorna la suma total.
    Si la tupla está vacía, retorna 0.

    No se permite usar la función built-in sum(). Implementar la suma
    recorriendo la tupla con un for (o while).

    Args:
        numeros: Tupla de números (enteros o flotantes)

    Returns:
        La suma de todos los elementos de la tupla

    Ejemplo:
        sum_tuple((1, 2, 3, 4, 5)) -> 15
        sum_tuple(()) -> 0
    """
    suma=0
    for n in numeros:
        suma+=n

    return suma



def count_occurrences(tupla, elemento):
    """
    Recorre la tupla y cuenta cuántas veces aparece el elemento.

    No se permite usar el método .count(). Implementar el conteo
    recorriendo la tupla con un for (o while).

    Args:
        tupla: Tupla con elementos de cualquier tipo
        elemento: El elemento a contar

    Returns:
        La cantidad de veces que aparece el elemento (int)

    Ejemplo:
        count_occurrences((1, 2, 2, 3, 2), 2) -> 3
        count_occurrences(('a', 'b', 'a'), 'c') -> 0
    """
    count=0
    for i in tupla:
        if i==elemento:
            count+=1

    return count



def find_index(tupla, elemento):
    """
    Recorre la tupla y retorna el índice de la PRIMERA aparición del
    elemento. Si el elemento no se encuentra, retorna -1.

    No se permite usar el método .index(). Implementar la búsqueda
    recorriendo la tupla con un for (o while).

    Args:
        tupla: Tupla con elementos
        elemento: El elemento a buscar

    Returns:
        El índice (int) de la primera aparición, o -1 si no está

    Ejemplo:
        find_index(('a', 'd', 'c', 'b'), 'b') -> 1
        find_index((1, 2, 3), 9) -> -1
    """
    indice=0
    res=False
    for i in tupla:
      if i != elemento:
          indice+=1
      else:
          res=True
          return indice


    if res==False:
     return -1



def filter_positives(numeros):
    """
    Recorre una tupla de números y retorna una nueva tupla con solo
    los números positivos (> 0). El cero NO se considera positivo.

    Args:
        numeros: Tupla de números (enteros o flotantes)

    Returns:
        Tupla con los números positivos, en el orden original

    Ejemplo:
        filter_positives((-3, 1, 0, 5, -2, 7)) -> (1, 5, 7)
        filter_positives((-1, -2, -3)) -> ()
    """
    dupla=[]
    for n in numeros:
        if n>0:
            dupla.append(n)

    return tuple(dupla)

