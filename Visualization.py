import itertools
from typing import Tuple, List
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import utils as ut
from collections import Counter

from PBSclasses import Encounter


def plot_all_encounter_map_types(encounter_list, size=(50, 50), remove_map_number=False) -> Tuple[plt.Figure,plt.Axes]:
    d_name, d_type, map_names = ut.get_dicts_encounters_name_type(encounter_list, remove_map_number)

    l1, l2 = ut.find_sizes_of_subplots(len(map_names))
    f, ax = plt.subplots(l1, l2)
    f.set_size_inches(size)

    k = 0
    for i, j in itertools.product(range(l1), range(l2)):
        if (k < len(map_names)):
            f, ax = add_type_bar(d_type[map_names[k]], f, ax, (i, j), area_name=map_names[k])
        else:
            ax[i, j].set_axis_off()
        k += 1

    f.tight_layout()

    return f, ax


def plot_type_bar(type_list, color_list=None, area_name="") -> Tuple[plt.Figure,plt.Axes]:
    f, ax = plt.subplots()
    ax = add_type_bar(type_list, f, ax, color_list=color_list, area_name=area_name)
    return f, ax


def add_type_bar(type_list, figure, ax, pos=None, color_list=None, area_name="") -> Tuple[plt.Figure,plt.Axes]:
    letter_counts = Counter(type_list)

    common = letter_counts.most_common()
    labels = [item[0] for item in common]
    number = [item[1] for item in common]
    nbars = len(common)
    if (not color_list):
        color_list = [('GRASS', '#7AC74C'), ('FIRE', '#EE8130'), ('WATER', '#6390F0'), ('BUG', '#A6B91A'),
                     ('NORMAL', '#A8A77A'), ('POISON', '#A33EA1'), ('ELECTRIC', '#F7D02C'),
                     ('GROUND', '#E2BF65'), ('FAIRY', '#D685AD'), ('FIGHTING', '#C22E28'), ('PSYCHIC', '#F95587'),
                     ('ROCK', '#B6A136'), ('GHOST', '#735797'), ('ICE', '#96D9D6'), ('DRAGON', '#6F35FC'),
                     ('DARK', '#705746'), ('STEEL', '#B7B7CE'), ('FLYING', '#A98FF3')]
    bar_color = []
    for l in labels:
        for c in color_list:
            if (c[0] == l):
                bar_color.append(c[1])
                break
        if (l not in c):
            bar_color.append("#000000")
    if (pos):
        ax[pos[0], pos[1]].barh(np.arange(nbars), number, tick_label=labels, color=bar_color)
        ax[pos[0], pos[1]].set_xlabel("Number of Pokemon species")
        ax[pos[0], pos[1]].title.set_text(area_name)
    else:
        ax.barh(np.arange(nbars), number, tick_label=labels, color=bar_color)
        ax.set_xlabel("Number of Pokemon species")
        ax.title.set_text(area_name)

    return figure, ax


def show_level_scatter_plot(level_list):
    x = range(len(level_list))
    y_ticks = np.arange(0, 100, 10)
    df = pd.DataFrame({'Pokemon battled': x, 'Level': level_list})
    df.plot(kind='scatter', x='Pokemon battled', y='Level', yticks=y_ticks, title='Level of Pokemons during the game',
            c='darkblue')
    plt.yscale('linear')

    plt.show()
