import re
import unicodedata

# Palabras que no aportan significado gramatical importante.
# Se ignoran para permitir comandos más naturales.
PALABRAS_VACIAS = {
    "un", "una", "unos", "unas",
    "el", "la", "los", "las",
    "de", "del", "al",
    "a", "en", "para", "con", "y",
    "llamado", "llamada"
}


def quitar_tildes(texto):
    """
    Convierte letras acentuadas a su forma simple.

    Ejemplo:
        "módulo" -> "modulo"
    """
    if texto is None:
        return ""

    texto_normalizado = unicodedata.normalize("NFD", str(texto))

    return "".join(
        caracter for caracter in texto_normalizado
        if unicodedata.category(caracter) != "Mn"
    )


def limpiar_texto(texto):
    """
    Normaliza el texto completo:
    - quita espacios al inicio y final
    - pasa todo a minúsculas
    - quita tildes
    - reduce espacios repetidos
    """
    if texto is None:
        return ""

    texto = str(texto).strip().lower()
    texto = quitar_tildes(texto)
    texto = re.sub(r"\s+", " ", texto)

    return texto


def separar_palabras(texto):
    """
    Divide el texto en palabras.
    """
    texto = limpiar_texto(texto)

    if not texto:
        return []

    return texto.split()


def eliminar_palabras_vacias(lista_palabras, vacias=None):
    """
    Elimina palabras que no aportan significado gramatical.
    """
    if vacias is None:
        vacias = PALABRAS_VACIAS

    return [
        palabra for palabra in lista_palabras
        if palabra not in vacias
    ]


def es_nombre_valido(nombre):
    """
    Valida nombres simples.
    Se permiten letras, números, guiones bajos y espacios.
    """
    if not nombre or not nombre.strip():
        return False

    patron = r"[a-z0-9_]+(?: [a-z0-9_]+)*"
    return re.fullmatch(patron, nombre.strip()) is not None
