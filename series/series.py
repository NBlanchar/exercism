def slices(cadena, longitud):
    if(len(cadena) >= longitud and longitud >= 1):
        resultado = []
        for x in range(len(cadena)):
            serie = cadena[x:x+longitud]
            if(len(serie) == longitud):
                resultado.append(serie)
        return resultado
    else:
        raise ValueError('error')
