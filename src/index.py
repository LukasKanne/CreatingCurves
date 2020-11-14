import src.plot as plot
import src.data_creation as data_creation
import src.curve_creation as curve_creation


def start():
    data_creation.setup_coordinate_system()
    points_on_curve = data_creation.get_input_points()
    x_line, y_line = curve_creation.create_curve(points_on_curve)
    plot.plot_data(points_on_curve, x_line, y_line)


start()
