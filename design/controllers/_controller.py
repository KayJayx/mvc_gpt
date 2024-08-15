from __future__ import annotations
from design.views.plot_controls_view import PlotControlsView
from design.models.plot_controls_model import PlotControlsModel
from design.controllers.plot_controls_controller import PlotControlsController

class MainController():

    """
    The responsibility of the Controller is to bridge the gap between the Model and View classes.
    The Controller has lots of responsibilities which we'll list below:
    1. Get data from the View (through user input) and pass it to the Model
    2. Get data from the Model and pass it to the View (for displaying)
    """

    def __init__(self) -> None:

        # Create the model, view and controller here
        self.plot_controls_view       = PlotControlsView()
        self.plot_controls_model      = PlotControlsModel()
        self.plot_controls_controller = PlotControlsController(self.plot_controls_view, self.plot_controls_model)

        # Run the main event handler to also render the GUI elements
        self.plot_controls_view.Run(self.plot_controls_controller.UpdatePlotCallback)