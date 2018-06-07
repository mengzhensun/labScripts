from numpy import genfromtxt
from IPython.core.debugger import Pdb
import math
ipdb = Pdb()
data = genfromtxt('10nsScan.csv', delimiter=',')
print(data)
ipdb.set_trace()
res = []
for i in range(2, len(data)):
    for a in data[i]:
        if math.isnan(a) == False:
            res.append(a)
res.sort()
print (res[:15])
print (res[:10])
