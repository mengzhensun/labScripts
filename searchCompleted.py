import commands
f = open('date.txt','r')
dat = f.readlines()
f.close()
g = open('name.txt','r')
nam = g.readlines()
g.close()
l = len(dat)
for i in range(l):
	c = "qacct -j %s | grep -B 12 \"%s\" |grep \"fgpu-\" >> diedCards.txt"%(nam[i].rstrip(),dat[i].rstrip())
	print(c)
	output = commands.getoutput(c)
