import re
import warnings
from unidecode import unidecode

# Deshabilitar las advertencias de unidecode
warnings.filterwarnings("ignore", category=RuntimeWarning, message="Surrogate character .* will be ignored.")

# Archivos de palabras clave
archivo_positivas = "positivas.txt"
archivo_negativas = "negativas.txt"

# Leer frases positivas y negativas desde los archivos
with open(archivo_positivas, 'r', encoding='utf-8') as archivo_positivas:
    frases_positivas = [line.strip() for line in archivo_positivas.readlines()]

with open(archivo_negativas, 'r', encoding='utf-8') as archivo_negativas:
    frases_negativas = [line.strip() for line in archivo_negativas.readlines()]

# Archivo de entrada y salida
archivo_entrada = "OviedoDepurado.txt"
archivo_salida = "resultadoOviedo.txt"

# Abre el archivo de entrada en modo lectura
with open(archivo_entrada, 'r', encoding='utf-8') as entrada:
    lineas = entrada.readlines()

# Abre el archivo de salida en modo escritura
with open(archivo_salida, 'w', encoding='utf-8') as salida:
    nombre = None  # Inicializa el nombre antes del bucle
    contenido_tweet = ""
    procesando_tweet = False  # Variable de estado para saber si estamos procesando un tweet

    positivos = 0
    negativos = 0
    neutrales = 0

    for linea in lineas:
        linea = linea.strip()
        if linea.startswith("Nombre:"):
            if procesando_tweet:
                # Procesar el tweet anterior
                contenido_decodificado = re.sub(r'\\u([0-9a-fA-F]{4})', lambda x: chr(int(x.group(1), 16)), contenido_tweet)
                contenido_decodificado = unidecode(contenido_decodificado)

                cantidad_frases_positivas = sum(1 for frase in frases_positivas if frase.lower() in contenido_decodificado.lower())
                cantidad_frases_negativas = sum(1 for frase in frases_negativas if frase.lower() in contenido_decodificado.lower())

                # Decidir el sentimiento basado en la cuenta de palabras
                if cantidad_frases_positivas > cantidad_frases_negativas:
                  sentimiento = "Sentimiento positivo"
                  positivos += 1
                elif cantidad_frases_negativas > cantidad_frases_positivas:
                  sentimiento = "Sentimiento negativo"
                  negativos += 1
                else:
                  sentimiento = "Sentimiento neutral"
                  neutrales += 1

                salida.write(f"Nombre: {nombre}\n")
                salida.write(f"Contenido: {contenido_decodificado}\n")
                salida.write(f"{sentimiento}\n\n")  # Agregar un salto de línea entre análisis

            # Almacenar el nombre para el próximo tweet
            nombre = linea.replace("Nombre:", "").strip()
            contenido_tweet = ""
            procesando_tweet = True
        elif procesando_tweet:
            contenido_tweet += linea + " "

    # Procesar el último tweet si lo hay
    if procesando_tweet:
        contenido_decodificado = re.sub(r'\\u([0-9a-fA-F]{4})', lambda x: chr(int(x.group(1), 16)), contenido_tweet)
        contenido_decodificado = unidecode(contenido_decodificado)

        # Contar cuántas palabras positivas y negativas hay en el tweet

    # Agregar conteo de sentimientos al final del archivo
    salida.write(f"Total de tweets con Sentimiento Positivo: {positivos}\n")
    salida.write(f"Total de tweets con Sentimiento Negativo: {negativos}\n")
    salida.write(f"Total de tweets con Sentimiento Neutral: {neutrales}\n")

print("Análisis de sentimientos completado. Los resultados se han guardado en", archivo_salida)
