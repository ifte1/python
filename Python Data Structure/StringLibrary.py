x='abc'
y='ABCk'
print(x.capitalize())
print(y.capitalize())

print(x.find('c'))
print(y.find('k'))

print(x.upper())
print(y.lower())

c=x.replace('ab','xk')
print(c)

a="   hello ifte    "
print(a.lstrip()) #left strip
print(a.rstrip()) #Right strip 
print(a.strip())