from design.views.plot_controls_view import PlotControlsView
from design.models.plot_controls_model import PlotControlsModel
import numpy as np

class PlotControlsController():

    """
    The responsibility of this class is to act as a bridge between the plot controls model and view classes
    """

    def __init__(self, plot_controls_view: PlotControlsView, plot_controls_model: PlotControlsModel) -> None:
        self.plot_controls_view  = plot_controls_view
        self.plot_controls_model = plot_controls_model

        # Set the callbacks for the controls
        self.plot_controls_view.generate_waveform_button.SetCallback(self.GenWaveformButtonCallback)
        self.plot_controls_view.clear_plot_button.SetCallback(self.ClearPlotButtonCallback)
        self.plot_controls_view.resolution_slider.SetCallback(self.ResolutionSliderCallback)
        self.plot_controls_view.amplitude_slider.SetCallback(self.AmplitudeSliderCallback)
        self.plot_controls_view.height_slider.SetCallback(self.HeightSliderCallback)
        self.plot_controls_view.phase_slider.SetCallback(self.PhaseSliderCallback)
        self.plot_controls_view.frequency_slider.SetCallback(self.FrequencySliderCallback)
        self.plot_controls_view.normalize_freq.SetCallback(self.NormalizeFreqCheckboxCallback)

        # Initialize the model values here
        self.plot_controls_model.SetResolutionSliderValue(self.plot_controls_view.resolution_slider.GetValue())
        self.plot_controls_model.SetAmplitudeSliderValue(self.plot_controls_view.amplitude_slider.GetValue())
        self.plot_controls_model.SetHeightSliderValue(self.plot_controls_view.height_slider.GetValue())
        self.plot_controls_model.SetPhaseSliderValue(self.plot_controls_view.phase_slider.GetValue())
        self.plot_controls_model.SetFrequencySliderValue(self.plot_controls_view.frequency_slider.GetValue())
        self.plot_controls_model.SetAngularLabel(2 * np.pi * self.plot_controls_view.frequency_slider.GetValue())
        self.plot_controls_model.SetPeriodLabel(1 / self.plot_controls_view.frequency_slider.GetValue())

    def UpdatePlotCallback(self) -> None:
        """
        Update the plot view and plot model here
        """

        # Clear the plots here
        if self.plot_controls_model.IsClearPlotButtonPressed():

            # Reset the event
            self.plot_controls_model.ClearClearPlotButtonPress()
            self.plot_controls_model.ClearGenWaveformButtonPress()

            # Actually clear the plot here
            self.plot_controls_view.time_plot.PlotLineSeriesData(x_data=[], y_data=[])
            self.plot_controls_model.SetTimePlotData(x_data=[], y_data=[])

        # If the generate waveform is set start populating the plots
        if self.plot_controls_model.IsGenWaveformButtonPressed():

            # Add the algorithm stuff here
            #*****************************************************************
            # DSP Notes
            # Sample Rate        : Rate at which you sample a signal (like the period) (measured in second per samples)
            # Sampling Frequency : The inverse of the sampling rate                    (measured in samples per second)

            samples   = self.plot_controls_model.GetResolutionSliderValue()
            x_data    = np.linspace(0, self.plot_controls_view.length_of_plot, samples, endpoint=True)
            amplitude = self.plot_controls_model.GetAmplitudeSliderValue()
            height    = self.plot_controls_model.GetHeightSliderValue()
            phase     = self.plot_controls_model.GetPhaseSliderValue()
            frequency = self.plot_controls_model.GetFrequencySliderValue()
            if self.plot_controls_model.IsNormalizeFreqChecked():
                y_data = [(amplitude * np.sin(((2 * np.pi * frequency * x) / samples) + phase)) + height for x in x_data]
            else:
                # Digital representation of what would be an analog signal, where samples represents the
                # total number of inputs into my function
                y_data = [(amplitude * np.sin(((2 * np.pi * frequency * x)) + phase)) + height for x in x_data]
            #*****************************************************************

            # Actually update the plot here
            self.plot_controls_view.time_plot.PlotLineSeriesData(x_data=x_data, y_data=y_data)
            self.plot_controls_model.SetTimePlotData(x_data=x_data, y_data=y_data)

            # Update the labels with new data
            angular_freq = 2 * np.pi * frequency
            period       = 1 / frequency
            self.plot_controls_view.angular_label.SetValue(f"Angular Freq: {'{:.3f}'.format(angular_freq)}")
            self.plot_controls_model.SetAngularLabel(angular_freq)
            self.plot_controls_view.period_label.SetValue(f"Period: {'{:.3f}'.format(period)}")
            self.plot_controls_model.SetPeriodLabel(period)

    def GenWaveformButtonCallback(self) -> None:
        """
        Set the generate waveform button event in the model class
        """
        if not self.plot_controls_model.IsGenWaveformButtonPressed():
            self.plot_controls_model.SetGenWaveformButtonPress()

    def ClearPlotButtonCallback(self) -> None:
        """
        Set the generate waveform button event in the model class
        """
        if not self.plot_controls_model.IsClearPlotButtonPressed():
            self.plot_controls_model.SetClearPlotButtonPress()

    def ResolutionSliderCallback(self) -> None:
        """
        Get the resolution slider value from the view class and store it in the model class
        """
        self.plot_controls_model.SetResolutionSliderValue(self.plot_controls_view.resolution_slider.GetValue())

    def AmplitudeSliderCallback(self) -> None:
        """
        Get the amplitude slider value from the view class and store it in the model class
        """
        self.plot_controls_model.SetAmplitudeSliderValue(self.plot_controls_view.amplitude_slider.GetValue())

    def HeightSliderCallback(self) -> None:
        """
        Get the height slider value from the view class and store it in the model class
        """
        self.plot_controls_model.SetHeightSliderValue(self.plot_controls_view.height_slider.GetValue())

    def PhaseSliderCallback(self) -> None:
        """
        Get the phase slider value from the view class and store it in the model class
        """
        self.plot_controls_model.SetPhaseSliderValue(self.plot_controls_view.phase_slider.GetValue())

    def FrequencySliderCallback(self) -> None:
        """
        Get the frequency slider value from the view class and store it in the model class
        """
        self.plot_controls_model.SetFrequencySliderValue(self.plot_controls_view.frequency_slider.GetValue())

    def FrequencySliderCallback(self) -> None:
        """
        Get the frequency slider value from the view class and store it in the model class
        """
        self.plot_controls_model.SetFrequencySliderValue(self.plot_controls_view.frequency_slider.GetValue())

    def NormalizeFreqCheckboxCallback(self) -> None:
        """
        Set the normalize frequency checkbox event in the model class
        """
        if not self.plot_controls_model.IsNormalizeFreqChecked():
            self.plot_controls_model.SetNormalizeFreqCheck()
        else:
            self.plot_controls_model.ClearNormalizeFreqCheck()