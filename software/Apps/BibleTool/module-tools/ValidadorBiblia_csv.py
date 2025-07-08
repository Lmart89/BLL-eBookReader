import csv
import re

def validar_csv(archivo_csv):
    linea_num = 1
    errores = 0

    with open(archivo_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for fila in reader:
            if len(fila) != 6:
                print(f"❌ [Línea {linea_num}] Número incorrecto de columnas ({len(fila)}): {fila}")
                errores += 1
            else:
                texto = fila[3].strip()
                if re.search(r'\(.*?(cf\.|ver|véase|vea|ver también).*?\)', texto, flags=re.IGNORECASE):
                    print(f"⚠️ [Línea {linea_num}] Posible referencia cruzada: {texto}")
                    errores += 1
            linea_num += 1

    if errores == 0:
        print("✅ CSV verificado: no se encontraron errores.")
    else:
        print(f"\n🔍 Total de posibles errores encontrados: {errores}")

if __name__ == "__main__":
    validar_csv("rv60.csv")
