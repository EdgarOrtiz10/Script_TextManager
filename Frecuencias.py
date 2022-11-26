import re
import nltk
import string

class Frecuencias: 
    def frecuencias(dataIn):
        global stopwords, data, frecuencia_palabras, mayor_frecuencia
        data = dataIn 
        nltk.download('punkt')
        nltk.download('stopwords')
        stopwords = nltk.corpus.stopwords.words('spanish') 
        string.punctuation #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        
        def preproceso(text):
            formatear_texto = text.lower()
            tokens = []
            for token in nltk.word_tokenize(formatear_texto):
                tokens.append(token)
            #print(tokens)
            #tokens = [word for word in tokens if word not in stopwords]
            tokens = [word for word in tokens if word not in stopwords and word not in string.punctuation ]
            formatear_texto = ' '.join(element for element in tokens)
            return formatear_texto
        
        formatear_texto = preproceso(data)
                
        #Frecuencia de palabras
        frecuencia_palabras = nltk.FreqDist(nltk.word_tokenize(formatear_texto))
        mayor_frecuencia = max(frecuencia_palabras.values())
        for word in frecuencia_palabras.keys():
            frecuencia_palabras[word] = (frecuencia_palabras[word] / mayor_frecuencia)