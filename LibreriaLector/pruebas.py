"""
pruebas.py  –  Suite de pruebas unitarias para LibreriaLector
=============================================================
Cubre:
  • utilidades   (limpiar_texto, quitar_tildes, es_nombre_valido …)
  • almacenamiento (agregar, eliminar, existir, contar, vaciar …)
  • reglas        (normalizar, validar_estructura, validar_comando …)
  • analizador    (separar_comandos, interpretar …)
  • acciones      (crear, eliminar, listar, buscar, contar, vaciar, mostrar)
  • nucleo        (ejecutar, ejecutar_lote, ejecutar_texto_compuesto)

Cada prueba es una función independiente que devuelve (ok: bool, msg: str).
La función `ejecutar_pruebas()` las corre todas e imprime el resumen.
"""

import traceback

from LibreriaLector import (
    # utilidades
    quitar_tildes, limpiar_texto, separar_palabras,
    eliminar_palabras_vacias, es_nombre_valido,
    # almacenamiento
    agregar_elemento, eliminar_elemento, existe_elemento,
    contar_elementos, vaciar_objeto, limpiar_almacenamiento,
    # reglas
    normalizar_accion, normalizar_objeto,
    validar_estructura, validar_comando,
    # analizador
    separar_comandos, interpretar, interpretar_comandos_compuestos,
    # acciones
    crear, eliminar, listar, buscar, contar, vaciar, mostrar,
    # nucleo
    ejecutar, ejecutar_lote, ejecutar_texto_compuesto,
)


# ══════════════════════════════════════════════════════════════
# Helpers internos
# ══════════════════════════════════════════════════════════════

def _reset():
    """Limpia el almacenamiento antes de cada grupo de pruebas."""
    limpiar_almacenamiento()


def _ok(nombre):
    return True, nombre


def _falla(nombre, detalle):
    return False, f"{nombre}: {detalle}"


# ══════════════════════════════════════════════════════════════
# BLOQUE 1 – utilidades
# ══════════════════════════════════════════════════════════════

def prueba_quitar_tildes_basico():
    assert quitar_tildes("módulo") == "modulo"
    assert quitar_tildes("ÑOÑO")  == "NONO"
    return _ok("quitar_tildes básico")


def prueba_quitar_tildes_none():
    assert quitar_tildes(None) == ""
    return _ok("quitar_tildes None")


def prueba_limpiar_texto_espacios_y_mayusculas():
    resultado = limpiar_texto("  HolA   MUNDO  ")
    assert resultado == "hola mundo", repr(resultado)
    return _ok("limpiar_texto espacios y mayúsculas")


def prueba_limpiar_texto_tildes():
    resultado = limpiar_texto("Módulo")
    assert resultado == "modulo", repr(resultado)
    return _ok("limpiar_texto tildes")


def prueba_limpiar_texto_none():
    assert limpiar_texto(None) == ""
    return _ok("limpiar_texto None")


def prueba_separar_palabras_normal():
    assert separar_palabras("crear modulo alfa") == ["crear", "modulo", "alfa"]
    return _ok("separar_palabras normal")


def prueba_separar_palabras_vacio():
    assert separar_palabras("") == []
    assert separar_palabras(None) == []
    return _ok("separar_palabras vacío / None")


def prueba_eliminar_palabras_vacias():
    entrada = ["un", "modulo", "de", "usuarios"]
    salida  = eliminar_palabras_vacias(entrada)
    assert salida == ["modulo", "usuarios"], salida
    return _ok("eliminar_palabras_vacias")


def prueba_es_nombre_valido_ok():
    assert es_nombre_valido("usuarios")
    assert es_nombre_valido("alfa beta")
    assert es_nombre_valido("mod_v2")
    return _ok("es_nombre_valido OK")


def prueba_es_nombre_valido_invalido():
    assert not es_nombre_valido("")
    assert not es_nombre_valido("   ")
    assert not es_nombre_valido("abc!!")
    assert not es_nombre_valido("abc@dominio")
    return _ok("es_nombre_valido inválidos")


# ══════════════════════════════════════════════════════════════
# BLOQUE 2 – almacenamiento
# ══════════════════════════════════════════════════════════════

