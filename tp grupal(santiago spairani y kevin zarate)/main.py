import random
from naufrago import Naufrago

class Tablero:
    def __init__(self):
        self.filas = 5
        self.columnas = 5
        self.grilla = []
        self.naufragos = []

        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                fila.append("~")
            self.grilla.append(fila)

    def colocar_naufragos(self, cantidad):
        while len(self.naufragos) < cantidad:
            fila = random.randint(0, 4)
            columna = random.randint(0, 4)

            repetido = False

            for naufrago in self.naufragos:
                if naufrago.ubicacion_coincide(fila, columna):
                    repetido = True

            if repetido == False:
                self.naufragos.append(Naufrago(fila, columna))

    def actualizar(self, fila, columna, simbolo):
        self.grilla[fila][columna] = simbolo

    def mostrar(self):
        print("\n   0  1  2  3  4")

        for i in range(self.filas):
            print(i, end="  ")

            for j in range(self.columnas):
                print(self.grilla[i][j], end="  ")

            print()
