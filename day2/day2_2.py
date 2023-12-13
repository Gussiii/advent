from pathlib import Path
import re



file = Path('data.txt').read_text().splitlines()

games_count = 0
ok = True
for line in file:
    cube_max={
    'red' : 0,
    'green': 0,
    'blue': 0}
    turn_prod = 1
    
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
                cube_max[color] = turn_count[color]
    # print(cube_max)
    for color in cube_max.keys():
        # print(cube_max[color])
        turn_prod = turn_prod * cube_max[color]
    # print(turn_prod)
    games_count += turn_prod

print(games_count)

