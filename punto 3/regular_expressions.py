# Integrante1: Manuela Delgado Aguirre - 2459640
# Integrante2: Paula Jimena Bohórquez Bermúdez - 2459409
# Docente: Luis Germán Toro Pareja
# Grupo: 50
# Laboratorio 5

import re

#Patrón para encontrar abreviaciones comunes. La función retorna la lista con las coincidencias.
def abreviations(txt):
    #El patrón agrupa letras que se repiten 1 o más veces seguidas de un punto o apostrofo. 
    pattern = r'(?:[a-zá-úñ]+\.){2,}|(?:[a-z]+\'){1,}[a-z]+\b'
    coincidences = re.findall(pattern, txt, re.IGNORECASE)
    return coincidences

#Patrón frases que sean preguntas. La función retorna la lista con las coincidencias
def questions(txt):
    #El patrón asegura que haya un signo de pregunta al inicio y al final de la expresión o solo al 
    #final (en el caso de las preguntas en inglés) que puede tener cualquier caracter alfanumérico, 
    #espacios y signos de puntuación.
    pattern = r'\¿[^\n\¡\!]+\?|[^\n\¿\¡\!]+\?'
    coincidences = re.findall(pattern, txt, flags = re.IGNORECASE)
    return coincidences

#Patrón frases que sean exclamaciones. La función retorna la lista con las coincidencias
def exclamations(txt):
    #El patrón asegura que haya un signo de exclamación al inicio y al final de la expresión o solo al 
    #final (en el caso de las preguntas en inglés) que puede tener cualquier caracter alfanumérico, 
    #espacios y signos de puntuación.
    pattern = r'¡[^¡!¿\?]*?!|[^¡!¿\?\n]+!'
    coincidences = re.findall(pattern, txt, flags = re.IGNORECASE)
    return coincidences

#Funcion que carga el archivo y retorna el texto completo
def readTxt():
    with open('punto 3/cybercrime_file.txt', 'r', encoding="utf-8") as file:
        content = file.readlines()

    text = ""

    for line in content:
        text += line

    return text

#Funcion que muestra las coincidencias
def showCoincidences():
    all_content = readTxt()

    print(f"Expresiones que son preguntas: ")
    for q in questions(all_content):
        print(f"*{q}")

    print(f"\nExpresiones que son exclamaciones: ")
    for e in exclamations(all_content):
        print(f"*{e}")

    print(f"\nExpresiones que son abreviaciones: ")
    for a in abreviations(all_content):
        print(f"*{a}")

    print(f"\nTotal preguntas: {len(questions(all_content))}")
    print(f"Total exclamaciones: {len(exclamations(all_content))}")
    print(f"Total abreviaciones: {len(abreviations(all_content))}")


if __name__ == '__main__':
    showCoincidences()