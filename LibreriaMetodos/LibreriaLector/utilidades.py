import re
import unicodedata

PALABRAS_VACIAS = {
    "un", "una", "unos", "unas",
    "el", "la", "los", "las",
    "de", "del", "al",
    "a", "en", "para", "con", "y",
    "llamado", "llamada"
}


def limpiar_texto(texto):
    """
    Convierte el texto a minúsculas, quita tildes y espacios sobrantes.
    """
    if texto is None:
        return ""

    texto = str(texto).strip().lower()

    texto = "".join(
        caracter for caracter in unicodedata.normalize("NFD", texto)
        if unicodedata.category(caracter) != "Mn"
    )

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


def es_nombre_valido(nombre):
    """
    Valida nombres simples compuestos por letras, números, guion bajo y espacios.
    """
    if not nombre or not nombre.strip():
        return False

    patron = r"[a-z0-9_]+(?: [a-z0-9_]+)*"
    return re.fullmatch(patron, nombre.strip()) is not None