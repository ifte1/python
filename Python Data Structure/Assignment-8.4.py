x=open('romeo.txt')
y=list()
for line in x:
    line=line.rstrip()
    word=line.split()
    for w in word:
        if w in y:
            continue
        y.append(w)
 

print(sorted(y))