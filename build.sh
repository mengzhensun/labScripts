#!/bin/bash
pdb=$1
nofr=$2
../foldx --command=BuildModel --pdb=$pdb --mutant-file=individual_list.txt --numberOfRuns=$nofr >> BuildModel_foldx_output.txt
