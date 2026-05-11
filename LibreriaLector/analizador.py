import re

from .utilidades import separar_palabras, eliminar_palabras_vacias
from .reglas import normalizar_accion, normalizar_objeto

PATRON_INICIO_ACCION = (
    r"(?:crear|crea|haz|construye|fabrica|"
    r"eliminar|borra|quita|remueve|"
    r"listar|muestra|ver|enseña|"
    r"buscar|encuentra|localiza|"
    r"contar|cuenta|cantidad|cuantos|"
    r"vaciar|limpiar|reiniciar|"
    r"mostrar|presenta|presentalo|muestralo)"
)


def separar_comandos(texto):
    """
    Separa una frase que contiene varios comandos.
    """
    texto_limpio = " ".join(str(texto).strip().split()).lower()

    if not texto_limpio:
        return []

    fragmentos = re.split(r"\b(?:ademas|tambien|luego|despues)\b", texto_limpio)

    comandos = []

    for fragmento in fragmentos:
        fragmento = fragmento.strip()
        if not fragmento:
            continue

        subfragmentos = re.split(
            rf"\by\b(?=\s*{PATRON_INICIO_ACCION}\b)",
            fragmento
        )

        for sub in subfragmentos:
            sub = sub.strip()
            if sub:
                comandos.append(sub)

    return comandos


def extraer_accion(tokens):
    """
    Busca la primera acción válida dentro de los tokens.
    """
    for token in tokens:
        accion = normalizar_accion(token)
        if accion:
            return accion
    return None


def extraer_objeto(tokens):
    """
    Busca el primer objeto válido dentro de los tokens.
    """
    for token in tokens:
        objeto = normalizar_objeto(token)
        if objeto:
            return objeto
    return None


def extraer_nombre(tokens, posicion_objeto):
    """
    Toma las palabras que aparecen después del objeto,
    quita palabras vacías y construye el nombre.
    """
    resto = tokens[posicion_objeto + 1:]
    resto_limpio = eliminar_palabras_vacias(resto)
    return " ".join(resto_limpio).strip()


def interpretar(texto):
    """
    Convierte un comando escrito en texto en una estructura interna.

    Ejemplo:
        "crear un modulo de usuarios"
    Devuelve:
        {"accion": "crear", "objeto": "modulo", "nombre": "usuarios"}
    """
    tokens = separar_palabras(texto)

    if not tokens:
        return {"error": "Texto vacío"}

    accion          = None
    objeto          = None
    posicion_accion = None
    posicion_objeto = None

    for i, token in enumerate(tokens):
        if accion is None:
            posible_accion = normalizar_accion(token)
            if posible_accion:
                accion = posible_accion
                posicion_accion = i

        if objeto is None:
            posible_objeto = normalizar_objeto(token)
            if posible_objeto:
                objeto = posible_objeto
                posicion_objeto = i

    if accion is None:
        return {"error": "No se detectó una acción válida"}

    if objeto is None:
        return {"error": "No se detectó un objeto válido"}

    if posicion_accion is not None and posicion_objeto is not None:
        if posicion_accion > posicion_objeto:
            return {"error": "Orden incorrecto: la acción debe ir antes del objeto"}

    nombre = ""
    if posicion_objeto is not None:
        nombre = extraer_nombre(tokens, posicion_objeto)

    return {"accion": accion, "objeto": objeto, "nombre": nombre}


def interpretar_comandos_compuestos(texto):
    """
    Interpreta varios comandos en una sola frase.
    Devuelve una lista de diccionarios.
    """
    comandos = separar_comandos(texto)
    return [interpretar(comando) for comando in comandos]
