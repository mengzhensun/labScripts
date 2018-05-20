f = open('diedJob.txt')
lines = f.readlines()
g = open('namecleanDiedJob.txt', 'w')
k = open('datecleanDiedJob.txt', 'w')
f.close()
for a in lines:
    if (lines.index(a)%2==1):
        g.write(a[15:30])
        g.write("\n")
    else:
        k.write(a[19:25])
        k.write("\n")
g.close()
