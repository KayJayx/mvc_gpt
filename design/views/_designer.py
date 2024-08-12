import controls as cc
import tkinter as tk
import numpy as np
import threading
import typing
import os

class Designer():

    """
    The responsibility of the Designer is to create the instances of the objects that are to
    be displayed to the user in addition to dictating their placement.
    """

    def __init__(self) -> None:

        # We need the tkinter library in order to get the window
        # screen width and height
        self.root          = tk.Tk()
        self.screen_width  = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight() - 155 if os.name == "posix" else self.root.winfo_screenheight() - 50

        # In order to make successful calls to the Dear PyGUI framework we must 
        # establish a context where we can make calls to that code
        cc.dpg.create_context()

        # Set the theme of the application
        cc.SetGlobalTheme()

        # Add your controls here
        #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        # State variables
        self.generate_waveform = threading.Event()
        self.clear_plots       = threading.Event()
        self.length_of_plot    = 1

        # Create the main window
        self.main_window = cc.Window()
        self.main_window.ChangePadding(window_pad=[0, 0], frame_pad=[0, 0], item_spacing=[0, 0])
        self.main_window.BindTheme()

        # Create a window just for the plots
        self.plot_window_width  = self.screen_width - 600
        self.plot_window_height = self.screen_height if os.name == "posix" else self.screen_height - 40
        self.plot_window        = cc.ChildWindow(
            width=self.plot_window_width,
            height=self.plot_window_height,
            parent=self.main_window,
            pos=[0, 0],
            no_scrollbar=True
        )

        # Create a time-domain plot and add it to the window
        x_label = "Time"
        y_label = "Amplitude"
        self.time_plot = cc.Plot(
            x_label=x_label, y_label=y_label,
            label=f"{y_label} vs. {x_label}",
            width=self.plot_window_width,
            height=int(self.plot_window_height / 2),
            parent=self.plot_window,
            pos=[0, 0]
        )
        self.time_plot.SwitchThemeComponent(theme_component=self.time_plot.line_theme_component)
        self.time_plot.SetPlotLineColor(color=[36, 183, 199])
        self.time_plot.BindTheme()
        self.time_plot.SetXAxisLimits(0, self.length_of_plot)
        self.time_plot.SetYAxisLimits(-5, 5)

        # Create a frequency-domain plot and add it to the window
        x_label = "Frequency"
        y_label = "Intensity"
        self.freq_plot = cc.Plot(
            x_label=x_label, y_label=y_label,
            label=f"{y_label} vs. {x_label}",
            width=self.plot_window_width,
            height=int(self.plot_window_height / 2),
            parent=self.plot_window,
            pos=[0, self.time_plot.GetPosition()[1] + self.time_plot.GetHeight()]
        )
        self.freq_plot.SwitchThemeComponent(theme_component=self.freq_plot.line_theme_component)
        self.freq_plot.SetPlotLineColor(color=[36, 183, 199])
        self.freq_plot.BindTheme()

        # Create a window for the controls
        self.control_window_width  = self.screen_width - self.plot_window_width if os.name == "posix" else self.screen_width - self.plot_window_width - 16
        self.control_window_height = self.plot_window_height
        self.control_window        = cc.ChildWindow(
            width=self.control_window_width,
            height=self.control_window_height,
            parent=self.main_window,
            pos=[self.plot_window_width, 0],
            no_scrollbar=True
        )

        # Create a label to show the controls
        self.group1         = cc.Group(parent=self.control_window, pos=[0, 0])
        self.group1.ChangePadding(window_pad=[0, 0], frame_pad=[10, 10], item_spacing=[0, 0])
        self.group1.BindTheme()
        self.controls_label = cc.Label(label="   Controls", parent=self.group1)
        self.separator      = cc.LineSeparator(parent=self.group1)

        # Create buttons for generating, stoping and clearing the waveform
        self.group2 = cc.Group(parent=self.control_window, pos=[0, 35])
        self.generate_waveform_button = cc.Button(
            label="Generate Waveform",
            width=140, height=30,
            parent=self.group2,
            pos=[20, 50]
        )
        self.clear_plot_button = cc.Button(
            label="Clear Plots",
            width=140, height=30,
            parent=self.group2,
            pos=[self.generate_waveform_button.GetPosition()[0] + self.generate_waveform_button.GetWidth() + 20, self.generate_waveform_button.GetPosition()[1]]
        )

        # Create sliders to change the waveform
        self.group3            = cc.Group(parent=self.control_window, pos=[0, 90])
        self.resolution_slider = cc.Slider(type=int, label="Change Samples", width=140, height=100, parent=self.group3, pos=[20, 90], min_value=1, max_value=2500, default_value=101)
        self.amplitude_slider  = cc.Slider(type=float, label="Change Amplitude", width=140, height=100, parent=self.group3, pos=[20, 110], min_value=1.0, max_value=5.0, default_value=1.0)
        self.height_slider     = cc.Slider(type=float, label="Change Height", width=140, height=100, parent=self.group3, pos=[20, 130], min_value=-5.0, max_value=5.0, default_value=0.0)
        self.phase_slider      = cc.Slider(type=float, label="Change Phase", width=140, height=100, parent=self.group3, pos=[20, 150], min_value=-10.0, max_value=10.0, default_value=0.0)
        self.frequency_slider  = cc.Slider(type=float, label="Change Frequency", width=140, height=100, parent=self.group3, pos=[20, 170], min_value=1.0, max_value=200.0, default_value=1.0)
        self.angular_label     = cc.Label(label=f"Angular Freq: {'{:.3f}'.format(2 * np.pi * self.frequency_slider.GetValue())}", parent=self.group3, pos=[20, 190])
        self.period_label      = cc.Label(label=f"Period: {'{:.3f}'.format(1 / self.frequency_slider.GetValue())}", parent=self.group3, pos=[20, 210])
        self.normalize_freq    = cc.CheckBox(label="Normalize Frequency", parent=self.group3, pos=[20, 230])
        #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
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

    def Run(self, callback: typing.Any = None) -> None:
        """
        Run the main loop for rendering.
        """
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