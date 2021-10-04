import string


def count_words(sentence):
    sentence = sentence.lower()
    for puntuacion in string.punctuation:
        if(puntuacion != "'"):
            sentence = sentence.replace(puntuacion, " ")
    sentence = sentence.replace('\n', ' ').replace('\t', ' ')
    sentence = sentence.replace('  ', ' ')
    sentence = sentence.split(" ")

    resultado = {}
    for x in range(len(sentence)):
        palabra = sentence[x]
        if(palabra.count("'") > 1):
            sentence[x] = palabra.replace("'", "")
    print(sentence)
    for palabra in sentence:
        if(palabra.count("'") > 1):
            palabra = palabra.replace("'", "")
        if palabra != '':
            resultado[palabra] = sentence.count(palabra)
    return resultado
        