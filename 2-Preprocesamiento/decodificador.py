import re
from unidecode import unidecode

# Archivo de entrada y salida
archivo_entrada = "Molano.txt"
archivo_salida = "salida.txt"

# Leer el archivo de entrada
with open(archivo_entrada, 'r', encoding='utf-8') as entrada:
    texto = entrada.read()

# Reemplazar secuencias de escape Unicode
texto_decodificado = re.sub(r'\\u([0-9a-fA-F]{4})', lambda x: chr(int(x.group(1), 16)), texto)

# Reemplazar caracteres Unicode con su equivalente ASCII más cercano
texto_decodificado = unidecode(texto_decodificado)

# Reemplazar las secuencias "\n" con saltos de línea reales
texto_decodificado = texto_decodificado.replace("\\n", "\n")

# Escribir el resultado en el archivo de salida en UTF-8
with open(archivo_salida, 'w', encoding='utf-8', errors='replace') as salida:
    salida.write(texto_decodificado)

print("El resultado se ha guardado en mi corazón Delfin", archivo_salida)