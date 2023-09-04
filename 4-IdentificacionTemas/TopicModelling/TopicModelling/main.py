import gensim
import gensim.corpora as corpora
from gensim.models import LdaModel
from gensim.utils import simple_preprocess
from nltk.corpus import stopwords
import re
import spacy  # Importa SpaCy

# Descarga las stopwords de NLTK si aún no las tienes
import nltk

nltk.download('stopwords')

# Carga tu modelo de SpaCy en español
nlp = spacy.load('es_core_news_sm')

# Carga tus datos desde el archivo de texto
with open('Galan.txt', 'r', encoding='utf-8') as file:
    tweets = file.readlines()

palabras_a_banear = ["mas", "co", "gustavobolivar", "GALAN", "Gus", "#", "jajaja"]

# Preprocesa los datos
stop_words = stopwords.words('spanish')


def preprocess_tweet(tweet):
    tweet = tweet.strip()
    tweet = re.sub(r'@\w+', '', tweet)

    # Usa SpaCy para identificar sustantivos y excluye las palabras a banear
    words = [word.text for word in nlp(tweet) if
             word.pos_ == 'NOUN' and word.text not in stop_words and word.text not in palabras_a_banear]

    return words


tweets = [preprocess_tweet(tweet) for tweet in tweets]

# Crea el diccionario y el corpus
id2word = corpora.Dictionary(tweets)
corpus = [id2word.doc2bow(tweet) for tweet in tweets]

# Entrena el modelo LDA
lda_model = LdaModel(corpus=corpus, id2word=id2word, num_topics=15, random_state=100, update_every=1, chunksize=100,
                     passes=10, alpha='auto', per_word_topics=True)

# Obtiene las palabras clave más probables por tema
topics = lda_model.show_topics(num_topics=15, num_words=5, log=False, formatted=False)
for topic in topics:
    print(f'Tema {topic[0]}: {", ".join([word[0] for word in topic[1]])}')
