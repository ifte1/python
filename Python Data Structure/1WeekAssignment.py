text = "X-DSPAM-Confidence:    0.8475"
pos=text.find(' ')
x=text[pos+4:]
x=float(x)
print(x)