def is_armstrong_number(number):
    cadena = str(number)
    count = 0
    for numero in cadena:
        potencia = int(numero) ** len(cadena)
        count = count + potencia
    if count == number:
        return True
    else:
        return False
