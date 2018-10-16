#!/bin/bash
pdb=$1
../foldx --command=RepairPDB --pdb=$pdb > RepairPDB.out
