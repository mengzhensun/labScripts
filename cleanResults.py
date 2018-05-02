from IPython.core.debugger import Pdb
ipdb = Pdb()
import re
f = open('mutation.edge','r')
x = f.readlines()
f.close()
b = {}
for a in x:
    key = re.findall(r'\w*\:\w*',a)[0]
    value = re.findall(r'[A-Z][A-Z][A-Z][0-9]*',a)[0]
    b[key] = value
f = open('results.txt', 'r')
y = f.readlines()
f.close()
res = {}
for a in y:
    key = re.findall(r'\w*\:\w+',a)[0]
#    ipdb.set_trace()
    ddG = re.findall(r'ddG = \-*\d*\.*\d*',a)[0]
    res[int(b[key][3:])]=ddG[6:]
#print(res)
f = open('cleanedResults.txt','w')
for key in sorted(res):
    print(key,res[key])
    f.write(res[key])
    f.write("\n")
f.close()

