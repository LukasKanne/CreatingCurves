import scipy.interpolate
import numpy as np
import src.config as config


def create_curve(point_data):
    x_line, y_line = create_spline(point_data.copy())
    return x_line, y_line


def create_spline(point_data):
    new_data = np.vstack((point_data, np.array([0, 1])))
    tck, u = scipy.interpolate.splprep(new_data.T, u=None, s=0.0, per=1)
    print(tck)
    print(u)
    u_new = np.linspace(u.min(), u.max(),config.INTERVAL_SIZE )
    x_new, y_new = scipy.interpolate.splev(u_new, tck, der=0)
    return x_new, y_new
