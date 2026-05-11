from .analizador import interpretar, interpretar_comandos_compuestos, separar_comandos
from .reglas import validar_comando
from .acciones import crear, eliminar, listar, buscar, contar, vaciar, mostrar

ACCIONES = {
    "crear":   crear,
    "eliminar":eliminar,
    "listar":  listar,
    "buscar":  buscar,
    "contar":  contar,
    "vaciar":  vaciar,
    "mostrar": mostrar,
}


def interpretar_comando(texto):
    return interpretar(texto)


def validar_comando_texto(texto):
    datos = interpretar(texto)
    return validar_comando(datos)


def ejecutar_desde_datos(datos):
    valido, mensaje = validar_comando(datos)
    if not valido:
        return f"Error: {mensaje}"

    accion = datos["accion"]
    if accion not in ACCIONES:
        return "Error: acción no implementada"

    return ACCIONES[accion](datos)


def ejecutar(texto):
    datos = interpretar(texto)
    return ejecutar_desde_datos(datos)


def ejecutar_lote(comandos):
    return [ejecutar(comando) for comando in comandos]


def ejecutar_texto_compuesto(texto):
    interpretados = interpretar_comandos_compuestos(texto)
    return [ejecutar_desde_datos(datos) for datos in interpretados]
