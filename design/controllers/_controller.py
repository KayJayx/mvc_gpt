from __future__ import annotations

class Controller():

    """
    The responsibility of the Controller is to bridge the gap between the Model and View classes.
    The Controller has lots of responsibilities which we'll list below:
    1. Get data from the View (through user input) and pass it to the Model
    2. Get data from the Model and pass it to the View (for displaying)
    """

    def __init__(self) -> None:

        # Create models here

        # Create controllers here

        # Run the designer to actually display the info to the screen
        #self.view.designer.Run(self.UpdateWaveform)
        pass

    def UpdateWaveform(self) -> None:
        """
        The purpose of this function is to update the waveform plot onto the main window
        """
        pass