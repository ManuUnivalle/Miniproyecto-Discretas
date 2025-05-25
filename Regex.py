import re

def endsWith(txt):
    #Patrón para palabras terminadas en d, s, o t
    pattern = r'\b\w*[dst]\b'
    x = re.findall(pattern, txt)
    return x

def capitalizeAndVowel(txt):
    #Patrón para palabras que empiezan por mayúsculas y contienen la letra a
    pattern = r'\b[A-Z]\w*a\w*\b'
    x = re.findall(pattern, txt)
    return x

def vowels_accents(txt):
    #Patrón para palabras que contengan todas las vocales incluidas tildes
    pattern = r'\b(?=\w*[aá])(?=\w*[eé])(?=\w*[ií])(?=\w*[oó])(?=\w*[uú])\w+\b'
    x = re.findall(pattern, txt)
    return x

def questions_exclamations(txt):
    #Patrón frases que sean preguntas o exclamaciones
    pattern = r'\¿.+\?|\¡.+\!'
    x = re.findall(pattern, txt)
    return x

def atSign(txt):
    #Patrón para palabras que contengan @
    pattern = r'\w*@\w*'
    x = re.findall(pattern, txt)
    return x

def commonAbreviations(txt):
    #Patrón para encontrar abreviaciones comunes
    pattern = r'(?:[A-Za-z]+\.){1,}'
    x = re.findall(pattern, txt)
    return x

if __name__ == '__main__':
    txt = """La Ciberseguridad es un área en constante crecimiento que nos permite mantenernos informados 
    y preparados frente a las diversas amenazas y novedades relacionadas a la seguridad de nuestros datos 
    (en español), por ente, se comparte un artículo de investigación, el cual, lo debe guardar como ¿cuál? 
    o ¡encantadaaaa!  un archivo en formato de texto (.txt) Manuela, Silla, Pepe, euforia, eufonía, murciélago,
    micorreo@correounivalle, @algo Algoa@ @ amistadoso p.ej. T., q.e.p.d. m.c. Vda."""
    #prueba
    salida = "Coincidencias: "
    for i in range(0, len(vowels_accents(txt))):
        salida += (vowels_accents(txt))[i] + ", "
    print(salida)

    