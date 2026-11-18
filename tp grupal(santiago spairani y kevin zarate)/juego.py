class Coordenada:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def es_igual_a(self, otra):
        return self.fila == otra.fila and self.columna == otra.columna
