# Predicción del Ganador de la Alcaldía de Bogotá 2023

![Badge de Python](https://img.shields.io/badge/Python-3.8-blue)
![Badge de Licencia](https://img.shields.io/badge/Licencia-MIT-green)

Este proyecto utiliza técnicas de web scraping en Twitter y análisis de datos para predecir el ganador de la alcaldía de Bogotá en 2023.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Pasos de Desarrollo](#pasos)
- [Uso](#uso)
- [Contribución](#contribución)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Descripción

El objetivo principal de este proyecto es analizar la opinión pública y las tendencias en Twitter relacionadas con los candidatos a la alcaldía de Bogotá en 2023. Mediante técnicas de web scraping y análisis de datos en Python, buscamos proporcionar una predicción informada sobre el posible ganador de las elecciones.

## Instalación

**Requisitos previos**:
- Python 3.8 o superior.
- Paquetes: [listar los paquetes principales que se necesitan, como tweepy, pandas, etc.]

```
# Clona el repositorio
git clone [URL del repositorio]

# Navega al directorio del proyecto
cd [nombre del directorio]

# Instala dependencias
pip install [dependencia requerida]
```

## Pasos

1. Recopilación de Datos
La recopilación de datos en este proyecto se realizó utilizando una herramienta de web scraping para extraer tweets de diferentes candidatos a la alcaldía de Bogotá en las elecciones de este año. Los candidatos seleccionados para obtener información de la aplicación Twitter fueron los siguientes: Carlos Fernando Galán, Gustavo Bolívar, Juan Daniel Oviedo y Diego Molano. Se recopiló un conjunto de tweets de estos candidatos para su posterior análisis.

Los datos fueron recopilados utilizando el repositorio twscrape (https://github.com/vladkens/twscrape), el cual está protegido por sus respectivos derechos de autor y políticas de uso. Agradecemos a los creadores del repositorio por proporcionar la fuente de datos para este proyecto.

2. Preprocesamiento
En la etapa de preprocesamiento, se llevó a cabo una limpieza exhaustiva de la información recopilada. Los tweets suelen contener etiquetas, datos irrelevantes y ruido que no son útiles para el siguiente paso, que es el análisis de sentimientos. El objetivo principal fue asegurarse de que los datos estuvieran en un formato adecuado y libres de elementos innecesarios.

3. Análisis de Sentimientos
El análisis de sentimientos desempeña un papel fundamental en este proyecto. Dado que el lenguaje español es muy amplio y depende en gran medida del contexto de las oraciones, las bibliotecas estándar disponibles en Internet para el análisis de sentimientos no eran las más convenientes. Por lo tanto, se crearon carpetas de palabras clave personalizadas que contienen términos positivos, negativos y neutrales. Este enfoque permitió entrenar un algoritmo específico para el contexto colombiano y el lenguaje español, incluyendo la jerga colombiana, lo que resultó en un análisis más competente y confiable.

4. Identificación de Temas de Interés
Después de realizar el análisis de sentimientos, se implementó un algoritmo capaz de reconocer los temas o "topics" relevantes dentro de los tweets depurados. Esto permitió identificar las principales áreas de interés en los mensajes de los candidatos. Los temas más recurrentes y relevantes se clasificaron y se utilizaron para categorizar todos los tweets de los candidatos, determinando en qué tema específico se encuentran.

5. Búsqueda de Pares Contradictorios
Esta etapa del proyecto tiene como objetivo encontrar pares de tweets contradictorios dentro de los datos procesados. Basándose en los pasos anteriores, se analizaron las opiniones y actitudes expresadas en los tweets para identificar aquellos que presentan contrastes significativos. Esta información puede ser valiosa para comprender mejor la dinámica de la opinión pública en relación con los candidatos y los temas clave.

6. Frontend
El frontend de este proyecto se centra en la creación de una interfaz de usuario que permitirá a los usuarios visualizar los tweets contradictorios identificados previamente, organizados por tema. Esta interfaz proporcionará una forma efectiva de explorar y comprender las opiniones contradictorias en el contexto político de las elecciones a la alcaldía de Bogotá. 

8. Reflexión
La utilidad de este sistema en un contexto político radica en su capacidad para proporcionar una visión clara y accesible de las opiniones contradictorias entre la ciudadanía con respecto a los candidatos y temas políticos relevantes en las elecciones a la alcaldía de Bogotá. Esto puede ser valioso para diversos actores, incluyendo a los votantes, los candidatos y los analistas políticos. 

## Uso

1. Configura tus credenciales de la API de Twitter en el directorio de infoGeneral
2. Sigue el paso a paso para hacer scraping de Twitter dependiendo de lo que quieras
3. Es importante seguir la secuencia de extracción -> depuración -> análisis, ejecutando cada script de la siguiente forma:
```
python main.py
```
4. En el caso de este proyecto, si quieres ver los resultados puedes ir a este [enlace](https://i0.wp.com/magis.iteso.mx/wp-content/uploads/2021/11/MAGIS-484-ERGOSUM-CARRUSEL.jpg?fit=1000%2C1002&ssl=1).

## Contribución

Si deseas contribuir al proyecto, por favor, sigue las siguientes pautas:
1. Haz un fork del repositorio.
2. Crea una nueva rama con un nombre descriptivo.
3. Realiza tus cambios y haz un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

## Desarrolladores

Si tienes preguntas o sugerencias, no dudes en contactarnos:

- Valentina Sierra Escobar
- Samir Alejandro Sánchez Romero
- Paula Andrea Peñuela Barrera
- William Daniel Martínez Oviedo
- Diego Alejandro Pardo Montero
