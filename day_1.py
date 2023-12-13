import re 

pattern = '([0-9])'

file = open('data.txt', 'r')
Lines = file.readlines()
 
count = 0
for line in Lines:
    x = re.findall(pattern,line)
    count += int(x[0]+x[-1])

print(count)
