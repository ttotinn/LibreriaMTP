from .utilidades import (
    quitar_tildes,
    limpiar_texto,
    separar_palabras,
    eliminar_palabras_vacias,
    es_nombre_valido,
    PALABRAS_VACIAS,
)

from .reglas import (
    normalizar_accion,
    normalizar_objeto,
    requiere_nombre,
    validar_estructura,
    validar_comando,
)

from .analizador import (
    separar_comandos,
    extraer_accion,
    extraer_objeto,
    extraer_nombre,
    interpretar,
    interpretar_comandos_compuestos,
)

from .almacenamiento import (
    obtener_base_datos,
    obtener_lista,
    agregar_elemento,
    eliminar_elemento,
    existe_elemento,
    contar_elementos,
    vaciar_objeto,
    limpiar_almacenamiento,
)

from .acciones import (
    crear,
    eliminar,
    listar,
    buscar,
    contar,
    vaciar,
    mostrar,
)

from .nucleo import (
    interpretar_comando,
    validar_comando_texto,
    ejecutar_desde_datos,
    ejecutar,
    ejecutar_lote,
    ejecutar_texto_compuesto,
)
