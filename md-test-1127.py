#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import os
import numpy as np


# In[ ]:


#10ns
for i in range(3, 13):
    p = "10ns/" + str(i)
    ps = "../loop-structure-1126/"
    comm = "mkdir -p "+p
    print comm
    os.system(comm)
    comm = "cp "+ ps + str(i)+".mae "+p
    print comm
    os.system(comm)
    comm = "cp complex_NPT_10ns.msj "+p
    print comm
    os.system(comm)
    comm = "cp MDrun_10ns.sh "+p
    print comm
    os.system(comm)
    comm = '/home/friesner/ms5134/loop-structure-1126-md/'+p
    #omm='/home/mengzhen/Documents/18Mar_eOD-GT8/input_structure_TC_1126/input_mae/loop-structure-1126-md/'+p
    print comm
    os.chdir(comm)
    comm = './MDrun_10ns.sh '+str(i)+'.mae' 
    print comm
    os.system(comm)
    comm = '/home/friesner/ms5134/loop-structure-1126-md/'
    #omm = '/home/mengzhen/Documents/18Mar_eOD-GT8/input_structure_TC_1126/input_mae/loop-structure-1126-md/'
    print comm
    os.chdir(comm)
    
    


# In[ ]:


for i in range(3, 13):
    p = "./150ns/" + str(i)
    ps = "../loop-structure-1126/"
    comm = "mkdir -p "+p
    print comm
    os.system(comm)
    comm = "cp "+ ps + str(i)+".mae "+p
    print comm
    os.system(comm)
    comm = "cp complex_NPT.msj "+p
    print comm
    os.system(comm)
    comm = "cp MDrun.sh "+p
    print comm
    os.system(comm)
    comm = '/home/friesner/ms5134/loop-structure-1126-md/'+p
    print comm
    os.chdir(comm)
    comm = './MDrun.sh '+str(i)+'.mae' 
    print comm
    os.system(comm)
    comm = '/home/friesner/ms5134/loop-structure-1126-md/'
    print comm
    os.chdir(comm)

