"""
consola.py  –  Prueba interactiva de LibreriaLector
====================================================
Ejecuta:  python consola.py
"""
 
import sys
import re
#sys.path.append(r"D:\ProyectoMTP")  # ← cambia esto a tu ruta si es necesario
 
from LibreriaLector import ejecutar, ejecutar_texto_compuesto, limpiar_almacenamiento
 
SEP = "─" * 50
 
AYUDA = """
COMANDOS DISPONIBLES:
  crear   modulo/elemento/registro  <nombre>
  eliminar modulo/elemento/registro <nombre>
  listar  modulo/elemento/registro
  buscar  modulo/elemento/registro  <nombre>
  contar  modulo/elemento/registro
  vaciar  modulo/elemento/registro
  mostrar pantalla
 
SINÓNIMOS DE ACCIONES:
  crear    → haz, construye, fabrica, crea
  eliminar → borra, quita, remueve
  listar   → ver, enseña, muestra
  buscar   → encuentra, localiza
  contar   → cuenta, cantidad, cuantos
  vaciar   → limpiar, reiniciar
  mostrar  → muestralo, presenta, presentalo
 
COMANDOS COMPUESTOS (se ejecutan en secuencia):
  >> crea modulo autos y muestralo en pantalla tambien borra modulo autos
 
COMANDOS DE CONSOLA:
  ayuda   → muestra este mensaje
  limpiar → resetea todo el almacenamiento
  salir   → cierra la consola
"""
 
CONECTORES = ["tambien", "también", "ademas", "además", "luego", "despues", "después"]
PATRON_Y_ACCION = (
    r"\by\b\s*(?:crear|crea|haz|construye|fabrica|"
    r"eliminar|borra|quita|remueve|listar|muestra|ver|"
    r"enseña|buscar|encuentra|localiza|contar|cuenta|"
    r"vaciar|limpiar|reiniciar|mostrar|muestralo|presenta)"
)
 
 
def es_comando_compuesto(texto):
    texto_lower = texto.lower()
    if any(c in texto_lower for c in CONECTORES):
        return True
    if re.search(PATRON_Y_ACCION, texto_lower):
        return True
    return False
 
 
def main():
    limpiar_almacenamiento()
 
    print(SEP)
    print("  LibreriaLector — Consola interactiva")
    print(SEP)
    print("  Escribe 'ayuda' para ver los comandos disponibles.")
    print(SEP)
 
    while True:
        try:
            entrada = input("\n>> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nCerrando consola...")
            break
 
        if not entrada:
            continue
 
        if entrada.lower() == "salir":
            print("Cerrando consola...")
            break
 
        if entrada.lower() == "ayuda":
            print(AYUDA)
            continue
 
        if entrada.lower() == "limpiar":
            limpiar_almacenamiento()
            print("   Almacenamiento limpiado.")
            continue
 
        if es_comando_compuesto(entrada):
            resultados = ejecutar_texto_compuesto(entrada)
            for r in resultados:
                print(f"   {r}")
        else:
            print(f"   {ejecutar(entrada)}")
 
 
if __name__ == "__main__":
    main()
