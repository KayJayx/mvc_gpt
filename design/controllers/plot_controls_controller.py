from views.plot_controls_view import PlotControlsView
from models.plot_controls_model import PlotControlsModel

class PlotControlsController():

    """
    The responsibility of this class is to act as a bridge between the plot controls model and view classes
    """

    def __init__(self, plot_controls_view: PlotControlsView, plot_controls_model: PlotControlsModel) -> None:
        self.plot_controls_view  = plot_controls_view
        self.plot_controls_model = plot_controls_model