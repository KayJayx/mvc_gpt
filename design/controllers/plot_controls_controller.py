from views.plot_controls_view import PlotControlsView
from models.plot_controls_model import PlotControlsModel

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