from __future__ import annotations
from design.views._designer import Designer

class View():

    """
    The responsibility of the View is to get user input and display data to the user.
    The View is also tightly coupled with the designer class, as it holds the actual
    objects which are displayed to the user.
    """

    def __init__(self) -> None:
        super().__init__()
        self.designer = Designer()

        # Create views here