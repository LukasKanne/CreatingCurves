import matplotlib.pyplot as plt
import scipy.interpolate
import numpy as np

import src.config as config


def prepare_data(x_data, y_data):
    prepare_data = [x_data, y_data]
    spline = scipy.interpolate.make_interp_spline(x_data, y_data, k=config.SPLINE_DEGREE)
    x_line = np.linspace(min(x_data), max(x_data), config.INTERVAL_SIZE)
    prepare_data.append(x_line)
    prepare_data.append(spline(x_line))
    return prepare_data


def create_spline(point_data):
    tck, u = scipy.interpolate.splprep(point_data.T, s=0.0, per=1)
    u_new = np.linspace(u.min(), u.max(), 1000)
    x_new, y_new = scipy.interpolate.splev(u_new, tck, der=0)
    return point_data, x_new, y_new


def plot_data(point_data, x_line, y_line):
    fig, ax = plt.subplots()
    ax.plot(point_data.T[0, :], point_data.T[1, :], marker='o', linestyle='', color='red', label='data')
    ax.plot(x_line, y_line, color='blue', label='spline')
    ax.legend()
    plt.show()
