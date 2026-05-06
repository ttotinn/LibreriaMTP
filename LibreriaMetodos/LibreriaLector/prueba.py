from LibreriaLector.nucleo import ejecutar
from LibreriaLector.almacenamiento import limpiar_almacenamiento


def prueba_rapida():
    limpiar_almacenamiento()

    ejemplos = [
        "crear un modulo de usuarios",
        "crear modulo productos",
        "listar modulo",
        "buscar modulo usuarios",
        "eliminar modulo usuarios",
        "listar modulo"
    ]

    for comando in ejemplos:
        print(f">> {comando}")
        print(ejecutar(comando))
        print("-" * 40)


if __name__ == "__main__":
    prueba_rapida()

    print("Modo interactivo. Escribe 'salir' para terminar.")
    while True:
        texto = input(">> ")
        if texto.strip().lower() == "salir":
            break
        print(ejecutar(texto))