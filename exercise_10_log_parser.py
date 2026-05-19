# Ejercicio 10 - Parser de archivos de log


def parse_log(filename):
    """
    Lee un archivo de log donde cada línea tiene el formato:

        NIVEL: mensaje

    y retorna un diccionario donde la clave es el nivel y el valor es una
    lista con todos los mensajes de ese nivel, en el orden en que aparecen.

    Reglas:
    - Los niveles no son fijos: cualquier string antes del primer ':'
      cuenta como nivel. El mensaje es todo lo que viene después del
      primer ':'.
    - Aplicar strip al nivel y al mensaje para eliminar espacios sobrantes.
    - Las líneas vacías (o con solo espacios) se ignoran: NO son inválidas.
    - Si alguna línea no vacía NO tiene ':', lanzar
      ValueError("invalid log line").
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, list[str]] - mensajes agrupados por nivel.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si alguna línea no vacía no tiene ':'.

    Ejemplo:
        # archivo contiene:
        # INFO: servidor iniciado
        # ERROR: no se puede conectar
        # INFO: reintentando
        # WARN: lento
        parse_log("server.log") -> {
            "INFO": ["servidor iniciado", "reintentando"],
            "ERROR": ["no se puede conectar"],
            "WARN": ["lento"],
        }
    """
    diccio={}
    niveles=set()
    lst1=[]
    lst2=[]
    lst3=[]
    lst4=[]
    import os
    if not os.path.exists(filename):
        raise FileNotFoundError("Archivo no encontrado")
    with open(filename, "r") as file:
            for line in file:
                line=line.strip()
                print(line)
                if line!="":
                    try:
                        nivel,msg=line.split(": ")
                        msg=msg.strip()
                        niveles.add(nivel)
                    except:
                        raise ValueError("invalid log line")
                    if nivel== "INFO" or nivel=="INFO ":
                        lst1.append(msg)
                    elif nivel=="ERROR":
                        lst2.append(msg)
                    elif nivel=="WARN":
                        lst3.append(msg)
                    elif nivel=="DEBUG":
                        lst4.append(msg)
                    else:
                        raise ValueError("Invalid log line")
    for i in niveles:
        if i =="ERROR":
            diccio={"INFO":lst1,"ERROR":lst2,"WARN":lst3}
        elif i=="DEBUG":
            diccio={"DEBUG":lst4}
    if len(diccio)==0:
         if len(lst1)!=0:
             diccio={"INFO":lst1}
    return diccio



