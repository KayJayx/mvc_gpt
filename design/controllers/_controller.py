from __future__ import annotations
import design.views._view as _view

class Controller():

    """
    The responsibility of the Controller is to bridge the gap between the Model and View classes.
    The Controller has lots of responsibilities which we'll list below:
    1. Get data from the View (through user input) and pass it to the Model
    2. Get data from the Model and pass it to the View (for displaying)
    """

    def __init__(self) -> None:

        # Create an instance of the View class, the idea is to share the entire view with all of the
        # controller classes such that individual controller subclasses can have the ability to
        # interact with the view
        self.view = _view.View()

        # Create models here

        # Create controllers here

        # Run the designer to actually display the info to the screen
        self.view.designer.Run(self.UpdateWaveform)

    def UpdateWaveform(self) -> None:
        """
        The purpose of this function is to update the waveform plot onto the main window
        """
        pass