import src.plot as plot


def create_curve(point_data):
    # [x_points, y_points, x_line, y_line] = plot.prepare_data(x_data, y_data)
    point_data, x_line, y_line = plot.create_spline(point_data)
    plot.plot_data(point_data, x_line, y_line)