def prueba_agregar_elemento():
    _reset()
    assert agregar_elemento("modulo", "alfa") is True
    assert agregar_elemento("modulo", "alfa") is False   # duplicado
    return _ok("agregar_elemento")


def prueba_eliminar_elemento():
    _reset()
    agregar_elemento("modulo", "beta")
    assert eliminar_elemento("modulo", "beta")  is True
    assert eliminar_elemento("modulo", "beta")  is False  # ya no existe
    return _ok("eliminar_elemento")


def prueba_existe_elemento():
    _reset()
    agregar_elemento("modulo", "gamma")
    assert existe_elemento("modulo", "gamma") is True
    assert existe_elemento("modulo", "delta") is False
    return _ok("existe_elemento")


def prueba_contar_elementos():
    _reset()
    agregar_elemento("elemento", "x")
    agregar_elemento("elemento", "y")
    assert contar_elementos("elemento") == 2
    return _ok("contar_elementos")


def prueba_vaciar_objeto():
    _reset()
    agregar_elemento("registro", "a")
    vaciar_objeto("registro")
    assert contar_elementos("registro") == 0
    return _ok("vaciar_objeto")


def prueba_categoria_dinamica():
    """Las categorías no predefinidas se crean automáticamente."""
    _reset()
    assert agregar_elemento("nuevo_tipo", "item1") is True
    assert existe_elemento("nuevo_tipo", "item1") is True
    return _ok("categoría dinámica")


def prueba_limpiar_almacenamiento():
    agregar_elemento("modulo",   "x")
    agregar_elemento("elemento", "y")
    limpiar_almacenamiento()
    assert contar_elementos("modulo")   == 0
    assert contar_elementos("elemento") == 0
    return _ok("limpiar_almacenamiento")


# ══════════════════════════════════════════════════════════════
# BLOQUE 3 – reglas
# ══════════════════════════════════════════════════════════════

def prueba_normalizar_accion_sinonimos():
    assert normalizar_accion("haz")      == "crear"
    assert normalizar_accion("borra")    == "eliminar"
    assert normalizar_accion("ver")      == "listar"
    assert normalizar_accion("localiza") == "buscar"
    assert normalizar_accion("cuenta")   == "contar"
    assert normalizar_accion("limpiar")  == "vaciar"
    assert normalizar_accion("muestralo")== "mostrar"
    return _ok("normalizar_accion sinónimos")


def prueba_normalizar_accion_desconocida():
    assert normalizar_accion("banana") is None
    return _ok("normalizar_accion desconocida")


def prueba_normalizar_objeto_sinonimos():
    assert normalizar_objeto("mod")      == "modulo"
    assert normalizar_objeto("item")     == "elemento"
    assert normalizar_objeto("dato")     == "registro"
    assert normalizar_objeto("salida")   == "pantalla"
    return _ok("normalizar_objeto sinónimos")


def prueba_validar_estructura_correcta():
    datos = {"accion": "crear", "objeto": "modulo", "nombre": "alfa"}
    ok, _ = validar_estructura(datos)
    assert ok
    return _ok("validar_estructura correcta")


def prueba_validar_estructura_faltante():
    ok, msg = validar_estructura({"accion": "crear"})
    assert not ok
    assert "nombre" in msg or "objeto" in msg
    return _ok("validar_estructura con claves faltantes")


def prueba_validar_estructura_no_dict():
    ok, msg = validar_estructura("texto")
    assert not ok
    return _ok("validar_estructura no-dict")


def prueba_validar_comando_valido():
    datos = {"accion": "crear", "objeto": "modulo", "nombre": "alfa"}
    ok, msg = validar_comando(datos)
    assert ok, msg
    return _ok("validar_comando válido")


def prueba_validar_comando_sin_nombre():
    datos = {"accion": "crear", "objeto": "modulo", "nombre": ""}
    ok, msg = validar_comando(datos)
    assert not ok
    assert "nombre" in msg
    return _ok("validar_comando sin nombre requerido")


def prueba_validar_comando_nombre_en_listar():
    datos = {"accion": "listar", "objeto": "modulo", "nombre": "alfa"}
    ok, msg = validar_comando(datos)
    assert not ok
    return _ok("validar_comando nombre en listar (no permitido)")


