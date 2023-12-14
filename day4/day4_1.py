#%%
from pathlib import Path
import re

file = Path('data.txt').read_text().splitlines()
pattern = '(\d+)'
total_points = 0

for line in file:
    local_points = 1
    
    winning_nums = re.findall(pattern,line.split('|')[0].split(':')[-1])
    play_nums = re.findall(pattern,line.split('|')[-1])
    
    winning = sum([1 if num in winning_nums else 0 for num in play_nums])
    if winning > 0:
        for point in range(1,winning):
            local_points = local_points * 2
    else:
        local_points = 0

    total_points += local_points
print(total_points)
