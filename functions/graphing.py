import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


def makeHisto(x, fileName):
    print('Plotting histogram.')
    num_bins = 5

    fig, ax = plt.subplots()

    n, bins, patches = plt.hist(x, num_bins)

    # labelling
    ax.set_xlabel('Number of Featured Articles')
    ax.set_ylabel('Number of Products')
    ax.set_title('Distribution of Featured Articles\non ' +
                 str(datetime.now().date()))

    # show proper ticks
    plt.xticks(range(0, 5))

    plt.savefig(fileName)
    print('Plot created and saved.')
    return()
