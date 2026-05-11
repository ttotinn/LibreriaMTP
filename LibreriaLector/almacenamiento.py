# Estado interno de la librería.
# Vive en memoria mientras el programa esté ejecutándose.

_CATEGORIAS_DEFAULT = ("modulo", "elemento", "registro")

base_datos: dict[str, list] = {cat: [] for cat in _CATEGORIAS_DEFAULT}


def obtener_base_datos():
    """
    Devuelve toda la estructura interna.
    """
    return base_datos


def obtener_lista(objeto):
    """
    Devuelve la lista de un tipo de objeto.
    Si no existe todavía, la crea.
    """
    if objeto not in base_datos:
        base_datos[objeto] = []

    return base_datos[objeto]


def agregar_elemento(objeto, nombre):
    """
    Agrega un nombre a la lista correspondiente.
    Retorna True si se agregó, False si ya existía.
    """
    lista = obtener_lista(objeto)

    if nombre in lista:
        return False

    lista.append(nombre)
    return True


def eliminar_elemento(objeto, nombre):
    """
    Elimina un nombre de la lista correspondiente.
    Retorna True si lo eliminó, False si no existía.
    """
    lista = obtener_lista(objeto)

    if nombre not in lista:
        return False

    lista.remove(nombre)
    return True


def existe_elemento(objeto, nombre):
    """
    Verifica si el elemento existe.
    """
    return nombre in obtener_lista(objeto)


def contar_elementos(objeto):
    """
    Cuenta cuántos elementos hay.
    """
    return len(obtener_lista(objeto))


def vaciar_objeto(objeto):
    """
    Vacía completamente la lista de un objeto.
    """
    obtener_lista(objeto).clear()


def limpiar_almacenamiento():
    """
    Vacía todo el almacenamiento interno,
    incluyendo categorías dinámicas creadas en tiempo de ejecución.
    """
    for clave in list(base_datos.keys()):
        base_datos[clave].clear()
