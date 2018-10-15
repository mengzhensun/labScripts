import sys
import os
import numpy as np
#the first argu is the name of pdb
#the second argu is the num of mutations
#the third argu is the num of build run
#the fourth argu is the num of repair times
#the fifth argu is the chain name
pdb = sys.argv[1]
nofm = sys.argv[2]
nofr = sys.argv[3]
nofrepair = sys.argv[4]
r = int(nofrepair)
#repair
for i in range(r):
    command = "./repair.sh "+pdb+".pdb"
    print(command)
    os.system(command)
    command = "mv "+pdb+"_Repair.pdb "+pdb +".pdb" 
    print(command)
    os.system(command)
#build
command = "./build.sh "+pdb+".pdb "+nofr
print(command)
os.system(command)
chain = sys.argv[5]
m = int(nofm)
r = int(nofr)
#interaction energy in a list of list wtE, wtE[0] is r energy of first mutation one etc.
wtE = []
mtE = []
ddG = []
avgddG = []
stdDev = []
for t in range(m):
    wtE.append([])
    mtE.append([])
    ddG.append([])
for i in range(m):
    for j in range(r):
        name1 = "WT_"+pdb+"_"+str(i+1)+"_"+str(j)
        name2 = pdb+"_"+str(i+1)+"_"+str(j)
        print (name1, name2)
        # calculate wt energy
        os.system("./complex.sh " + name1+".pdb"+" "+'A')
        os.system("cat Interaction_" + name1 + "_AC.fxout|grep '.pdb' > temp.txt")
        f = open("temp.txt", 'r')
        res1 = f.read().split('\t')
        e1 = float(res1[5])
        wtE[i].append(e1)
        f.close()
        # calculate mt energy
        os.system("./complex.sh " + name2 +".pdb"+" "+'A')
        os.system("cat Interaction_" + name2 + "_AC.fxout|grep '.pdb' > temp.txt")
        f = open("temp.txt", 'r')
        res2 = f.read().split('\t')
        e2 = float(res2[5])
        mtE[i].append(e2)
        f.close()
        ddG[i].append(e2-e1)
    avgddG.append(round(np.mean(ddG[i]),4))
    stdDev.append(round(np.std(ddG[i]),4))
f1 = open("avgddG.txt", "w")
for e in avgddG:
    f1.write("%s\n" % e)
f1.close()
f2 = open("stdDev.txt", "w")
for e in stdDev:
    f2.write("%s\n" % e)
f2.close()