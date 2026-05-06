ACCIONES_SINONIMOS = {
    "crear": {"crear", "crea", "haz", "fabrica", "construye"},
    "eliminar": {"eliminar", "borra", "quita", "remueve"},
    "listar": {"listar", "muestra", "ver", "enseña"},
    "buscar": {"buscar", "encuentra", "localiza"}
}

OBJETOS_SINONIMOS = {
    "modulo": {"modulo", "módulo", "mod"},
    "elemento": {"elemento", "item"},
    "registro": {"registro", "dato"}
}

ACCIONES_VALIDAS = set(ACCIONES_SINONIMOS.keys())
OBJETOS_VALIDOS = set(OBJETOS_SINONIMOS.keys())


def normalizar_accion(palabra):
    """
    Convierte una palabra en la acción canónica correspondiente.
    """
    for accion_canonica, sinonimos in ACCIONES_SINONIMOS.items():
        if palabra in sinonimos:
            return accion_canonica
    return None


def normalizar_objeto(palabra):
    """
    Convierte una palabra en el objeto canónico correspondiente.
    """
    for objeto_canonico, sinonimos in OBJETOS_SINONIMOS.items():
        if palabra in sinonimos:
            return objeto_canonico
    return None


def validar_estructura(datos):
    """
    Verifica que el diccionario tenga las claves necesarias.
    """
    if not isinstance(datos, dict):
        return False, "Formato de datos inválido"

    claves = {"accion", "objeto", "nombre"}
    faltantes = claves - set(datos.keys())

    if faltantes:
        return False, f"Faltan claves: {', '.join(sorted(faltantes))}"

    return True, ""


def validar_comando(datos):
    """
    Valida acción, objeto y nombre.
    """
    valido, mensaje = validar_estructura(datos)
    if not valido:
        return False, mensaje

    if "error" in datos:
        return False, datos["error"]

    accion = datos.get("accion", "")
    objeto = datos.get("objeto", "")
    nombre = datos.get("nombre", "").strip()

    if accion not in ACCIONES_VALIDAS:
        return False, f"Acción no válida: {accion}"

    if objeto not in OBJETOS_VALIDOS:
        return False, f"Objeto no válido: {objeto}"

    if accion in {"crear", "eliminar", "buscar"} and not nombre:
        return False, f"La acción '{accion}' necesita un nombre"

    if accion == "listar" and nombre:
        return False, "La acción 'listar' no debe llevar nombre"

    return True, ""