def prueba_validar_comando_mostrar_objeto_incorrecto():
    datos = {"accion": "mostrar", "objeto": "modulo", "nombre": ""}
    ok, msg = validar_comando(datos)
    assert not ok
    assert "pantalla" in msg
    return _ok("validar_comando mostrar con objeto incorrecto")


def prueba_validar_comando_nombre_invalido():
    datos = {"accion": "crear", "objeto": "modulo", "nombre": "abc!!"}
    ok, msg = validar_comando(datos)
    assert not ok
    assert "válido" in msg.lower() or "valido" in msg.lower()
    return _ok("validar_comando nombre inválido")


def prueba_validar_comando_con_error_interno():
    datos = {"error": "algo salió mal", "accion": "crear",
             "objeto": "modulo", "nombre": "x"}
    ok, msg = validar_comando(datos)
    assert not ok
    return _ok("validar_comando con clave 'error' interna")


# ══════════════════════════════════════════════════════════════
# BLOQUE 4 – analizador
# ══════════════════════════════════════════════════════════════

def prueba_interpretar_simple():
    r = interpretar("crear modulo usuarios")
    assert r == {"accion": "crear", "objeto": "modulo", "nombre": "usuarios"}, r
    return _ok("interpretar simple")


def prueba_interpretar_con_palabras_vacias():
    r = interpretar("haz un modulo de ventas")
    assert r["accion"] == "crear"
    assert r["objeto"] == "modulo"
    assert r["nombre"] == "ventas"
    return _ok("interpretar con palabras vacías")


def prueba_interpretar_sinonimos():
    r = interpretar("borra elemento alfa")
    assert r["accion"] == "eliminar"
    assert r["objeto"] == "elemento"
    return _ok("interpretar sinónimos")


def prueba_interpretar_sin_nombre():
    r = interpretar("listar modulo")
    assert r["accion"] == "listar"
    assert r["nombre"] == ""
    return _ok("interpretar sin nombre")


def prueba_interpretar_texto_vacio():
    r = interpretar("")
    assert "error" in r
    return _ok("interpretar texto vacío")


def prueba_interpretar_sin_accion():
    r = interpretar("modulo usuarios")
    assert "error" in r
    return _ok("interpretar sin acción")


def prueba_interpretar_sin_objeto():
    r = interpretar("crear alfa")
    assert "error" in r
    return _ok("interpretar sin objeto")


def prueba_interpretar_orden_incorrecto():
    r = interpretar("modulo crear usuarios")
    assert "error" in r
    assert "orden" in r["error"].lower()
    return _ok("interpretar orden incorrecto")


def prueba_separar_comandos_con_tambien():
    resultado = separar_comandos("crear modulo alfa tambien listar modulo")
    assert len(resultado) == 2, resultado
    return _ok("separar_comandos con 'tambien'")


def prueba_separar_comandos_con_y_accion():
    resultado = separar_comandos("crea modulo alfa y eliminar modulo beta")
    assert len(resultado) == 2, resultado
    return _ok("separar_comandos con 'y' + acción")


def prueba_separar_comandos_vacio():
    assert separar_comandos("") == []
    assert separar_comandos("   ") == []
    return _ok("separar_comandos vacío")


def prueba_interpretar_compuesto():
    texto = "crear modulo alfa tambien listar modulo"
    resultado = interpretar_comandos_compuestos(texto)
    assert len(resultado) == 2
    assert resultado[0]["accion"] == "crear"
    assert resultado[1]["accion"] == "listar"
    return _ok("interpretar_comandos_compuestos")


# ══════════════════════════════════════════════════════════════
# BLOQUE 5 – acciones (unitarias, con mocks de almacenamiento)
# ══════════════════════════════════════════════════════════════

def prueba_accion_crear_nuevo():
    _reset()
    r = crear({"objeto": "modulo", "nombre": "alfa"})
    assert "creado" in r, r
    return _ok("accion crear nuevo")


def prueba_accion_crear_duplicado():
    _reset()
    crear({"objeto": "modulo", "nombre": "alfa"})
    r = crear({"objeto": "modulo", "nombre": "alfa"})
    assert "ya existe" in r, r
    return _ok("accion crear duplicado")


