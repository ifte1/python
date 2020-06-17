counts=dict()
line=input('enter some line= ')
word=line.split()
print (word)

print('countings...')
for w in word:
    counts[w]=counts.get(w,0)+1

print(counts)