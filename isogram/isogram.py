def is_isogram(frase):
    resultado = True
    frase = frase.upper()
    for x in frase:
        if (x == '-' or x == ' '):
            frase = frase[1:]
        else:
            caracter = frase[0]
            frase = frase[1:]
        for y in frase:
            if caracter == y:
                resultado = False
    return resultado
