# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("file not found")
for line in fh:
    line=line.rstrip()
    line=line.upper()
    print(line)
