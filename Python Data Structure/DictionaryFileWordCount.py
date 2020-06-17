name=input('Enter file name= ')

try:
    handle=open(name)
except:
    print('File not found')

counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

bigcount=None
bigword=None

for k,v in counts.items():
    if bigcount is None or v>bigcount:
        bigcount=v
        bigword=k

print(bigword,bigcount)
