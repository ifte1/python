def computepay(h,r):
    if h<=40:
        k=h*r
        return k
    elif h>40:
        l=h-40
        m=r*1.5*l
        p=40*r
        return m+p

    return 42.37

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

p = computepay(hrs,rate)
print("Pay",p)