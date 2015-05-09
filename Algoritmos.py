import datetime


class Algoritmos:
    def __init__(self, alg, mode, inicio, limite):
        self.estabiertos = []
        self.estcerrados = []
        self.maxabiertos, self.maxcerrados = 0, 0
        self.visitados = 0
        self.algoritmo = alg
        self.mode = mode
        self.inicial = inicio
        self.inicial.setCoste(self.algoritmo)
        self.limite = limite

    def inicia(self):
        salida = ""
        a = datetime.datetime.now()
        if self.algoritmo == "Anchura":
            final = self.busquedaAnchura()
        elif self.algoritmo == "Profundidad":
            final = self.busquedaProfundidad()
        elif self.algoritmo == "ProfundidadIterativa":
            final = self.busquedaProfundidadIter()
        elif self.algoritmo == "Greedy":
            final = self.busquedaGreedyEstrella()
        elif self.algoritmo == "AEstrella":
            final = self.busquedaGreedyEstrella()
        b = datetime.datetime.now()
        time = b - a

        if self.mode == 0:
            salida += self.algoritmo + "," + self.inicial.getMatriz() + ","
            salida += str(final.getProfundidad()) + "," + str(self.visitados) + ","
            salida += str(self.getAbiertos()) + "," + str(self.getCerrados()) + "," + str(time.microseconds / 100)
        elif self.mode == 1 or self.mode == 2:
            if self.mode == 1:
                print final
                aux = final.getPadre()
                while aux is not None:
                    print aux
                    aux = aux.getPadre()

            if final.solucion():
                salida += "\nSe ha encontrado solucion"
                salida += "\nProfundidad: " + str(final.getProfundidad())
            else:
                salida += "\nNo se ha encontrado solucion"
            salida += "\nNodos visitados: " + str(self.visitados)
            salida += "\nEstados abiertos: " + str(self.getAbiertos())
            salida += "\nEstados cerrados: " + str(self.getCerrados())
            salida += "\nTiempo empleado: " + str(time.microseconds / 100) + " ms\n"
        print salida

    def busquedaAnchura(self):
        self.estabiertos.append(self.inicial)
        actual = self.estabiertos[0]
        self.visitados += 1
        while not actual.solucion() and len(self.estabiertos) > 0:
            self.estcerrados.append(actual)
            self.estabiertos.remove(actual)
            if self.mode == 2:
                print "\nSe expande el nodo ", actual.getMatriz()
            hijos = actual.generaCaminos(None, self.mode)
            self.tratarRepetidosAnchura(hijos)
            if len(self.estabiertos) > self.maxabiertos:
                self.maxabiertos = len(self.estabiertos)
            if len(self.estcerrados) > self.maxcerrados:
                self.maxcerrados = len(self.estcerrados)
            if len(self.estabiertos) > 0:
                actual = self.estabiertos[0]
                self.visitados += 1
        return actual

    def busquedaProfundidad(self):
        self.estabiertos.append(self.inicial)
        actual = self.estabiertos[0]
        self.visitados += 1
        while not actual.solucion() and len(self.estabiertos) > 0:
            self.estcerrados.append(actual)
            if actual.getProfundidad() < self.limite:
                if self.mode == 2:
                    print "\nSe expande el nodo ", actual.getMatriz()
                hijos = actual.generaCaminos(None, self.mode)
                self.tratarRepetidosAnchura(hijos)
            if len(self.estabiertos) > self.maxabiertos:
                self.maxabiertos = len(self.estabiertos)
            if len(self.estcerrados) > self.maxcerrados:
                self.maxcerrados = len(self.estcerrados)
            if len(self.estabiertos) > 0:
                actual = self.estabiertos.pop()
                self.visitados += 1
        return actual

    def busquedaProfundidadIter(self):
        prof = 0
        self.estabiertos.append(self.inicial)
        actual = self.estabiertos[0]
        while not actual.solucion() and prof <= self.limite:
            self.estabiertos.append(self.inicial)
            actual = self.estabiertos[0]
            self.visitados += 1
            while not actual.solucion() and len(self.estabiertos) > 0:
                self.estcerrados.append(actual)
                if actual.getProfundidad() < self.limite:
                    if self.mode == 2:
                        print "\nSe expande el nodo ", actual.getMatriz()
                    hijos = actual.generaCaminos(None, self.mode)
                    self.tratarRepetidosAnchura(hijos)
                    if len(self.estabiertos) > self.maxabiertos:
                        self.maxabiertos = len(self.estabiertos)
                    if len(self.estcerrados) > self.maxcerrados:
                        self.maxcerrados = len(self.estcerrados)
                if len(self.estabiertos) > 0:
                    actual = self.estabiertos.pop()
                    self.visitados += 1
            del self.estabiertos[:]
            prof += 1
        return actual

    def busquedaGreedyEstrella(self):
        self.estabiertos.append(self.inicial)
        actual = self.estabiertos[0]
        self.visitados += 1
        while not actual.solucion() and len(self.estabiertos) > 0:
            self.estcerrados.append(actual)
            self.estabiertos.remove(actual)
            if self.mode == 2:
                print "\nSe expande el nodo ", actual.getMatriz()
            hijos = actual.generaCaminos(self.algoritmo, self.mode)
            self.tratarRepetidosGreedy(hijos)
            if len(self.estabiertos) > self.maxabiertos:
                self.maxabiertos = len(self.estabiertos)
            if len(self.estcerrados) > self.maxcerrados:
                self.maxcerrados = len(self.estcerrados)
            if len(self.estabiertos) > 0:
                actual = self.estabiertos[0]
                self.visitados += 1
        return actual

    def tratarRepetidosAnchura(self, hijos):
        if self.mode == 2:
            print "\nTratando repetidos: "
        for nodo in hijos:
            i = 0
            encontrado = False
            while not encontrado and i < len(self.estabiertos):
                if self.estabiertos[i] == nodo:
                    if self.mode == 2:
                        print "    Nodo repetido, se descarta ", nodo.getMatriz()
                    encontrado = True
                    break
                else:
                    i += 1
            i = 0
            while not encontrado and i < len(self.estcerrados):
                if self.estcerrados[i] == nodo:
                    if self.mode == 2:
                        print "    Nodo repetido, se descarta ", nodo.getMatriz()
                    encontrado = True
                    break
                else:
                    i += 1
            if not encontrado:
                if self.mode == 2:
                    print "    Nodo no visitado, se agrega " + nodo.getMatriz()
                self.estabiertos.append(nodo)

    def tratarRepetidosProfundidad(self, hijos):
        if self.mode == 2:
            print "\nTratando repetidos: "
        for nodo in hijos:
            i = 0
            encontrado = False
            while not encontrado and i < len(self.estcerrados):
                if self.estcerrados[i] == nodo:
                    if nodo.getProfundidad() < self.estcerrados[i].getProfundidad():
                        if self.mode == 2:
                            print "    Nodo repetido, profundidad menor, se intercambia ", nodo.getMatriz()
                        del self.estcerrados[i]
                        self.estabiertos.append(nodo)
                        encontrado = True
                        break
                    else:
                        if self.mode == 2:
                            print "    Nodo repetido, profundidad mayor, se descarta ", nodo.getMatriz()
                        encontrado = True
                        break
                else:
                    i += 1
            i = 0
            while not encontrado and i < len(self.estabiertos):
                if self.estabiertos[i] == nodo:
                    if self.mode == 2:
                        print "    Nodo repetido, se descarta ", nodo.getMatriz()
                    encontrado = True
                    break
                else:
                    i += 1
            if not encontrado:
                if self.mode == 2:
                    print "    Nodo no visitado, se agrega " + nodo.getMatriz()
                self.estabiertos.append(nodo)

    def tratarRepetidosGreedy(self, hijos):
        if self.mode == 2:
            print "\nTratando repetidos: "
        for nodo in hijos:
            i = 0
            encontrado = False
            while not encontrado and i < len(self.estcerrados):
                if self.estcerrados[i] == nodo:
                    if nodo.getCoste() < self.estcerrados[i].getCoste():
                        if self.mode == 2:
                            print "    Nodo repetido, coste menor, se reabre ", nodo.getMatriz()
                        del self.estcerrados[i]
                        self.estabiertos.append(nodo)
                        encontrado = True
                        break
                    else:
                        if self.mode == 2:
                            print "    Nodo repetido, coste mayor, se descarta ", nodo.getMatriz()
                        encontrado = True
                        break
                else:
                    i += 1
            i = 0
            while not encontrado and i < len(self.estabiertos):
                if self.estabiertos[i] == nodo:
                    if nodo.getCoste() < self.estabiertos[i].getCoste():
                        if self.mode == 2:
                            print "    Nodo repetido, coste menor, se intercambia ", nodo.getMatriz()
                        del self.estabiertos[i]
                        self.estabiertos.append(nodo)
                        encontrado = True
                        break
                    else:
                        if self.mode == 2:
                            print "    Nodo repetido, coste mayor, se descarta ", nodo.getMatriz()
                        encontrado = True
                        break
                else:
                    i += 1
            if not encontrado:
                if self.mode == 2:
                    print "    Nodo no visitado, se agrega " + nodo.getMatriz()
                self.estabiertos.append(nodo)
        self.estabiertos = sorted(self.estabiertos, key=lambda puzzle: puzzle.getCoste())

    def getAbiertos(self):
        return self.maxabiertos

    def getCerrados(self):
        return self.maxcerrados
