#!/bin/bash
pdb=$1
chain=$2
../foldx --command=AnalyseComplex --pdb=$pdb --analyseComplexChains=$chain >> AnalyseComplex_output.txt
