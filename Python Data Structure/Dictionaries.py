purse=dict()
purse['money']=12
purse['candy']=2
purse['tissue']=75
print(purse)
print(purse['money'])

purse['candy']=purse['candy']+5
print(purse['candy'])

#using key and values function

print(purse.keys())
print(purse.values())

#using double variable in loop to access key and values

for k,v in purse.items():
    print(k,v)