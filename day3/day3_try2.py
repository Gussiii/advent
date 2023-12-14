#%%
from pathlib import Path
import re

pattern = r"(\d+)"



data = 'data.txt'

index = Path(data).read_text()
number_poss = [(m.start(), m.end(), int(m.group())) for m in  re.finditer(pattern, index.replace('\n',''))]

file = Path(data).read_text().splitlines()
matrix = [line for line in file]
n_row = len(matrix)
n_col = len(matrix[0])
count = 0

# %%
count = 0
counted = False
for number in number_poss:
    col = number[0]//n_row
    min_ind = (number[0]%n_col) - 1
    max_ind = (number[1]%n_col) + 1

    if min_ind < 0:
        min_ind = 0
    if max_ind > n_col:
        max_ind = n_col
    
    if min_ind > max_ind:
        min_ind , max_ind = max_ind, max_ind

    if col == 0:
        s = ''.join(matrix[col][min_ind:max_ind] + matrix[col+1][min_ind:max_ind])
        local_mat = [matrix[col][min_ind:max_ind] , matrix[col+1][min_ind:max_ind]]
    elif col == n_row-1:
        s = ''.join(matrix[col-1][min_ind:max_ind] + matrix[col-2][min_ind:max_ind])
        local_mat = [matrix[col-1][min_ind:max_ind], matrix[col-2][min_ind:max_ind] ]
    else:
        s = ''.join(matrix[col-1][min_ind:max_ind] + matrix[col][min_ind:max_ind] + matrix[col+1][min_ind:max_ind])
        local_mat = [matrix[col-1][min_ind:max_ind], matrix[col][min_ind:max_ind], matrix[col+1][min_ind:max_ind]]

    if re.findall(r'[^0-9\.]', s) != []:
        counted = True
        # print(local_mat, number, counted)
        count += number[2]


    else:
        if local_mat == ['', '', '']:
            print(local_mat, number, counted)
        # if len(local_mat) < 3:
        #     counted = False
        #     print(local_mat, number, counted)
        # break

print(count)
    

# %%
