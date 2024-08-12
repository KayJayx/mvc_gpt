import controls as cc
import tkinter as tk
import typing
import os

class MainWindowView():

    """
    This serves as the view class of the main window which all other controls will be children of
    """

    def __init__(self) -> None:

        # We need the tkinter library in order to get the window
        # screen width and height
        self.root                  = tk.Tk()
        self.screen_width          = self.root.winfo_screenwidth()
        self.screen_height         = self.root.winfo_screenheight() - 155 if os.name == "posix" else self.root.winfo_screenheight() - 50
        self.plot_window_width     = self.screen_width - 600
        self.plot_window_height    = self.screen_height if os.name == "posix" else self.screen_height - 40
        self.control_window_width  = self.screen_width - self.plot_window_width if os.name == "posix" else self.screen_width - self.plot_window_width - 16
        self.control_window_height = self.plot_window_height

        # In order to make successful calls to the Dear PyGUI framework we must 
        # establish a context where we can make calls to that code
        cc.dpg.create_context()

        # Set the theme of the application
        cc.SetGlobalTheme()

        # State variables
        self.length_of_plot = 1

        # Create the main window
        self.main_window = cc.Window()
        self.main_window.ChangePadding(window_pad=[0, 0], frame_pad=[0, 0], item_spacing=[0, 0])
        self.main_window.BindTheme()

    def Run(self, callback: typing.Any = None) -> None:
        """
        Run the main loop for rendering.
        """

        # Set a primary window which will always be drawn in the background
        cc.dpg.set_primary_window(self.main_window.tag, True)

        # This is technically the main window of the application
        # Call the viewport function which actually creates the window through the 
        # operating system followed by some other setup functions
        cc.dpg.create_viewport(
            title="MVC Tutorial",
            x_pos=0, y_pos=0,
            width=self.screen_width,
            height=self.screen_height,
            max_width=self.screen_width,
            max_height=self.screen_height + 155 if os.name == "posix" else self.screen_height,
            min_width=self.screen_width,
            min_height=self.screen_height
        )

        # Setup the viewport
        cc.dpg.setup_dearpygui()

        # Show the main window created by the operating system
        cc.dpg.show_viewport()

        # Main loop
        while cc.dpg.is_dearpygui_running():

            # Call a user defined function here
            if callback is not None:
                callback()

            # Render the GUI frame
            cc.dpg.render_dearpygui_frame()

        # Destroy the DearPyGUI context
        cc.dpg.destroy_context()