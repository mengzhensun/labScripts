
import sys
import os
import numpy as np


for i in range(3, 13):
    p = str(i)
    ps = "../../loop-structure-1126/truncated/"
    comm = "mkdir -p "+p
    print comm
    os.system(comm)
    comm = "cp "+ ps + str(i)+".mae "+p
    print comm
    os.system(comm)
    comm = "cp template/* "+p
    print comm
    os.system(comm)
    comm = '/home/friesner/ms5134/loop-structure-0111-fep/truncated-10ns/'+p
    print comm
    os.chdir(comm)
    comm = './run.sh '+str(i)+'.mae'
    print comm
    os.system(comm)
    comm = '/home/friesner/ms5134/loop-structure-0111-fep/truncated-10ns/'
    print comm
    os.chdir(comm)
