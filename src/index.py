import src.plot as plot
import src.input as input
import src.data_creation as data_creation
import src.curve_creation as curve_creation
import matplotlib.pyplot as plt



def start():
    data_creation.setup_coordinate_system()
    points_on_curve = data_creation.get_input_points()
    curve_creation.create_curve(points_on_curve)

start()




