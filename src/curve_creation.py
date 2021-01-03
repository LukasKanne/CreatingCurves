import scipy.interpolate
import numpy as np
import src.config as config


def create_curve(point_data):
    x_line, y_line = create_spline(point_data.copy())
    return x_line, y_line


def create_spline(point_data):
    new_data = point_data
    if config.CLOSED_CURVE:
        new_data = np.vstack((point_data, np.array([0,1])))
    spline_object = scipy.interpolate.splprep(new_data.T, u=None, k=config.SPLINE_ORDER,
                                              s=0.0, per= int(config.CLOSED_CURVE))
    tck = spline_object[0]
    u = spline_object[1]
    u_new = np.linspace(u.min(), u.max(), config.INTERVAL_SIZE)
    x_new, y_new = scipy.interpolate.splev(u_new, tck, der=0)
    return x_new, y_new
