import itertools

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import utils as ut
from collections import Counter


def plotAllEncounterMapTypes(encounterList, size=(50, 50), removeMapNumber=False):
    d_name, d_type, mapNames = ut.getDictsEncountersNameType(encounterList, removeMapNumber)

    l1, l2 = ut.findSizesOfSubplots(len(mapNames))
    f, ax = plt.subplots(l1, l2)
    f.set_size_inches(size)

    k = 0
    for i, j in itertools.product(range(l1), range(l2)):
        if (k < len(mapNames)):
            f, ax = addTypeBar(d_type[mapNames[k]], f, ax, (i, j), areaName=mapNames[k])
        else:
            ax[i, j].set_axis_off()
        k += 1

    f.tight_layout()

    return f, ax


def plotTypeBar(typeList, colorList=None, areaName=""):
    f, ax = plt.subplots()
    ax = addTypeBar(typeList, f, ax, colorList=colorList, areaName=areaName)
    return f, ax


def addTypeBar(typeList, figure, ax, pos=None, colorList=None, areaName=""):
    letter_counts = Counter(typeList)

    common = letter_counts.most_common()
    labels = [item[0] for item in common]
    number = [item[1] for item in common]
    nbars = len(common)
    if (not colorList):
        colorList = [('GRASS', '#7AC74C'), ('FIRE', '#EE8130'), ('WATER', '#6390F0'), ('BUG', '#A6B91A'),
                     ('NORMAL', '#A8A77A'), ('POISON', '#A33EA1'), ('ELECTRIC', '#F7D02C'),
                     ('GROUND', '#E2BF65'), ('FAIRY', '#D685AD'), ('FIGHTING', '#C22E28'), ('PSYCHIC', '#F95587'),
                     ('ROCK', '#B6A136'), ('GHOST', '#735797'), ('ICE', '#96D9D6'), ('DRAGON', '#6F35FC'),
                     ('DARK', '#705746'), ('STEEL', '#B7B7CE'), ('FLYING', '#A98FF3')]
    bar_color = []
    for l in labels:
        for c in colorList:
            if (c[0] == l):
                bar_color.append(c[1])
                break
        if (l not in c):
            bar_color.append("#000000")
    if (pos):
        ax[pos[0], pos[1]].barh(np.arange(nbars), number, tick_label=labels, color=bar_color)
        ax[pos[0], pos[1]].set_xlabel("Number of Pokemon species")
        ax[pos[0], pos[1]].title.set_text(areaName)
    else:
        ax.barh(np.arange(nbars), number, tick_label=labels, color=bar_color)
        ax.set_xlabel("Number of Pokemon species")
        ax.title.set_text(areaName)

    return figure, ax


def showLevelScatterPlot(levelList):
    x = range(len(levelList))
    y_ticks = np.arange(0, 100, 10)
    df = pd.DataFrame({'Pokemon battled': x, 'Level': levelList})
    df.plot(kind='scatter', x='Pokemon battled', y='Level', yticks=y_ticks, title='Level of Pokemons during the game',
            c='darkblue')
    plt.yscale('linear')

    plt.show()
