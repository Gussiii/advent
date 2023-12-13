from pathlib import Path
import re

file = Path('samp.txt').read_text()#.splitlines()
print(file)

matches = re.finditer('[^0-9\.]',file)
indices = [m.start(0) for m in matches]
print(indices)

file[10]