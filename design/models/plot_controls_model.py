from typing import Tuple
import threading

class PlotControlsModel():

    """
    This holds all of the state information of the plot controls
    """

    def __init__(self) -> None:
        self.__time_plot_x_data          = None
        self.__time_plot_y_data          = None
        self.__time_plot_data_lock       = threading.Lock()
        self.__freq_plot_x_data          = None
        self.__freq_plot_y_data          = None
        self.__freq_plot_data_lock       = threading.Lock()
        self.__gen_waveform_button_press = threading.Event()
        self.__clear_plot_button_press   = threading.Event()
        self.__resolution_slider_value   = None
        self.__resolution_slider_lock    = threading.Lock()
        self.__amplitude_slider_value    = None
        self.__amplitude_slider_lock     = threading.Lock()
        self.__height_slider_value       = None
        self.__height_slider_lock        = threading.Lock()
        self.__phase_slider_value        = None
        self.__phase_slider_lock         = threading.Lock()
        self.__frequency_slider_value    = None
        self.__frequency_slider_lock     = threading.Lock()
        self.__angular_label             = None
        self.__angular_label_lock        = threading.Lock()
        self.__period_label              = None
        self.__period_label_lock         = threading.Lock()
        self.__normalize_freq_check      = threading.Event()

    def GetTimePlotData(self) -> Tuple[list, list]:
        """
        Gets the time plot data for the time plot
        """
        with self.__time_plot_data_lock:
            return self.__time_plot_x_data, self.__time_plot_y_data

    def SetTimePlotData(self, x_data: list, y_data: list) -> None:
        """
        Sets the time plot data for the time plot
        """
        with self.__time_plot_data_lock:
            self.__time_plot_x_data = x_data
            self.__time_plot_y_data = y_data

    def GetFreqPlotData(self) -> Tuple[list, list]:
        """
        Gets the frequency plot data for the frequency plot
        """
        with self.__freq_plot_data_lock:
            return self.__freq_plot_x_data, self.__freq_plot_y_data

    def SetFreqPlotData(self, x_data: list, y_data: list) -> None:
        """
        Sets the frequency plot data for the frequency plot
        """
        with self.__freq_plot_data_lock:
            self.__freq_plot_x_data = x_data
            self.__freq_plot_y_data = y_data

    def SetGenWaveformButtonPress(self) -> None:
        """
        Set the generate waveform button pressed event
        """
        self.__gen_waveform_button_press.set()

    def ClearGenWaveformButtonPress(self) -> None:
        """
        Clear the generate waveform button pressed event
        """
        self.__gen_waveform_button_press.clear()

    def IsGenWaveformButtonPressed(self) -> bool:
        """
        Is the generate waveform button pressed
        """
        return self.__gen_waveform_button_press.is_set()

    def SetClearPlotButtonPress(self) -> None:
        """
        Set the clear plot button pressed event
        """
        self.__clear_plot_button_press.set()

    def ClearClearPlotButtonPress(self) -> None:
        """
        Clear the clear plot button pressed event
        """
        self.__clear_plot_button_press.clear()

    def IsClearPlotButtonPressed(self) -> bool:
        """
        Is the clear plot button pressed
        """
        return self.__clear_plot_button_press.is_set()

    def GetResolutionSliderValue(self) -> int:
        """
        Get the resolution slider value
        """
        with self.__resolution_slider_lock:
            return self.__resolution_slider_value
        
    def SetResolutionSliderValue(self, value: int) -> None:
        """
        Set the resolution slider value
        """
        with self.__resolution_slider_lock:
            self.__resolution_slider_value = value

    def GetAmplitudeSliderValue(self) -> float:
        """
        Get the amplitude slider value
        """
        with self.__amplitude_slider_lock:
            return self.__amplitude_slider_value
        
    def SetAmplitudeSliderValue(self, value: float) -> None:
        """
        Set the amplitude slider value
        """
        with self.__amplitude_slider_lock:
            self.__amplitude_slider_value = value

    def GetHeightSliderValue(self) -> float:
        """
        Get the height slider value
        """
        with self.__height_slider_lock:
            return self.__height_slider_value
        
    def SetHeightSliderValue(self, value: float) -> None:
        """
        Set the height slider value
        """
        with self.__height_slider_lock:
            self.__height_slider_value = value

    def GetPhaseSliderValue(self) -> float:
        """
        Get the phase slider value
        """
        with self.__phase_slider_lock:
            return self.__phase_slider_value
        
    def SetPhaseSliderValue(self, value: float) -> None:
        """
        Set the phase slider value
        """
        with self.__phase_slider_lock:
            self.__phase_slider_value = value

    def GetFrequencySliderValue(self) -> float:
        """
        Get the frequency slider value
        """
        with self.__frequency_slider_lock:
            return self.__frequency_slider_value
        
    def SetFrequencySliderValue(self, value: float) -> None:
        """
        Set the frequency slider value
        """
        with self.__frequency_slider_lock:
            self.__frequency_slider_value = value

    def GetAngularLabel(self) -> float:
        """
        Get the angular label
        """
        with self.__angular_label_lock:
            return self.__angular_label
        
    def SetAngularLabel(self, label: float) -> None:
        """
        Set the angular label
        """
        with self.__angular_label_lock:
            self.__angular_label = label

    def GetPeriodLabel(self) -> float:
        """
        Get the period label
        """
        with self.__period_label_lock:
            return self.__period_label
        
    def SetPeriodLabel(self, label: float) -> None:
        """
        Set the period label
        """
        with self.__period_label_lock:
            self.__period_label = label

    def SetNormalizeFreqCheck(self) -> None:
        """
        Set the normalize check event
        """
        self.__normalize_freq_check.set()

    def ClearNormalizeFreqCheck(self) -> None:
        """
        Clear the normalize check event
        """
        self.__normalize_freq_check.clear()

    def IsNormalizeFreqChecked(self) -> bool:
        """
        Is the normalize check checked
        """
        return self.__normalize_freq_check.is_set()