class Matrix:
    def __init__(self, matrix_string):
        self.matriz = []
        filas = matrix_string.split('\n')
        for x in range(len(filas)):
            stringfilas = filas[x]
            datos = stringfilas.split(' ')
            fila_matriz = []
            for y in range(len(datos)):
                valor = int(datos[y])
                fila_matriz.append(valor)
            self.matriz.append(fila_matriz)        
           
    def row(self, index):
        resultado = []
        for x in range(len(self.matriz[index-1])):
            resultado.append(self.matriz[index-1][x])
        return resultado

    def column(self, index):
        resultado = []
        for x in range(len(self.matriz)):
            resultado.append(self.matriz[x][index-1])
        return resultado
