import copy


class Puzzle:
    def __init__(self, args):
        self.matriz = [[0 for i in range(3)] for i in range(3)]
        self.profundidad = 0
        self.padre = None
        self.coste = 0
        self.x, self.y = 0, 0
        i, j = 0, 0
        if args is not None:
            for val in args:
                if val == 0:
                    self.x, self.y = i, j
                self.matriz[i][j] = val
                if j == 2:
                    j = 0
                    i += 1
                else:
                    j += 1

    def __str__(self):
        i, j = 0, 0
        cad = ''
        while i <= 2 and j <= 2:
            cad += str(self.matriz[i][j]) + ' '
            if j == 2:
                j = 0
                i += 1
                cad += '\n'
            else:
                j += 1
        return cad

    def __radd__(self, other):
        return other + str(self)

    def __add__(self, other):
        return str(self) + other

    def __eq__(self, other):
        i, j = 0, 0
        igual = True
        while igual and i <= 2 and j <= 2:
            if self.matriz[i][j] != other.matriz[i][j]:
                igual = False
            if j == 2:
                j = 0
                i += 1
            else:
                j += 1
        return igual

    def getProfundidad(self):
        return self.profundidad

    def getCoste(self):
        return self.coste

    def setCoste(self, alg):
        if alg == "Greedy":
            self.coste = self.costeManhattan()
        elif alg == "AEstrella":
            self.coste = self.costeManhattan() + self.profundidad

    def getPadre(self):
        return self.padre

    def getMatriz(self):
        return ''.join(str(value) for lista in self.matriz for value in lista)

    def move(self, mov, alg, mode):
        hijo = self.copy()
        hijo.padre = self.copy()
        hijo.profundidad += 1
        hijo.setCoste(alg)
        if mov == 'up':
            if self.x > 0:
                hijo.intercambia(self.x - 1, self.y)
        elif mov == 'left':
            if self.y > 0:
                hijo.intercambia(self.x, self.y - 1)
        elif mov == 'right':
            if self.y < 2:
                hijo.intercambia(self.x, self.y + 1)
        elif mov == 'down':
            if self.x < 2:
                hijo.intercambia(self.x + 1, self.y)
        if mode == 2:
            print "    Hijo generado: Move " + mov + " " + hijo.getMatriz()
        return hijo

    def intercambia(self, posx, posy):
        self.matriz[self.x][self.y], self.matriz[posx][posy] = self.matriz[posx][posy], self.matriz[self.x][self.y]
        self.x, self.y = posx, posy

    def generaCaminos(self, alg, mode):
        caminos = []
        if self.x == 0:
            if self.y == 0:
                caminos.append(self.move('down', alg, mode))
                caminos.append(self.move('right', alg, mode))
            elif self.y == 1:
                caminos.append(self.move('down', alg, mode))
                caminos.append(self.move('left', alg, mode))
                caminos.append(self.move('right', alg, mode))
            elif self.y == 2:
                caminos.append(self.move('down', alg, mode))
                caminos.append(self.move('left', alg, mode))
        elif self.x == 1:
            if self.y == 0:
                caminos.append(self.move('up', alg, mode))
                caminos.append(self.move('right', alg, mode))
                caminos.append(self.move('down', alg, mode))
            elif self.y == 1:
                caminos.append(self.move('down', alg, mode))
                caminos.append(self.move('left', alg, mode))
                caminos.append(self.move('right', alg, mode))
                caminos.append(self.move('up', alg, mode))
            elif self.y == 2:
                caminos.append(self.move('down', alg, mode))
                caminos.append(self.move('left', alg, mode))
                caminos.append(self.move('up', alg, mode))
        elif self.x == 2:
            if self.y == 0:
                caminos.append(self.move('up', alg, mode))
                caminos.append(self.move('right', alg, mode))
            elif self.y == 1:
                caminos.append(self.move('up', alg, mode))
                caminos.append(self.move('left', alg, mode))
                caminos.append(self.move('right', alg, mode))
            elif self.y == 2:
                caminos.append(self.move('up', alg, mode))
                caminos.append(self.move('left', alg, mode))
        return caminos

    def solucion(self):
        if self.matriz[0][0] != 1:
            return False
        if self.matriz[0][1] != 2:
            return False
        if self.matriz[0][2] != 3:
            return False
        if self.matriz[1][0] != 4:
            return False
        if self.matriz[1][1] != 0:
            return False
        if self.matriz[1][2] != 5:
            return False
        if self.matriz[2][0] != 6:
            return False
        if self.matriz[2][1] != 7:
            return False
        if self.matriz[2][2] != 8:
            return False
        return True

    def costeManhattan(self):
        coste = 0
        fin = [1, 2, 3], [4, 0, 5], [6, 7, 8]
        i, j = 0, 0
        while i <= 2 and j <= 2:
            if self.matriz[i][j] != fin[i][j]:
                k, l = 0, 0
                while k <= 2 and l <= 2:
                    if self.matriz[i][j] == fin[k][l]:
                        coste += abs(k - i) + abs(l - j) + 1
                        break
                    if l == 2:
                        l = 0
                        k += 1
                    else:
                        l += 1
            if j == 2:
                j = 0
                i += 1
            else:
                j += 1
        return coste

    def costeEstrella(self):
        return self.costeManhattan() + self.getProfundidad()

    def copy(self):
        return copy.deepcopy(self)
