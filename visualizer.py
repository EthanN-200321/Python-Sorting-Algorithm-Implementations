import matplotlib.animation as animation
import matplotlib.pyplot as plt
from algorithms import bogosort as bg

a = bg.bogosort([1,3,2,43])
fig, ax = plt.subplots()
line = ax.plot()

def animate(d):
    for i in d:
        .set_ydata()
