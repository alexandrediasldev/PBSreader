from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

def showTypeBar(typeList, colorList=None, areaName = ""):
    fig_size = (10, 5)
    f = plt.figure(figsize=fig_size)
    f = addTypeBar(typeList,f,colorList,areaName)
    f.show()

def addTypeBar(typeList, figure,ax,pos=(0,0),colorList=None,areaName=""):

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

    ax[pos[0],pos[1]].barh(np.arange(nbars), number, tick_label=labels, color=bar_color)
    ax[pos[0],pos[1]].set_xlabel("Number of Pokemon species")
    ax[pos[0],pos[1]].title.set_text(areaName)
    #plt.subtitle("Types repartition " + areaName)
    return ax


def showLevelScatterPlot(levelList):
    x = range(len(levelList))
    y_ticks = np.arange(0, 100, 10)
    df = pd.DataFrame({'Pokemon battled': x, 'Level': levelList})
    df.plot(kind='scatter', x='Pokemon battled', y='Level', yticks=y_ticks, title='Level of Pokemons during the game',
            c='darkblue')
    plt.yscale('linear')

    plt.show()
