from views.plot_window_view import PlotWindowView
from models.plot_window_model import PlotWindowModel

class PlotWindowController():

    """
    The responsibility of this class is to act as a bridge between the plot window model and view classes
    """

    def __init__(self, plot_window_view: PlotWindowView, plot_window_model: PlotWindowModel) -> None:
        self.plot_window_view  = plot_window_view
        self.plot_window_model = plot_window_model