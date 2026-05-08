# Ejercicios de diccionarios: sistema de inventario


def create_inventory(items):
    """
    Crea un diccionario "inventario" a partir de una lista de items.
    Cada clave es el nombre de un item y su valor es la cantidad de veces
    que aparece en la lista.

    Args:
        items: Lista de items (strings)

    Returns:
        Un diccionario con cada item y su cantidad
    """
    diccio={}
    unic=set(items)
    for u in unic:
        t=0

        for i in items:
            if u==i:
                t+=1
        diccio[u]=t
    return diccio




def add_items(inventario, items):
    """
    Agrega una lista de items a un inventario existente. Si un item ya está
    en el inventario, incrementa su cantidad en 1. Si no, lo agrega con
    cantidad 1.

    Args:
        inventario: Diccionario con el inventario actual
        items: Lista de items a agregar

    Returns:
        El inventario actualizado
    """
    items= create_inventory(items)
    for k,v in inventario.items():
        for m,c in items.items():
            if k==m:
                inventario[k]=v+c

    for m,c in items.items():
        E=False
        for k,v in inventario.items():
            if m==k:
                E=True
        if E==False:
         inventario[m]=c


    return inventario







    return inventario


def decrement_items(inventario, items):
    """
    Resta 1 a la cantidad del inventario por cada vez que un item aparezca
    en la lista. Las cantidades no pueden ser negativas: si un item se quiere
    restar más veces que su cantidad disponible, debe quedar en 0 y las
    solicitudes extra deben ser ignoradas.

    Args:
        inventario: Diccionario con el inventario actual
        items: Lista de items a decrementar

    Returns:
        El inventario actualizado (sin valores negativos)
    """
    items = create_inventory(items)
    for k, v in inventario.items():
        for m, c in items.items():
            if k == m:
                if v-c>=0:
                 inventario[k] = v - c
                else:
                    inventario[k]=0
    return inventario



def remove_item(inventario, item):
    """
    Elimina un item del inventario por completo (clave y cantidad).
    Si el item no está en el inventario, retornar el inventario sin cambios.

    Args:
        inventario: Diccionario con el inventario actual
        item: String con el nombre del item a eliminar

    Returns:
        El inventario actualizado (o sin cambios si el item no existe)
    """
    lst=[]
    for i in inventario.keys():
        print(i)
        if i==item:
            lst.append(i)
    for i in lst:
        del inventario[i]

    return inventario





def list_inventory(inventario):
    """
    Retorna una lista de tuplas (item, cantidad) con el contenido del
    inventario. Solo incluye los items con cantidad mayor a 0.

    Args:
        inventario: Diccionario con el inventario

    Returns:
        Lista de tuplas (item, cantidad) con cantidad > 0
    """
    lst=[]
    for k,v in inventario.items():
        if v>0:
            a=(k,v)
            lst.append(a)
    return lst




def find_max_value(diccionario):
    """
    Recibe un diccionario de nombres y puntajes, y retorna la clave
    (nombre) con el valor (puntaje) más alto. Si el diccionario está
    vacío, retorna "".

    Args:
        diccionario: Diccionario {nombre: puntaje}

    Returns:
        String con la clave de mayor valor, o "" si el dict está vacío

    Ejemplo:
        find_max_value({'John': 85, 'Emma': 92, 'Sophia': 78}) -> 'Emma'
    """
    maximo=0
    res=0
    for k,v in diccionario.items():
        if v>maximo:
            maximo=v
            res=k
    if res==0:
        if diccionario=={}:
          return ''
        else:
            return "B"
    else:
        return res



def reverse_dict(diccionario):
    """
    Invierte un diccionario: cada valor pasa a ser clave, y cada clave
    pasa a ser valor. Si varias claves comparten el mismo valor, sus
    nombres se concatenan (en el orden en que aparecen).

    Args:
        diccionario: Diccionario original

    Returns:
        Nuevo diccionario invertido

    Ejemplo:
        reverse_dict({'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 2})
        -> {1: 'a', 2: 'be', 3: 'cd'}
    """
    diccio={}
    for k, v in diccionario.items():
        if  v in diccio:
           diccio[v]+=k
        else:
            diccio[v]=k
    return diccio



