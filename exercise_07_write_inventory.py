# Ejercicio 7 - Escribir un inventario ordenado


def write_inventory(filename, inventory):
    """
    Escribe el inventario en un archivo, una línea por item, ordenadas
    alfabéticamente por nombre de item, con el formato:

        item:cantidad

    Reglas:
    - Cada línea debe terminar con "\\n".
    - Si el diccionario está vacío, el archivo se crea vacío.
    - Si el archivo ya existía, se sobreescribe.
    - La función no retorna nada (None).

    Args:
        filename: str - nombre del archivo a escribir.
        inventory: dict[str, int] - item -> cantidad.

    Returns:
        None

    Ejemplo:
        write_inventory("stock.txt", {"wood": 10, "coal": 3, "iron": 7})
        # El archivo stock.txt queda con:
        # coal:3
        # iron:7
        # wood:10
    """

    ordenlist=[]
    contador=0
    for k,v in inventory.items():
        line=f"{k}:{v}"
        if ordenlist== []:
            ordenlist.append(line)
        else:
            hecho=False
            for i in range(len(ordenlist)):
                if line<ordenlist[i]:
                    ordenlist.insert(i,line)
                    hecho=True
            if hecho==False:
                 ordenlist.append(line)
    with open(filename, "w") as file:
        for line in ordenlist:
            file.write(f"{line}\n")


    return None







