import re

#Patrón para palabras terminadas en d, s, o t. La función retorna la lista con las coincidencias
def endsWith(txt):
    #El patrón delimita final de una palabra, coincide con cualquier caracter alfabético que se repite 
    #0 o más veces, seguida de d, s, t al final de la palabra
    pattern = r'[A-ZÁ-Úá-úa-zñÑ]+[dst]\b'
    coincidences = re.findall(pattern, txt)
    return coincidences

#Patrón para palabras que empiezan por mayúsculas y contienen la letra a. La función retorna la lista con las coincidencias
def capitalizeAndVowel(txt):
    #El patrón comienza con una letra mayúscula, seguida de cualquier caracter alfabético que se repite 0 o más veces, 
    #la letra a y cualquier caracter alfabético que se repite 0 o más veces
    pattern = r'[A-ZÁ-ÚÑ][á-úa-zñ]*a[á-úa-z]*'
    coincidences = re.findall(pattern, txt)
    return coincidences

#Patrón para palabras que contengan todas las vocales incluidas tildes. La función retorna la lista con las coincidencias
def vowels_accents(txt):
    #El patrón delimita el inicio y final de una palabra, agrupa cualquier caracter alfanumérico que 
    # se repite 0 o más veces y comprueba que tenga todas las vocales incluidas tildes
    pattern = r'\b(?=\w*[aá])(?=\w*[eé])(?=\w*[ií])(?=\w*[oó])(?=\w*[uú])\w+\b'
    coincidences = re.findall(pattern, txt)
    return coincidences

#Patrón frases que sean preguntas o exclamaciones. La función retorna la lista con las coincidencias
def questions_exclamations(txt):
    #El patrón asegura que haya un signo de pregunta o de exclamación al inicio y al final de la expresión 
    #que puede tener cualquier caracter alfanumérico, espacios y signos de puntuación 1 o más veces
    pattern = r'\¿[\wá-úñÑÁ-Ú\s\,\.\;\(\)\:]+\?|\¡[\wá-úñÑÁ-Ú\s\,\.\;\(\)\:]+\!'
    coincidences = re.findall(pattern, txt, flags = re.I)
    return coincidences

#Patrón para palabras que contengan @. La función retorna la lista con las coincidencias
def atSign(txt):
    #El patrón mira cualquier letra y @ que se repita 0 o más veces, seguido de un @, 
    #seguido de cualquier letra y @ que se repita 0 o más veces
    pattern = r'[A-ZÁ-Úa-zá-úñÑ@]*@[A-ZÁ-Úa-zá-ú@]*'
    coincidences = re.findall(pattern, txt)
    return coincidences

#Patrón para encontrar abreviaciones comunes. La función retorna la lista con las coincidencias. 
def commonAbreviations(txt):
    #El patrón agrupa letras que se repiten 1 o más veces seguidas de un punto. 
    #Luego mira si esa agrupación se repite por lo menos 1 o más veces
    pattern = r'(?:[A-ZÁ-Úa-zá-úñÑ]+\.){1,}'
    coincidences = re.findall(pattern, txt)
    return coincidences

#Patrón para expresiones que podrían indicar plagio. La función busca en el texto frases que coincidan con las de la lista predeterminada.
#Retorna la lista con las coincidencias
def plagiarismPhrases(txt):
    det_phrases =["según el autor", "de acuerdo con algunos estudios" ,"como se ha mencionado anteriormente", "se sabe que", 
              "varios autores coinciden en", "se dice que", "algunos investigadores afirman", "como se demuestra", 
              "estudios recientes muestran que"]
    #El patrón delimita inicio y fin de una frase, forma una cadena a partir de las cadenas de la lista y agrupa la expresión
    #Mira si coincide con alguna de las frases predeterminadas
    pattern = r'\b(?:' + '|'.join(det_phrases) + r')\b'
    coincidences = re.findall(pattern, txt, flags = re.I)
    return coincidences

#Patrón para encontrar frases repetidas N veces. La función retorna la lista con las coincidencias.
def repeatedPhrases(txt, piece):
    #El patrón delimita inicio y fin de una frase y verifica que la frase dada en consola esté en el texto
    pattern = r'\b' + piece + r'\b'
    coincidences = re.findall(pattern, txt)
    return coincidences

if __name__ == '__main__':
    txt = """La Ciberseguridad es un área. en constante crecimiento que nos permite mantenernos informados 
    y preparados frente a las diversas amenazas y novedades relacionadas a la seguridad de nuestros datos 
    (en español), por ente, se comparte un artículo de investigación, el cual, lo debe guardar como ¿cuál?, 
    añadís o ¡encantadaaaa!  un archivo en formato de texto (.txt) Manuela, Silla, Sillá, Ñandú Pepe, euforia, 
    eufonía, murciélago, micorreo@correounivalle, @al@go Algoa@ @ amistadoso p.ej. T., q.e.p.d. m.c. Vda. área. 
    de acuerdo con algunos estudios, área. según el autor: La Ciberseguridad es un área en constante crecimiento."""
    pieza = input("Ingresa la frase que quieres ver si se repite: ")

    #prueba
    salida = "Coincidencias: "
    for i in range(0, len(repeatedPhrases(txt, pieza))):
        salida += (repeatedPhrases(txt, pieza)[i]) +", "
    print(salida)
    print(f"Se repite {len(repeatedPhrases(txt,pieza))} veces")