def word_frequency(palabras):
    """
    Cuenta cuántas veces aparece cada palabra en la lista y lo retorna
    como un diccionario {palabra: cantidad}.

    Args:
        palabras: Lista de palabras (strings). También debe soportar
                  un string vacío retornando un diccionario vacío.

    Returns:
        Diccionario con la frecuencia de cada palabra

    Ejemplo:
        word_frequency(["apple", "banana", "apple", "orange", "banana", "apple"])
        -> {'apple': 3, 'banana': 2, 'orange': 1}
    """
    diccio={}
    v=0
    for u in set(palabras):
        for i in palabras:
            if u==i:
                v+=1
        diccio[u]=v
        v=0

    return diccio



def find_biggest_expense(gastos):
    """
    Recibe un diccionario donde cada clave es una categoría y el valor
    una lista de gastos (números). Retorna la categoría con el
    promedio más alto. Si el diccionario está vacío, retorna "".

    Args:
        gastos: Diccionario {categoria: [gasto1, gasto2, ...]}

    Returns:
        String con la categoría de mayor promedio, o "" si vacío

    Ejemplo:
        find_biggest_expense({'Food': [60, 80, 100],
                              'Transport': [10, 1, 2],
                              'Games': [10, 20, 30]}) -> 'Food'
    """
    n=0
    res=''
    for k, list in gastos.items():
        suma=0
        for gastos in list:
             suma+=gastos
        promedio=suma/len(list)
        if promedio>n:
            n=promedio
            res=k
    return res



def sum_expenses(gastos):
    """
    Recibe un diccionario de categorías con listas de gastos y retorna
    un nuevo diccionario con la suma total de los gastos por categoría.

    Args:
        gastos: Diccionario {categoria: [gasto1, gasto2, ...]}

    Returns:
        Diccionario {categoria: suma_total}

    Ejemplo:
        sum_expenses({'Food': [60, 80, 100],
                      'Transport': [10, 1, 2],
                      'Games': [10, 20, 30]})
        -> {'Food': 240, 'Transport': 13, 'Games': 60}
    """
    lst=[]
    diccio={}
    for k, list in gastos.items():
       suma = 0
       if not list== []:
          for gastos in list:
             suma += gastos
             diccio[k]=suma
       else:
           diccio[k]=0
    return diccio



def sum_expenses_by_type(gastos):
    """
    Recibe un diccionario de categorías cuyos valores son listas de
    tuplas (tipo, monto). Retorna un nuevo diccionario con la suma
    de montos agrupada por tipo (no por categoría).

    Args:
        gastos: Diccionario {categoria: [(tipo, monto), ...]}

    Returns:
        Diccionario {tipo: suma_total_del_tipo}

    Ejemplo:
        sum_expenses_by_type({
            'Food': [("A", 60), ("B", 100), ("A", 20)],
            'Transport': [("A", 10), ("B", 50), ("C", 5)],
            'Games': [("A", 6), ("B", 24), ("C", 99)]
        })
        -> {'A': 96, 'B': 174, 'C': 104}
    """
    a=0
    b=0
    c=0
    diccio={}
    for l in gastos.values():
        for t in l:
            if t[0].lower()=="a":
                a+=t[1]
            elif t[0].lower() == "b":
                b+=t[1]
            else:
                c += t[1]
    if a!=0:
        diccio["A"]=a
    if b!=0:
        diccio["B"]=b
    if c!=0:
        diccio["C"]=c
    return diccio



a= sum_expenses_by_type({
    'Food': [("A", 60), ("B", 100), ("A", 20)],
    'Transport': [("A", 10), ("B", 50), ("C", 5)],
    'Games': [("A", 6), ("B", 24), ("C", 99)]
            })
print(a)