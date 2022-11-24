import aspose.words as aw
from Etiquetas import Etiquetas
import re
import nltk
import string

global docText, frecuencia_palabras
docText = []
url = input("Introduzca nombre del archivo\n") + (".docx")
docToRead = aw.Document(url)

#Pasamos el archivo a una lista
for paragraph in docToRead.get_child_nodes(aw.NodeType.PARAGRAPH, True):   
    paragraph = paragraph.as_paragraph()
    docText.append(paragraph.to_string(aw.SaveFormat.TEXT))
docText = '\t'.join(docText)

quitar = ",;:.\n!\"'"
for caracter in quitar:
    docText= docText.replace(caracter,
                           "")
    
docText = docText.lower() #Convertimos a minuscula
palabras = docText.split(" ") #convetimos la cadena a un arreglo

print(Etiquetas.etiquetas(palabras))