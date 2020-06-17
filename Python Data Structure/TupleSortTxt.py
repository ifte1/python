#top 10 most common word
fhand=open('romeo.txt')
counts=dict()
for line in fhand:
    word=line.split()
    for w in word:
        counts[w]=counts.get(w,0)+1


lst=list()
for k,v in counts.items():
    lst.append((v,k))
lst=sorted(lst,reverse=True)
for val,key in lst[:10]:
    print(key,val)

#we can do line 11 to 15 in one line
print(sorted([(v,k) for k,v in counts.items()],reverse=True))
