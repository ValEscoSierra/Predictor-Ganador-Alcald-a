import re

# Nombre del archivo que utilizamos y la salida te amo delfin
#te amo más
archivo_entrada = "Oviedo.txt"
archivo_salida = "salida2.txt"

# Abre y modo lectura
with open(archivo_entrada, 'r') as entrada:
    contenido = entrada.read()

# Utiliza le agregue que DOTALL para que capturara toda la info y le agregue la etiqueta nombre para saber quien escribio
etiquetas = re.findall(r'"name": "(.*?)"', contenido, re.DOTALL)
etiquetas_full_text = re.findall(r'"full_text": "(.*?)"', contenido, re.DOTALL)

# Abre el archivo de salida en modo escritura
with open(archivo_salida, 'w') as salida:
    # Combina las coincidencias de "name" y "full_text" en el archivo de salida
    for name, full_text in zip(etiquetas, etiquetas_full_text):
        salida.write(f"Nombre: {name}\n")
        salida.write(f"Contenido: {full_text}\n\n")

print("Extracción completada. El texto se ha guardado en mi corazon ", archivo_salida)

