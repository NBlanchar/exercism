def convert(num):
    resultado = ''
    if (num % 3 == 0):
        resultado = 'Pling'
    if (num % 5 == 0):
        resultado = resultado + 'Plang'
    if (num % 7 == 0):
        resultado = resultado + 'Plong'
    if (resultado == ''):
        resultado = str(num)
    return resultado
