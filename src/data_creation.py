import numpy as np
import matplotlib.pyplot as plt
import src.keyboard_input as keyboard_input
import src.plot as plot


def get_input_points():

    listener = keyboard_input.start_listener()
    data_points = []
    while listener.running:
        plot.instruction("if you are ready, type escape key")
        data_points = np.asarray(plt.ginput(1, timeout=-1))
        plt.plot(data_points[:, 0], data_points[:, 1], marker='o', color='blue', linestyle='')
        while listener.running:
            plot.instruction("select points of curve in order they are met")

            try:
                plt.plot(data_points[:, 0], data_points[:, 1], marker='o', color='blue', linestyle='')
                data_points = np.vstack((data_points, np.asarray(plt.ginput(1))))
            except:
                pass

    return data_points
