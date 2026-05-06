from LibreriaLector.analizador import interpretar
from LibreriaLector.reglas import validar_comando
from LibreriaLector.acciones import crear, eliminar, listar, buscar

ACCIONES = {
    "crear": crear,
    "eliminar": eliminar,
    "listar": listar,
    "buscar": buscar
}


def ejecutar(texto):
    """
    Función principal de la librería.
    Recibe texto, lo interpreta, lo valida y ejecuta la acción.
    """
    datos = interpretar(texto)

    valido, mensaje = validar_comando(datos)
    if not valido:
        return f"Error: {mensaje}"

    accion = datos["accion"]

    if accion not in ACCIONES:
        return "Error: acción no implementada"

    return ACCIONES[accion](datos)