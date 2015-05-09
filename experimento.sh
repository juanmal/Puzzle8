#!/bin/bash
puzzles=(123456708 123758460 253176480 123406758 123056478 135048627 035148627 305148627 135648027 123406758)
algoritmos=(Anchura Profundidad ProfundidadIterativa Greedy AEstrella)

cabecera="Algoritmo,Estado Inicial,Pasos,Nodos visitados,Estados abiertos,Estados cerrados,Tiempo ejecucion"
echo $cabecera > salida.csv

progreso=0

for alg in ${algoritmos[@]}
do
    echo "" >> salida.csv
    for puzz in ${puzzles[@]}
    do
		progreso=$((progreso+2))
		echo -ne "\r Completado: $progreso%"
		out=$(python main.py ${alg} ${puzz} 0)
        echo $out >> salida.csv
    done
done
echo ""
