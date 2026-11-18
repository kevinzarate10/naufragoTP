from tablero import Tablero
from sonda import Sonda

class Juego:
    def __init__(self):
        self.sondas = 8
        self.rescatados = 0
        self.tablero = Tablero()
        self.tablero.colocar_naufragos(4)

    def pedir_coordenada(self):
        fila = int(input("Fila (0 a 4): "))

        while fila < 0 or fila > 4:
            fila = int(input("Fila incorrecta. Ingrese de 0 a 4: "))

        columna = int(input("Columna (0 a 4): "))

        while columna < 0 or columna > 4:
            columna = int(input("Columna incorrecta. Ingrese de 0 a 4: "))

        return fila, columna

    def jugar_turno(self):
        print("\nSondas:", self.sondas)
        print("Naufragos rescatados:", self.rescatados)
        self.tablero.mostrar()

        fila, columna = self.pedir_coordenada()

        sonda = Sonda(fila, columna)
        resultado = sonda.activar(self.tablero)

        self.sondas = self.sondas - 1

        if resultado == "rescatado":
            self.rescatados = self.rescatados + 1
            print("Encontraste un naufrago")
        elif resultado == "cruz":
            print("Hay un naufrago en esa fila o columna")
        else:
            print("No hay naufragos cerca")

    def iniciar(self):
        while self.sondas > 0 and self.rescatados < 4:
            self.jugar_turno()

        self.tablero.mostrar()

        if self.rescatados == 4:
            print("Ganaste")
        else:
            print("Perdiste")
