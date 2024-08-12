import design.views.main_window_view as mwv
import controls as cc

class PlotWindowView():

    """
    This serves as the view class for the plot window
    """

    def __init__(self, main_window_view: mwv.MainWindowView) -> None:
        self.main_window_view = main_window_view

        # Create the controls here
        #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        # Create a window just for the plots
        self.plot_window = cc.ChildWindow(
            width=self.main_window_view.plot_window_width,
            height=self.main_window_view.plot_window_height,
            parent=self.main_window_view.main_window,
            pos=[0, 0],
            no_scrollbar=True
        )

        # Create a time-domain plot and add it to the window
        x_label = "Time"
        y_label = "Amplitude"
        self.time_plot = cc.Plot(
            x_label=x_label, y_label=y_label,
            label=f"{y_label} vs. {x_label}",
            width=self.main_window_view.plot_window_width,
            height=int(self.main_window_view.plot_window_height / 2),
            parent=self.plot_window,
            pos=[0, 0]
        )
        self.time_plot.SwitchThemeComponent(theme_component=self.time_plot.line_theme_component)
        self.time_plot.SetPlotLineColor(color=[36, 183, 199])
        self.time_plot.BindTheme()
        self.time_plot.SetXAxisLimits(0, self.main_window_view.length_of_plot)
        self.time_plot.SetYAxisLimits(-5, 5)

        # Create a frequency-domain plot and add it to the window
        x_label = "Frequency"
        y_label = "Intensity"
        self.freq_plot = cc.Plot(
            x_label=x_label, y_label=y_label,
            label=f"{y_label} vs. {x_label}",
            width=self.main_window_view.plot_window_width,
            height=int(self.main_window_view.plot_window_height / 2),
            parent=self.plot_window,
            pos=[0, self.time_plot.GetPosition()[1] + self.time_plot.GetHeight()]
        )
        self.freq_plot.SwitchThemeComponent(theme_component=self.freq_plot.line_theme_component)
        self.freq_plot.SetPlotLineColor(color=[36, 183, 199])
        self.freq_plot.BindTheme()
        #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-