# Leer el archivo de resultados de clasificación
with open('resultados_clasificacion.txt', 'r', encoding='utf-8') as archivo_resultados:
    lineas = archivo_resultados.readlines()

# Crear un diccionario para almacenar tweets positivos y negativos por tema
temas_tweets = {}
temas_tweets_no_relacion = {}

tema_actual = None
tweet_actual = {"Nombre": None, "Contenido": None, "Sentimiento": None}
tweet_positivo = None
tweet_negativo = None

for linea in lineas:
    linea = linea.strip()
    if linea.startswith("Tema:"):
        if tweet_actual["Nombre"]:
            if tweet_actual["Sentimiento"] == "Sentimiento positivo":
                tweet_positivo = tweet_actual
            elif tweet_actual["Sentimiento"] == "Sentimiento negativo":
                tweet_negativo = tweet_actual
            tweet_actual = {"Nombre": None, "Contenido": None, "Sentimiento": None}

        tema_actual = linea.replace("Tema:", "").strip()
    elif linea.startswith("Nombre:"):
        tweet_actual["Nombre"] = linea.replace("Nombre:", "").strip()
    elif linea.startswith("Contenido:"):
        tweet_actual["Contenido"] = linea.replace("Contenido:", "").strip()
    elif linea.startswith("Sentimiento:"):
        tweet_actual["Sentimiento"] = linea.replace("Sentimiento:", "").strip()

    if tweet_positivo and tweet_negativo:
        temas_tweets[tema_actual] = {"Positivo": tweet_positivo, "Negativo": tweet_negativo}
        tweet_positivo = None
        tweet_negativo = None

# Imprimir o guardar los resultados en un archivo
with open('resultados_temas.txt', 'w', encoding='utf-8') as archivo_resultados_temas:
    for tema, tweets in temas_tweets.items():
        archivo_resultados_temas.write(f"Tema: {tema}\n")
        archivo_resultados_temas.write(f"Tweet Positivo:\n")
        if tweets["Positivo"]:
            archivo_resultados_temas.write(f"Nombre: {tweets['Positivo']['Nombre']}\n")
            archivo_resultados_temas.write(f"Contenido: {tweets['Positivo']['Contenido']}\n")
            archivo_resultados_temas.write(f"Sentimiento: {tweets['Positivo']['Sentimiento']}\n")
        else:
            archivo_resultados_temas.write("No existe tweet positivo relacionado.\n")

        archivo_resultados_temas.write(f"Tweet Negativo:\n")
        if tweets["Negativo"]:
            archivo_resultados_temas.write(f"Nombre: {tweets['Negativo']['Nombre']}\n")
            archivo_resultados_temas.write(f"Contenido: {tweets['Negativo']['Contenido']}\n")
            archivo_resultados_temas.write(f"Sentimiento: {tweets['Negativo']['Sentimiento']}\n")
        else:
            archivo_resultados_temas.write("No existe tweet negativo relacionado.\n")

        archivo_resultados_temas.write("\n")
