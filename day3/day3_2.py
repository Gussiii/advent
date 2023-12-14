#%%

from operator import indexOf
from pathlib import Path
import re

pattern = r"\*"

index = Path('data.txt').read_text()
index = [m.start(0) for m in re.finditer(pattern, index.replace('\n',''))]

file = Path('data.txt').read_text().splitlines()
matrix = [line for line in file]

n_row = len(matrix)
n_col = len(matrix[0])
#%%
count = 0
ratio = 1

for triger in index:
    index_target = [triger//n_row, triger%n_col]
    matrix_slice = [
        matrix[index_target[0]-1][index_target[1]-3:index_target[1]+4],
        matrix[index_target[0]][index_target[1]-3:index_target[1]+4],
        matrix[index_target[0]+1][index_target[1]-3:index_target[1]+4]]
    gears = 0
    for s in matrix_slice:
        matches = re.finditer(r"\d+", s)
        for m in matches:
            x1, x2 = m.start()-1, m.end()
            if (x1>2 and x2<4) or (x2>2 and x1<4):
                ratio = ratio * int(m.group())
                gears += 1
    if gears == 2: 
        count += ratio
    ratio = 1

print(count)

#%%

# %%
