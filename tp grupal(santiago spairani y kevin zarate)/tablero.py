from coordenada import Coordenada

class Sonda:
    def __init__(self, fila, columna):
        self.coordenada = Coordenada(fila, columna)

    def activar(self, tablero):
        for naufrago in tablero.naufragos:
            if naufrago.rescatado == False:
                if naufrago.coordenada.es_igual_a(self.coordenada):
                    naufrago.rescatar()
                    tablero.actualizar(self.coordenada.fila, self.coordenada.columna, "N")
                    return "rescatado"

        en_cruz = False

        for naufrago in tablero.naufragos:
            if naufrago.rescatado == False:
                if naufrago.coordenada.fila == self.coordenada.fila or naufrago.coordenada.columna == self.coordenada.columna:
                    en_cruz = True

        if en_cruz:
            tablero.actualizar(self.coordenada.fila, self.coordenada.columna, "*")
            return "cruz"
        else:
            tablero.actualizar(self.coordenada.fila, self.coordenada.columna, ".")
            return "agua"
