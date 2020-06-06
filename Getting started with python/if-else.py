x=input("Enter score: ")

try:
    y=float(x)
except:
    print("enter right value")
    quit()
if y<0.6 :
    print("F")
elif y>=0.6 and y<0.7:
    print("D")
elif y>=0.7 and y<0.8:
    print("C")
elif y>=0.8 and y<0.9:
    print("B")
elif y>=0.9 and y<=1.0:
    print("A")
else:
    print("out of range")
    