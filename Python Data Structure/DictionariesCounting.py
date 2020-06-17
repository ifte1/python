counts=dict()
names=['ifte','rahil','ifte','sajjad','rahil','raihan']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)


#another way
counter=dict()
for name in names:
    counter[name]=counter.get(name,0)+1
print(counter)