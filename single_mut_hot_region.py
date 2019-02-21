import sys
import os

file=open("mutation.txt", "r")
mut=file.readlines()
file.close()
mut
l=len(mut)
mutnum_l=[x.split(':')[1] for x in [m.split("->")[0] for m in mut]]
path = '/home/friesner/ms5134/loop-structure-0111-fep/truncated-10-hot-region/prime10-single-mutation/all-char-7-fillres-sidechain/'
for i in range(0, 1):
    cur = path+mutnum_l[i]+'/'
    comm = 'mkdir -p '+ cur
    print(comm)
    os.system(comm)
    comm = 'cp ' + path + 'template/* '+cur 
    print(comm)
    os.system(comm)
    mutfile = cur+"mutation_"+mutnum_l[i]+'.txt'
    file=open(mutfile, "w")
    file.write(mut[i])
    file.close()
    os.chdir(cur)
    comm = './run-with-restregion.sh 5IES180508.mae '+mutnum_l[i]+' '+"mutation_"+mutnum_l[i]+'.txt'
    print(comm)
    os.system(comm)
    os.chdir(path)