def prueba_accion_eliminar_existente():
    _reset()
    crear({"objeto": "modulo", "nombre": "beta"})
    r = eliminar({"objeto": "modulo", "nombre": "beta"})
    assert "eliminado" in r, r
    return _ok("accion eliminar existente")


def prueba_accion_eliminar_inexistente():
    _reset()
    r = eliminar({"objeto": "modulo", "nombre": "delta"})
    assert "no existe" in r, r
    return _ok("accion eliminar inexistente")


def prueba_accion_listar_vacio():
    _reset()
    r = listar({"objeto": "modulo"})
    assert "no hay" in r.lower(), r
    return _ok("accion listar vacío")


def prueba_accion_listar_con_elementos():
    _reset()
    crear({"objeto": "modulo", "nombre": "x"})
    crear({"objeto": "modulo", "nombre": "y"})
    r = listar({"objeto": "modulo"})
    assert "x" in r and "y" in r, r
    return _ok("accion listar con elementos")


def prueba_accion_buscar_encontrado():
    _reset()
    crear({"objeto": "modulo", "nombre": "gamma"})
    r = buscar({"objeto": "modulo", "nombre": "gamma"})
    assert "encontrado" in r, r
    return _ok("accion buscar encontrado")


def prueba_accion_buscar_no_encontrado():
    _reset()
    r = buscar({"objeto": "modulo", "nombre": "omega"})
    assert "no encontrado" in r, r
    return _ok("accion buscar no encontrado")


def prueba_accion_contar():
    _reset()
    crear({"objeto": "elemento", "nombre": "a"})
    crear({"objeto": "elemento", "nombre": "b"})
    r = contar({"objeto": "elemento"})
    assert "2" in r, r
    return _ok("accion contar")


def prueba_accion_vaciar():
    _reset()
    crear({"objeto": "registro", "nombre": "x"})
    r = vaciar({"objeto": "registro"})
    assert "vaciados" in r, r
    assert contar_elementos("registro") == 0
    return _ok("accion vaciar")


def prueba_accion_mostrar_pantalla_sin_nombre():
    r = mostrar({"objeto": "pantalla", "nombre": ""})
    assert r == "Mostrando en pantalla", r
    return _ok("accion mostrar pantalla sin nombre")


def prueba_accion_mostrar_pantalla_con_nombre():
    r = mostrar({"objeto": "pantalla", "nombre": "dashboard"})
    assert "dashboard" in r, r
    return _ok("accion mostrar pantalla con nombre")


def prueba_accion_mostrar_otro_objeto():
    r = mostrar({"objeto": "modulo", "nombre": ""})
    assert "modulo" in r, r
    return _ok("accion mostrar otro objeto")


# ══════════════════════════════════════════════════════════════
# BLOQUE 6 – nucleo / integración
# ══════════════════════════════════════════════════════════════

def prueba_ejecutar_crear():
    _reset()
    r = ejecutar("crear modulo reportes")
    assert "creado" in r, r
    return _ok("ejecutar crear")


def prueba_ejecutar_crear_duplicado():
    _reset()
    ejecutar("crear modulo reportes")
    r = ejecutar("crear modulo reportes")
    assert "ya existe" in r, r
    return _ok("ejecutar crear duplicado")


def prueba_ejecutar_eliminar():
    _reset()
    ejecutar("crear modulo reportes")
    r = ejecutar("eliminar modulo reportes")
    assert "eliminado" in r, r
    return _ok("ejecutar eliminar")


def prueba_ejecutar_listar():
    _reset()
    ejecutar("crear modulo alfa")
    r = ejecutar("listar modulo")
    assert "alfa" in r, r
    return _ok("ejecutar listar")


def prueba_ejecutar_buscar():
    _reset()
    ejecutar("crear modulo alfa")
    assert "encontrado" in ejecutar("buscar modulo alfa")
    assert "no encontrado" in ejecutar("buscar modulo zeta")
    return _ok("ejecutar buscar")


