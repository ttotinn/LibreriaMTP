from LibreriaLector.utilidades import limpiar_texto, separar_palabras, PALABRAS_VACIAS
from LibreriaLector.reglas import normalizar_accion, normalizar_objeto


def interpretar(texto):
    """
    Interpreta un comando de texto y devuelve una estructura interna.
    Ejemplo:
        "crear un modulo de usuarios"
    devuelve:
        {
            "accion": "crear",
            "objeto": "modulo",
            "nombre": "usuarios"
        }
    """
    texto_limpio = limpiar_texto(texto)

    if not texto_limpio:
        return {"error": "Texto vacío"}

    palabras = separar_palabras(texto_limpio)

    accion = None
    objeto = None
    pos_accion = None
    pos_objeto = None

    for i, palabra in enumerate(palabras):
        if accion is None:
            posible_accion = normalizar_accion(palabra)
            if posible_accion:
                accion = posible_accion
                pos_accion = i
                continue

        if objeto is None:
            posible_objeto = normalizar_objeto(palabra)
            if posible_objeto:
                objeto = posible_objeto
                pos_objeto = i

    if accion is None:
        return {"error": "No se detectó una acción válida"}

    if objeto is None:
        return {"error": "No se detectó un objeto válido"}

    if pos_accion > pos_objeto:
        return {"error": "Orden incorrecto: la acción debe ir antes del objeto"}

    resto = palabras[pos_objeto + 1:]
    nombre_tokens = [p for p in resto if p not in PALABRAS_VACIAS]
    nombre = " ".join(nombre_tokens).strip()

    return {
        "accion": accion,
        "objeto": objeto,
        "nombre": nombre
    }