#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shoblin
#
# Created:     27.11.2019
# Copyright:   (c) Shoblin 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt

from random_walks import RandomWalk

def main():
    while True:
        rw = RandomWalk(50000)
        rw.fill_walk()

        # Set the size of the plotting window.
        plt.figure(figsize=(10, 6))

        point_numbers = list(range(rw.number_points))
        plt.scatter(rw.x_values, rw.y_values, c = point_numbers,
                    cmap = plt.cm.viridis, edgecolor='none', s=1)

        # Emphasize the first and last points.
        plt.scatter(0, 0, c='green', edgecolors='none', s=10)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
                    edgecolors='none', s=10)

        # Remove the axes.
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)

        plt.show()

        keep_running = input("Make another walk? (y/n): ")
        if keep_running == 'n':
            break

if __name__ == '__main__':
    main()
