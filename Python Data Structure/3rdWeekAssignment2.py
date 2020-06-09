# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
y=0
count=0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    s=line
    pos=s.find(' ')
    x=s[pos:]
    x=float(x)
    y=y+x
z=y/count
print("Average spam confidence: ",z)

