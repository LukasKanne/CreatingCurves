import matplotlib.pyplot as plt
import src.config as config


def setup_coordinate_system():
    plt.clf()
    fig = plt.subplot(autoscale_on=False)
    plt.axis(config.AXIS)
    return fig


def instruction(string):
    plt.title(string, fontsize=16)
    plt.draw()


def plot_data(points_on_curve, x_line, y_line):
    plt.close()
    plt.clf()
    if not config.AUTO_SCALE:
        plt.axis(config.AXIS)

    plt.plot(points_on_curve[:, 0], points_on_curve[:, 1],
             marker=config.MARKER_STYLE_DATA,
             linestyle='',
             color=config.COLOR_DATA,
             label='data')

    plt.plot(x_line, y_line,
             color=config.COLOR_SPLINE,
             label='spline')

    if config.LEGEND:
        plt.legend()
    if not config.COORDINATE_SYSTEM:
        plt.axis('off')
    plt.show()
