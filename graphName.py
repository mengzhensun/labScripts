import commands
import re
f = open('mutation.edge', 'r')
x = f.readlines()
f.close
pair = {}
for a in x:
    value = a[0:7] + '_' + a[8:15]
    key = re.findall(r'[A-Z]{3}[0-9]{2,3}[A-Z]{3}',a)[0]
    pair[key] = value
Name = []
mutationName = []
for key, value in pair.iteritems():
    Name.append(value)
    mutationName.append(key[3:])
# file1 = open('mutationNameGraph.txt', 'w')
# file2 = open('graphName.txt', 'w')
# for item in Name:
#     file1.write("%s\n" % item)
# for item in mutationName:
#     file2.write("%s\n" % item) 
# file1.close()
# file2.close()
for name in Name:
    solName = "tar xzf *"+ name + "_slovent_9*"
    compName = "tar xzf *" + name + "_complex_8*"
    output = commands.getoutput(solName)
    output = commands.getoutput(compName)
output = commands.getoutput("mkdir graph")
i = 0
for name in Name:
    solName = "*" + name + "_solvent_"
    compName = "*" + name + "_complex_"
    graphName = mutationName[i]
    solventCopy =  "cp " + solName + "fep1/" + solName + "*/freeenergy_time.png graph/" + graphName + ".png"
    complexCopy =  "cp " + compName + "fep1/" + compName + "*/freeenergy_time.png graph/" + graphName + ".png"
    output = commands.getoutput(solventCopy)
    output = commands.getoutput(complexCopy)
    i += 1
output = commands.getoutput("tar -cvzf graph.tgz ./graph")

