def abbreviate(words):
    resultado = ''
    words = words.replace("-", " ").replace("   ", " ")
    words = words.replace("  ", " ").replace("_", "")
    words = words.upper()
    words = words.split(' ')
    for x in words:
        resultado = resultado + x[0]
    return resultado