def prueba_ejecutar_contar():
    _reset()
    ejecutar("crear modulo cont_a")
    ejecutar("crear modulo cont_b")
    r = ejecutar("contar modulo")
    assert "2" in r, r
    return _ok("ejecutar contar")


def prueba_ejecutar_vaciar():
    _reset()
    ejecutar("crear modulo a")
    r = ejecutar("vaciar modulo")
    assert "vaciados" in r, r
    return _ok("ejecutar vaciar")


def prueba_ejecutar_mostrar():
    _reset()
    r = ejecutar("mostrar pantalla")
    assert "pantalla" in r.lower(), r
    return _ok("ejecutar mostrar")


def prueba_ejecutar_error_accion_invalida():
    _reset()
    r = ejecutar("banana modulo alfa")
    assert r.startswith("Error"), r
    return _ok("ejecutar error acción inválida")


def prueba_ejecutar_error_objeto_invalido():
    _reset()
    r = ejecutar("crear pizza alfa")
    assert r.startswith("Error"), r
    return _ok("ejecutar error objeto inválido")


def prueba_ejecutar_error_orden_incorrecto():
    _reset()
    r = ejecutar("modulo crear alfa")
    assert r.startswith("Error"), r
    return _ok("ejecutar error orden incorrecto")


def prueba_ejecutar_error_sin_nombre():
    _reset()
    r = ejecutar("crear modulo")
    assert r.startswith("Error"), r
    return _ok("ejecutar error sin nombre")


def prueba_ejecutar_error_nombre_invalido():
    _reset()
    r = ejecutar("crear modulo abc!!")
    assert r.startswith("Error"), r
    return _ok("ejecutar error nombre inválido")


def prueba_ejecutar_texto_vacio():
    r = ejecutar("")
    assert r.startswith("Error"), r
    return _ok("ejecutar texto vacío")


def prueba_ejecutar_lote():
    _reset()
    resultados = ejecutar_lote([
        "crear modulo alfa",
        "crear modulo beta",
        "listar modulo",
    ])
    assert len(resultados) == 3
    assert "creado"  in resultados[0]
    assert "creado"  in resultados[1]
    assert "alfa"    in resultados[2]
    assert "beta"    in resultados[2]
    return _ok("ejecutar_lote")


def prueba_ejecutar_texto_compuesto():
    _reset()
    texto = "crear modulo alfa tambien listar modulo"
    resultados = ejecutar_texto_compuesto(texto)
    assert len(resultados) == 2
    assert "creado"  in resultados[0]
    assert "alfa"    in resultados[1]
    return _ok("ejecutar_texto_compuesto")


def prueba_flujo_completo_ciclo_vida():
    """Crea, lista, busca, cuenta, elimina y verifica."""
    _reset()
    assert "creado"      in ejecutar("crear elemento pieza_a")
    assert "creado"      in ejecutar("crear elemento pieza_b")
    assert "pieza_a"     in ejecutar("listar elemento")
    assert "encontrado"  in ejecutar("buscar elemento pieza_a")
    assert "2"           in ejecutar("contar elemento")
    assert "eliminado"   in ejecutar("eliminar elemento pieza_a")
    assert "1"           in ejecutar("contar elemento")
    assert "no encontrado" in ejecutar("buscar elemento pieza_a")
    assert "vaciados"    in ejecutar("vaciar elemento")
    assert "0"           in ejecutar("contar elemento")
    return _ok("flujo completo ciclo de vida")


# ══════════════════════════════════════════════════════════════
# RUNNER
# ══════════════════════════════════════════════════════════════

