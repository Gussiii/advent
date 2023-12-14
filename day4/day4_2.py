#%%
from pathlib import Path
import re

file = Path('data.txt').read_text().splitlines()
pattern = '(\d+)'
total_points = 0

card_count= dict(
    zip(
        [i for i in range(1,len(file)+1)],
        [1 for _ in range(1,len(file)+1)]))


#%%
for current_card, line in enumerate(file):
    current_card = current_card + 1
    
    winning_nums = re.findall(pattern,line.split('|')[0].split(':')[-1])
    play_nums = re.findall(pattern,line.split('|')[-1])
    winning = sum([1 if num in winning_nums else 0 for num in play_nums])
    
    if winning > 0:
        for _ in range(0,card_count[current_card]):
            for card in range(current_card+1,current_card+winning+1):
                card_count[card] += 1


print(sum(card_count.values()))
