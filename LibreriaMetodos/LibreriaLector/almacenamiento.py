base_datos = {
    "modulo": [],
    "elemento": [],
    "registro": []
}


def obtener_lista(objeto):
    """
    Devuelve la lista asociada al objeto.
    """
    if objeto not in base_datos:
        base_datos[objeto] = []
    return base_datos[objeto]


def limpiar_almacenamiento():
    """
    Vacía todo el almacenamiento interno.
    """
    for clave in base_datos:
        base_datos[clave].clear()