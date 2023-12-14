from pathlib import Path
import re

cube_max={
    'red' : 12,
    'green':13,
    'blue': 14
}

file = Path('data.txt').read_text().splitlines()

games_count = 0
ok = True
for line in file:
    
    game = line.split(':')
    game_num = int(game[0].split(" ")[-1])
    game = game[-1]
    
    games = [g for g in game.split(';')]
    for turn in games:
        cubes = [c for c in turn.split(',')]
        turn_count = {}
        for cube in cubes:
            amount = int(re.findall(r'\w*',cube)[1])
            color = re.findall(r'\w*',cube)[3]
            if color not in turn_count.keys():
                turn_count[color] = amount
            else:
                turn_count[color] += amount
        for color in turn_count.keys():
            if turn_count[color] > cube_max[color]:
                ok = False
    if ok:
        games_count += game_num
    ok = True

print(games_count)

ieanrstn 

