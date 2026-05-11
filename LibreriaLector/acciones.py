from .almacenamiento import (
    agregar_elemento,
    eliminar_elemento,
    existe_elemento,
    contar_elementos,
    vaciar_objeto,
    obtener_lista
)


def _plural(objeto):
    return f"{objeto}s"


def crear(datos):
    objeto = datos["objeto"]
    nombre = datos["nombre"]
    if agregar_elemento(objeto, nombre):
        return f"{objeto.capitalize()} {nombre} creado correctamente"
    return f"{objeto.capitalize()} {nombre} ya existe"


def eliminar(datos):
    objeto = datos["objeto"]
    nombre = datos["nombre"]
    if eliminar_elemento(objeto, nombre):
        return f"{objeto.capitalize()} {nombre} eliminado correctamente"
    return f"{objeto.capitalize()} {nombre} no existe"


def listar(datos):
    objeto = datos["objeto"]
    lista = obtener_lista(objeto)
    if not lista:
        return f"No hay {_plural(objeto)} registrados"
    return f"{_plural(objeto).capitalize()}: {', '.join(lista)}"


def buscar(datos):
    objeto = datos["objeto"]
    nombre = datos["nombre"]
    if existe_elemento(objeto, nombre):
        return f"{objeto.capitalize()} {nombre} encontrado"
    return f"{objeto.capitalize()} {nombre} no encontrado"


def contar(datos):
    objeto = datos["objeto"]
    cantidad = contar_elementos(objeto)
    return f"Cantidad de {_plural(objeto)}: {cantidad}"


def vaciar(datos):
    objeto = datos["objeto"]
    vaciar_objeto(objeto)
    return f"{_plural(objeto).capitalize()} vaciados correctamente"


def mostrar(datos):
    objeto = datos["objeto"]
    nombre = datos.get("nombre", "").strip()
    if objeto == "pantalla":
        if nombre:
            return f"Mostrando en pantalla: {nombre}"
        return "Mostrando en pantalla"
    if nombre:
        return f"Mostrando {objeto}: {nombre}"
    return f"Mostrando {objeto}"
