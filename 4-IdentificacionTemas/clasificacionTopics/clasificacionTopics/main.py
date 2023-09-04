# Leer los temas desde un archivo de texto
with open('temas.txt', 'r', encoding='utf-8') as archivo_temas:
    temas = [line.strip() for line in archivo_temas.readlines()]

# Leer el archivo de salida con los tweets y sus sentimientos
with open('tweetsCompletos.txt', 'r', encoding='utf-8') as archivo_salida:
    lineas = archivo_salida.readlines()

# Crear un diccionario para asignar temas a los tweets
tweets_con_temas = {}

for i in range(0, len(lineas), 3):  # Iterar cada tres líneas (nombre, contenido, sentimiento)
    nombre = lineas[i].strip().replace("Nombre:", "")
    contenido = lineas[i + 1].strip().replace("Contenido:", "")
    sentimiento = lineas[i + 2].strip()

    # Buscar el tema en el contenido del tweet
    tema_asignado = "otro"
    for tema in temas:
        if tema.lower() in contenido.lower():
            tema_asignado = tema
            break

    # Almacenar el tweet con su tema
    if tema_asignado not in tweets_con_temas:
        tweets_con_temas[tema_asignado] = []
    tweets_con_temas[tema_asignado].append({"Nombre": nombre, "Contenido": contenido, "Sentimiento": sentimiento})

# Guardar los tweets clasificados por tema en un archivo
with open('resultados_clasificacion.txt', 'w', encoding='utf-8') as archivo_resultados:
    for tema, tweets in tweets_con_temas.items():
        for tweet in tweets:
            archivo_resultados.write(f"Tema: {tema}\n")
            archivo_resultados.write(f"Nombre: {tweet['Nombre']}\n")
            archivo_resultados.write(f"Contenido: {tweet['Contenido']}\n")
            archivo_resultados.write(f"Sentimiento: {tweet['Sentimiento']}\n")
            archivo_resultados.write("\n")  # Separar tweets con línea en blanco