TODAS_LAS_PRUEBAS = [
    # utilidades
    prueba_quitar_tildes_basico,
    prueba_quitar_tildes_none,
    prueba_limpiar_texto_espacios_y_mayusculas,
    prueba_limpiar_texto_tildes,
    prueba_limpiar_texto_none,
    prueba_separar_palabras_normal,
    prueba_separar_palabras_vacio,
    prueba_eliminar_palabras_vacias,
    prueba_es_nombre_valido_ok,
    prueba_es_nombre_valido_invalido,
    # almacenamiento
    prueba_agregar_elemento,
    prueba_eliminar_elemento,
    prueba_existe_elemento,
    prueba_contar_elementos,
    prueba_vaciar_objeto,
    prueba_categoria_dinamica,
    prueba_limpiar_almacenamiento,
    # reglas
    prueba_normalizar_accion_sinonimos,
    prueba_normalizar_accion_desconocida,
    prueba_normalizar_objeto_sinonimos,
    prueba_validar_estructura_correcta,
    prueba_validar_estructura_faltante,
    prueba_validar_estructura_no_dict,
    prueba_validar_comando_valido,
    prueba_validar_comando_sin_nombre,
    prueba_validar_comando_nombre_en_listar,
    prueba_validar_comando_mostrar_objeto_incorrecto,
    prueba_validar_comando_nombre_invalido,
    prueba_validar_comando_con_error_interno,
    # analizador
    prueba_interpretar_simple,
    prueba_interpretar_con_palabras_vacias,
    prueba_interpretar_sinonimos,
    prueba_interpretar_sin_nombre,
    prueba_interpretar_texto_vacio,
    prueba_interpretar_sin_accion,
    prueba_interpretar_sin_objeto,
    prueba_interpretar_orden_incorrecto,
    prueba_separar_comandos_con_tambien,
    prueba_separar_comandos_con_y_accion,
    prueba_separar_comandos_vacio,
    prueba_interpretar_compuesto,
    # acciones
    prueba_accion_crear_nuevo,
    prueba_accion_crear_duplicado,
    prueba_accion_eliminar_existente,
    prueba_accion_eliminar_inexistente,
    prueba_accion_listar_vacio,
    prueba_accion_listar_con_elementos,
    prueba_accion_buscar_encontrado,
    prueba_accion_buscar_no_encontrado,
    prueba_accion_contar,
    prueba_accion_vaciar,
    prueba_accion_mostrar_pantalla_sin_nombre,
    prueba_accion_mostrar_pantalla_con_nombre,
    prueba_accion_mostrar_otro_objeto,
    # nucleo / integración
    prueba_ejecutar_crear,
    prueba_ejecutar_crear_duplicado,
    prueba_ejecutar_eliminar,
    prueba_ejecutar_listar,
    prueba_ejecutar_buscar,
    prueba_ejecutar_contar,
    prueba_ejecutar_vaciar,
    prueba_ejecutar_mostrar,
    prueba_ejecutar_error_accion_invalida,
    prueba_ejecutar_error_objeto_invalido,
    prueba_ejecutar_error_orden_incorrecto,
    prueba_ejecutar_error_sin_nombre,
    prueba_ejecutar_error_nombre_invalido,
    prueba_ejecutar_texto_vacio,
    prueba_ejecutar_lote,
    prueba_ejecutar_texto_compuesto,
    prueba_flujo_completo_ciclo_vida,
]


def ejecutar_pruebas():
    """
    Ejecuta todas las pruebas e imprime un resumen detallado.
    Devuelve True si todas pasaron, False en caso contrario.
    """
    SEP = "─" * 56
    print(SEP)
    print(f"  Ejecutando {len(TODAS_LAS_PRUEBAS)} pruebas…")
    print(SEP)

    pasadas  = []
    fallidas = []

    for prueba in TODAS_LAS_PRUEBAS:
        try:
            ok, nombre = prueba()
            if ok:
                pasadas.append(nombre)
                print(f"  ✓  {nombre}")
            else:
                fallidas.append(nombre)
                print(f"  ✗  {nombre}")
        except Exception as exc:
            nombre = prueba.__name__
            fallidas.append(nombre)
            print(f"  ✗  {nombre}")
            print(f"       {exc}")
            traceback.print_exc()

    print(SEP)
    print(f"  Resultado: {len(pasadas)} pasadas / {len(fallidas)} fallidas "
          f"de {len(TODAS_LAS_PRUEBAS)} totales")

    if fallidas:
        print("\n  Fallidas:")
        for nombre in fallidas:
            print(f"    • {nombre}")

    print(SEP)
    return len(fallidas) == 0


# Permite ejecutar directamente: python -m LibreriaLector.pruebas
if __name__ == "__main__":
    import sys
    ok = ejecutar_pruebas()
    sys.exit(0 if ok else 1)
