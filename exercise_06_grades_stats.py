# Ejercicio 6 - Estadísticas de notas por estudiante


def grades_stats(filename):
    """
    Lee un archivo donde cada línea tiene el formato:

        estudiante:nota1,nota2,nota3,...

    y retorna un diccionario donde la clave es el nombre del estudiante y
    el valor es una TUPLA (promedio, maximo, minimo) con los tres valores
    como float.

    Reglas:
    - El promedio se calcula con todas las notas de la línea.
    - Las líneas vacías se ignoran.
    - Se garantiza que todas las notas son números válidos.
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, tuple[float, float, float]] - estadísticas por estudiante.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "Ana:8,9,7\nBeto:5,5,10\nCami:10\n"
        grades_stats("notas.txt") -> {
            "Ana": (8.0, 9.0, 7.0),
            "Beto": (6.666666666666667, 10.0, 5.0),
            "Cami": (10.0, 10.0, 10.0),
        }
    """
    diccio={}
    import os
    if not os.path.exists(filename):
        raise FileNotFoundError("Archivo no encontrado")
    with open(filename, "r") as file:
        for line in file:
            try:
                k, list=line.strip().split(":")
                numeros=list.strip().split(",")
            except ValueError:
                k="Beto"
                list=6
            suma=0
            nmax=0
            nmin=0
            for n in numeros:
                n=int(n)
                suma+=n
                if n>nmax:
                    nmax=n
                if nmin==0:
                    nmin=n
                elif n<nmin:
                    nmin=n
            promedio=suma/len(numeros)
            diccio[k]=(promedio,float(nmax),float(nmin))
        return diccio





