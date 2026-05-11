from .utilidades import es_nombre_valido

ACCIONES_SINONIMOS = {
    "crear":   {"crear", "crea", "haz", "construye", "fabrica"},
    "eliminar":{"eliminar", "borra", "quita", "remueve"},
    "listar":  {"listar", "muestra", "ver", "enseña"},
    "buscar":  {"buscar", "encuentra", "localiza"},
    "contar":  {"contar", "cuenta", "cantidad", "cuantos"},
    "vaciar":  {"vaciar", "limpiar", "reiniciar"},
    "mostrar": {"mostrar", "muestralo", "presenta", "presentalo"}
}

OBJETOS_SINONIMOS = {
    "modulo":   {"modulo", "módulo", "mod"},
    "elemento": {"elemento", "item"},
    "registro": {"registro", "dato"},
    "pantalla": {"pantalla", "pantallas", "salida"}
}

ACCIONES_VALIDAS = set(ACCIONES_SINONIMOS.keys())
OBJETOS_VALIDOS  = set(OBJETOS_SINONIMOS.keys())


def normalizar_accion(palabra):
    """
    Convierte una palabra a la acción canónica.
    Ejemplo: "haz" -> "crear"
    """
    for accion_canonica, sinonimos in ACCIONES_SINONIMOS.items():
        if palabra in sinonimos:
            return accion_canonica
    return None


def normalizar_objeto(palabra):
    """
    Convierte una palabra al objeto canónico.
    Ejemplo: "mod" -> "modulo"
    """
    for objeto_canonico, sinonimos in OBJETOS_SINONIMOS.items():
        if palabra in sinonimos:
            return objeto_canonico
    return None


def requiere_nombre(accion):
    """
    Indica si una acción necesita nombre.
    """
    return accion in {"crear", "eliminar", "buscar"}


def validar_estructura(datos):
    """
    Verifica que el diccionario tenga la estructura mínima.
    """
    if not isinstance(datos, dict):
        return False, "Formato de datos inválido"

    claves_necesarias = {"accion", "objeto", "nombre"}
    faltantes = claves_necesarias - set(datos.keys())

    if faltantes:
        return False, f"Faltan claves: {', '.join(sorted(faltantes))}"

    return True, ""


def validar_comando(datos):
    """
    Valida la gramática del comando:
    - estructura
    - acción válida
    - objeto válido
    - nombre según la acción
    - reglas especiales para mostrar
    """
    valido, mensaje = validar_estructura(datos)
    if not valido:
        return False, mensaje

    if "error" in datos:
        return False, datos["error"]

    accion  = datos.get("accion", "")
    objeto  = datos.get("objeto", "")
    nombre  = datos.get("nombre", "").strip()

    if accion not in ACCIONES_VALIDAS:
        return False, f"Acción no válida: {accion}"

    if objeto not in OBJETOS_VALIDOS:
        return False, f"Objeto no válido: {objeto}"

    if accion == "mostrar" and objeto != "pantalla":
        return False, "La acción 'mostrar' debe usarse con el objeto 'pantalla'"

    if requiere_nombre(accion) and not nombre:
        return False, f"La acción '{accion}' necesita un nombre"

    if accion in {"listar", "contar", "vaciar", "mostrar"} and nombre:
        return False, f"La acción '{accion}' no debe llevar nombre"

    if nombre and not es_nombre_valido(nombre):
        return False, "Nombre no válido"

    return True, "Comando válido"
