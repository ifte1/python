x=open('mbox-short.txt')
count=0
for line in x:
    count=count+1
    #print(line)
    line=line.rstrip()
    if line.startswith('i '):
        print (line)
print(count)
p=x.read()
print(len(p))
print(p[0:2])
