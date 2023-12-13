import re 

pattern = r'(?=(zero|one|two|three|four|five|six|seven|eight|nine|[1-9]))'

str_2_num = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}

file = open('data_2.txt', 'r')
Lines = file.readlines()
 
count = 0
for line in Lines:
    matches = re.finditer(pattern,line)
    matches = [match.group(1) for match in matches]

    x0 = matches[0]
    x1 = matches[-1]

    if x0 in str_2_num.keys():
        x0 = str_2_num[x0]
    if x1 in str_2_num.keys():
        x1 = str_2_num[x1]
    count += int(x0+x1)

print(count)
