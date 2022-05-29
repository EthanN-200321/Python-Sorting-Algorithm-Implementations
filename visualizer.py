import matplotlib.animation as animation
import matplotlib.pyplot as plt
import random
import sys

sys.path.insert(0, 'algorithms/')
from algorithms import *

def visualize(algo, nums=32):
    # Data, colours
    colours = ["#101115", "#fafafa", "#d32ce6"]
    data = list(range(1, nums + 1))
    random.shuffle(data) # Get Generator, title string
    if algo == 0:
        titlestr = "Bogosort"
        generator = bogosort(data)
    if algo == 1:
        titlestr = "Bozosort"
        generator = bozosort(data)
    if algo == 2:
        titlestr = "Bubble sort"
        generator = bubblesort(data)
    if algo == 3:
        titlestr = "Bucket Sort"
        generator = bucketsort(data)
    if algo == 4:
        titlestr = "Cocktail sort"
        generator = cocktailsort(data)
    if algo == 5:
        titlestr = "Gnome Sort"
        generator = gnomesort(data)
    if algo == 6:
        titlestr = "Insertion Sort"
        generator = insertionsort(data)
    if algo == 7:
        titlestr = "Quick Sort"
        generator = quicksort(data, 0, len(data)-1)
    if algo == 8:
        titlestr = "Selection Sort"
        generator = selectionsort(data)

    # Defining graph + parameters
    fig, ax = plt.subplots(facecolor=colours[0])
    for spine in ax.spines.values():
        spine.set_edgecolor(colours[1])
    ax.set_facecolor(colours[0])
    plt.xticks([])
    plt.yticks([])
    ax.set_xlim(0, nums)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes, color=colours[1])
    ax.set_title(titlestr, color=colours[1])

    bar_sub = ax.bar(range(len(data)), data, align="edge", color=colours[2])
    iteration = [0]


    def update(data, rects, iteration):
        if algo == 5:  # Gnome Sort
        else:
            for rect, val in zip(rects, data):
                rect.set_height(val)
            iteration[0] += 1
            text.set_text(f"# of operations: {iteration[0]}")


    anim = animation.FuncAnimation(
        fig,
        func=update,
        fargs=(bar_sub, iteration),
        frames=generator,
        repeat=False,
        blit=False,
        interval=18,
        save_count=1600
    )
    anim.save(f"{titlestr}.mp4", animation.FFMpegWriter(fps=30))
  
if __name__ == "__main__":
    for i in range(0, 8):
        visualize(algo=7)

