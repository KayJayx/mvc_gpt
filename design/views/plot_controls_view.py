import design.views.main_window_view as mwv
import controls as cc
import numpy as np
import threading

class PlotControlsView():

    """
    This serves as the view class for the plot controls panel
    """

    def __init__(self, main_window_view: mwv.MainWindowView) -> None:
        self.main_window_view = main_window_view

        # Create the controls here
        #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        # Create a window for the controls
        self.control_window        = cc.ChildWindow(
            width=self.main_window_view.control_window_width,
            height=self.main_window_view.control_window_height,
            parent=self.main_window_view.main_window,
            pos=[self.main_window_view.plot_window_width, 0],
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
        #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-