import Puzzle
import Algoritmos
import sys


if len(sys.argv) > 1:
    if len(sys.argv) == 4:
        alg = sys.argv[1]
        modo = int(sys.argv[3])
        matriz = [int(x) for x in sys.argv[2]]
        if alg == "Profundidad" or alg == "ProfundidadIterativa":
            limite = 20
        else:
            limite = None
        p = Puzzle.Puzzle(matriz)
        busq = Algoritmos.Algoritmos(alg, modo, p, limite)
        busq.inicia()
    else:
        print " Parametros incorrectos\n Uso: python main.py (Algoritmo) (Matriz) (modo) \n " \
              "Algoritmo: Anchura Profundidad ProfundidadIterativa Greedy AEstrella \n " \
              "Modos: 0 - Corto // 1 - Sucesion de estados // 2 - Debug"
else:
    opcion = -1
    while opcion != 0:
        print "\n 1 Anchura\n"
        print " 2 Profundidad\n"
        print " 3 Profundidad Iterativa\n"
        print " 4 Greedy\n"
        print " 5 A*\n"
        print " 0 Salir"

        opcion = input()

        if 0 < opcion < 6:
            print "    Modo \n"
            print " 0 Corto\n"
            print " 1 Estados\n"
            print " 2 Debug\n"
            modo = input()

            print " Matriz: "
            cad = input()

            matriz = []

            for var in str(cad):
                matriz.append(int(var))

            p = Puzzle.Puzzle(matriz)
            limite = 20
            if opcion == 1:
                busq = Algoritmos.Algoritmos("Anchura", modo, p, None)
            elif opcion == 2:
                busq = Algoritmos.Algoritmos("Profundidad", modo, p, limite)
            elif opcion == 3:
                busq = Algoritmos.Algoritmos("ProfundidadIterativa", modo, p, limite)
            elif opcion == 4:
                busq = Algoritmos.Algoritmos("Greedy", modo, p, None)
            elif opcion == 5:
                busq = Algoritmos.Algoritmos("AEstrella", modo, p, None)

            busq.inicia()
