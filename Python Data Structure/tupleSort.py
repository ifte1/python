x=dict()
x={'a':4,'l':10,'c':15}
print(x)
p=sorted(x.items())
print(p)

for k,v in sorted(x.items()):
    print(k,v)

temp=list()
for k,v in x.items():
    temp.append((v,k))

temp=sorted(temp,reverse=True)#reverse print using value from a dict
print(temp)
