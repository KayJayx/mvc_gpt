from __future__ import annotations
from views.main_window_view import MainWindowView
from views.plot_window_view import PlotWindowView
from views.plot_controls_view import PlotControlsView
from models.plot_window_model import PlotWindowModel
from models.plot_controls_model import PlotControlsModel
from controllers.plot_window_controller import PlotWindowController
from controllers.plot_controls_controller import PlotControlsController

class MainController():

    """
    The responsibility of the Controller is to bridge the gap between the Model and View classes.
    The Controller has lots of responsibilities which we'll list below:
    1. Get data from the View (through user input) and pass it to the Model
    2. Get data from the Model and pass it to the View (for displaying)
    """

    def __init__(self) -> None:

        # Create views here
        self.main_window_view   = MainWindowView()
        self.plot_window_view   = PlotWindowView(self.main_window_view)
        self.plot_controls_view = PlotControlsView(self.main_window_view)

        # Create models here
        self.plot_window_model   = PlotWindowModel()
        self.plot_controls_model = PlotControlsModel()

        # Create controllers here
        self.plot_window_controller   = PlotWindowController(self.plot_window_view, self.plot_window_model)
        self.plot_controls_controller = PlotControlsController(self.plot_controls_view, self.plot_controls_model)

        # Run the main event handler to also render the GUI elements
        self.main_window_view.Run()