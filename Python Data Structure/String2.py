str1="mango"
str2="banana"
str3=str1+str2

index=0
while index < len(str3):
    letter=str3[index]
    print(index,letter)
    index=index+1

print(str3[7])
print(str3[:5])
print(str3[5:])
print(str3[4:8])