#!/usr/bin/env python3
import sys
from random import randrange
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

def create_voronoi_for_state(state_name, points):
    vor = Voronoi(points)
    fig = voronoi_plot_2d(vor)
    plt.savefig(f'{state_name}.png')


def get_random_point_array():
    # generate random numbers between 0-1
    return [[randrange(10), randrange(10)] for _ in range(10)]

def main():
    print('todo')

if __name__=='__main__':
    main()