name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = dict()                                     #create empty dictionary
hlst = []                                           #create empty list

for line in handle: 
    words = line.split()
    if len(words) > 2 and words[0] == 'From':       #Select lines with 'From'
        hr = words[5].split(':')                    #Select hour (5th index) and split string with colon
        hours[hr[0]] = hours.get(hr[0], 0) + 1    #increase count for each hour
    else:
        continue

for k,v in hours.items():                           #k = hour, v = count
    hlst.append((k,v))                               #append tuples to list

hlst.sort()                                         #sort list by hour
for k,v in hlst:                                    #loop through list of tuples
    print (k,v)  