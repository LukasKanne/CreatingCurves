import numpy as np
import matplotlib.pyplot as plt
import src.keyboard_input as keyboard_input


def setup_coordinate_system():
    plt.clf()
    fig = plt. subplot(autoscale_on=False)
    return fig



def instruction(string):
    print(string)
    plt.title(string, fontsize=16)
    plt.draw()


def get_input_points():

    plt.waitforbuttonpress()
    listener = keyboard_input.start_listener()
    data_points = []
    while listener.running:
        instruction("if you are ready, type r into console")
        data_points = np.asarray(plt.ginput(1, timeout=-1))
        plt.plot(data_points[:, 0], data_points[:, 1], marker='o', color='blue', linestyle='')

        while listener.running:
            instruction("select points of curve in order they are met")

            try:
                plt.plot(data_points[:, 0], data_points[:, 1], marker='o', color='blue', linestyle='')
                data_points = np.vstack((data_points, np.asarray(plt.ginput(1))))
            except:
                pass

    return data_points

