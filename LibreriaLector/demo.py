"""
demo.py  –  Demostración completa de LibreriaLector
====================================================
Muestra cada capa de la librería de forma ordenada y
ejecuta el conjunto de pruebas unitarias al final.
"""

from LibreriaLector import (
    limpiar_texto,
    separar_comandos,
    interpretar,
    interpretar_comandos_compuestos,
    validar_comando,
    ejecutar,
    ejecutar_lote,
    ejecutar_texto_compuesto,
    limpiar_almacenamiento,
)
from LibreriaLector.pruebas import ejecutar_pruebas   # ← suite de tests integrada


SEP  = "=" * 56
SEP2 = "-" * 56


def titulo(n, texto):
    print(f"\n{SEP}")
    print(f"  {n}) {texto}")
    print(SEP)


def entrada(texto):
    print(f"  Entrada : {texto!r}")


def salida(resultado):
    if isinstance(resultado, list):
        print("  Salida  :")
        for item in resultado:
            print(f"            {item!r}")
    else:
        print(f"  Salida  : {resultado!r}")


# ------------------------------------------------------------------
# Limpiamos el almacenamiento antes de empezar
# ------------------------------------------------------------------
limpiar_almacenamiento()


# ------------------------------------------------------------------
# 1) LIMPIEZA DE TEXTO
# ------------------------------------------------------------------
titulo(1, "LIMPIEZA DE TEXTO")
t1 = "   Módulo     Usuarios   "
entrada(t1)
salida(limpiar_texto(t1))


# ------------------------------------------------------------------
# 2) SEPARACIÓN DE COMANDOS COMPUESTOS
# ------------------------------------------------------------------
titulo(2, "SEPARACIÓN DE COMANDOS")
t2 = "crea un modulo de usuarios y muestralo en pantalla tambien borra modulo de autos"
entrada(t2)
salida(separar_comandos(t2))


# ------------------------------------------------------------------
# 3) INTERPRETACIÓN DE UN COMANDO
# ------------------------------------------------------------------
titulo(3, "INTERPRETACIÓN GRAMATICAL")
t3 = "haz un modulo de ventas"
entrada(t3)
salida(interpretar(t3))


# ------------------------------------------------------------------
# 4) VALIDACIÓN GRAMATICAL
# ------------------------------------------------------------------
titulo(4, "VALIDACIÓN GRAMATICAL")
datos_ok   = interpretar(t3)
datos_malo = {"accion": "crear", "objeto": "modulo", "nombre": ""}

print(f"  Dict válido  → {validar_comando(datos_ok)}")
print(f"  Dict inválido→ {validar_comando(datos_malo)}")


# ------------------------------------------------------------------
# 5) EJECUCIÓN SIMPLE
# ------------------------------------------------------------------
titulo(5, "EJECUCIÓN SIMPLE")
casos_simples = [
    "crear modulo reportes",
    "crear modulo reportes",      # duplicado
    "listar modulo",
    "buscar modulo reportes",
    "contar modulo",
    "eliminar modulo reportes",
    "listar modulo",
    "mostrar pantalla",
]
for cmd in casos_simples:
    print(f"  {cmd!r:<40} → {ejecutar(cmd)!r}")


# ------------------------------------------------------------------
# 6) SINÓNIMOS DE ACCIONES Y OBJETOS
# ------------------------------------------------------------------
titulo(6, "SINÓNIMOS")
sinonimos = [
    "haz elemento alfa",
    "construye registro beta",
    "borra elemento alfa",
    "encuentra registro beta",
    "cuenta elemento",
    "limpiar registro",
    "muestralo pantalla",
]
for cmd in sinonimos:
    print(f"  {cmd!r:<40} → {ejecutar(cmd)!r}")


# ------------------------------------------------------------------
# 7) EJECUCIÓN EN LOTE
# ------------------------------------------------------------------
titulo(7, "EJECUCIÓN EN LOTE (ejecutar_lote)")
limpiar_almacenamiento()
lote = [
    "crear modulo alfa",
    "crear modulo beta",
    "crear modulo gamma",
    "listar modulo",
    "contar modulo",
    "vaciar modulo",
    "listar modulo",
]
salida(ejecutar_lote(lote))


# ------------------------------------------------------------------
# 8) COMANDOS COMPUESTOS (interpretar + ejecutar)
# ------------------------------------------------------------------
titulo(8, "COMANDOS COMPUESTOS")
limpiar_almacenamiento()
t8 = "crea un modulo de usuarios y muestralo en pantalla tambien borra modulo de autos"
entrada(t8)
print("\n  Interpretados:")
for d in interpretar_comandos_compuestos(t8):
    print(f"    {d}")
print("\n  Ejecutados:")
salida(ejecutar_texto_compuesto(t8))


# ------------------------------------------------------------------
# 9) MANEJO DE ERRORES
# ------------------------------------------------------------------
titulo(9, "MANEJO DE ERRORES")
errores = [
    ("acción inexistente",    "banana modulo usuarios"),
    ("objeto desconocido",    "crear pizza usuarios"),
    ("orden incorrecto",      "modulo crear usuarios"),
    ("sin nombre requerido",  "crear modulo"),
    ("nombre con caracteres inválidos", "crear modulo abc!@#"),
    ("texto vacío",           ""),
    ("solo espacios",         "    "),
]
for descripcion, cmd in errores:
    print(f"  [{descripcion}]")
    print(f"    {cmd!r} → {ejecutar(cmd)!r}")


# ------------------------------------------------------------------
# 10) SUITE DE PRUEBAS UNITARIAS
# ------------------------------------------------------------------
titulo(10, "PRUEBAS UNITARIAS AUTOMATIZADAS")
ejecutar_pruebas()
