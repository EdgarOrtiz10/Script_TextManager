import aspose.words as aw

class Etiquetas:
  def __init__(self, data, palabra, frecuencia):
    self.data = data  
    self.palabra = palabra
    self.frecuencia = frecuencia
  
  
  def etiquetas(self):
    diccionario_frecuencia = {}
    for palabra in self.data:
      if palabra in diccionario_frecuencia:
        diccionario_frecuencia[palabra] += 1
      else:
        diccionario_frecuencia[palabra] = 1

    etiquetas_listadas = []
    for palabra in diccionario_frecuencia:
      frecuencia = diccionario_frecuencia[palabra]
      etiquetas_listadas.append(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia} \n")
  
    return etiquetas_listadas





 

