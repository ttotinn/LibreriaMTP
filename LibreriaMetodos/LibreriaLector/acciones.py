from LibreriaLector.almacenamiento import obtener_lista


def _plural(objeto):
    return f"{objeto}s"


def crear(datos):
    objeto = datos["objeto"]
    nombre = datos["nombre"]

    lista = obtener_lista(objeto)

    if nombre in lista:
        return f"{objeto.capitalize()} {nombre} ya existe"

    lista.append(nombre)
    return f"{objeto.capitalize()} {nombre} creado correctamente"


def eliminar(datos):
    objeto = datos["objeto"]
    nombre = datos["nombre"]

    lista = obtener_lista(objeto)

    if nombre not in lista:
        return f"{objeto.capitalize()} {nombre} no existe"

    lista.remove(nombre)
    return f"{objeto.capitalize()} {nombre} eliminado correctamente"


def listar(datos):
    objeto = datos["objeto"]
    lista = obtener_lista(objeto)

    if not lista:
        return f"No hay {_plural(objeto)} registrados"

    return f"{_plural(objeto).capitalize()}: {', '.join(lista)}"


def buscar(datos):
    objeto = datos["objeto"]
    nombre = datos["nombre"]

    lista = obtener_lista(objeto)

    if nombre in lista:
        return f"{objeto.capitalize()} {nombre} encontrado"

    return f"{objeto.capitalize()} {nombre} no encontrado"