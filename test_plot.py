import pickle
import argparse
import subprocess
import sys

import numpy as np
from matplotlib import pyplot as plt

plt.style.use("dark_background")

fig, ax = plt.subplots()


x = np.linspace(0, 2*np.pi, 100)
y = np.sin(3*x)
ax.plot(x, y)


fig.savefig("/tmp/plot_contour.png", pad_inches=0.1, bbox_inches="tight")

subprocess.call(["kitty", "+kitten", "icat", "--align", "left", "/tmp/plot_contour.png"])


