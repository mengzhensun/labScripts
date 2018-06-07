from numpy import genfromtxt
from IPython.core.debugger import Pdb
import math
ipdb = Pdb()
data = genfromtxt('10nsScan.csv', delimiter=',')
#print(data)
#ipdb.set_trace()
res = []
resMatrix = []
for i in range(2, len(data)):
    resMatrix.append([])
    for a in data[i]:
        if math.isnan(a) == False:
            res.append(a)
	    resMatrix[i-2].append(a)
res.sort()
for i in range(len(resMatrix)):
    resMatrix[i].sort()
    print (resMatrix[i])
#print (res[:15])
#print (res[:10])
