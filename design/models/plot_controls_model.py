import threading

class PlotControlsModel():

    """
    This holds all of the state information of the plot controls
    """

    def __init__(self) -> None:
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

    def GetResolutionSliderValue(self) -> str:
        """
        Get the resolution slider value
        """
        with self.__resolution_slider_lock:
            return self.__resolution_slider_value
        
    def SetResolutionSliderValue(self, value: str) -> None:
        """
        Set the resolution slider value
        """
        with self.__resolution_slider_lock:
            self.__resolution_slider_value = value

    def GetAmplitudeSliderValue(self) -> str:
        """
        Get the amplitude slider value
        """
        with self.__amplitude_slider_lock:
            return self.__amplitude_slider_value
        
    def SetAmplitudeSliderValue(self, value: str) -> None:
        """
        Set the amplitude slider value
        """
        with self.__amplitude_slider_lock:
            self.__amplitude_slider_value = value

    def GetHeightSliderValue(self) -> str:
        """
        Get the height slider value
        """
        with self.__height_slider_lock:
            return self.__height_slider_value
        
    def SetHeightSliderValue(self, value: str) -> None:
        """
        Set the height slider value
        """
        with self.__height_slider_lock:
            self.__height_slider_value = value

    def GetPhaseSliderValue(self) -> str:
        """
        Get the phase slider value
        """
        with self.__phase_slider_lock:
            return self.__phase_slider_value
        
    def SetPhaseSliderValue(self, value: str) -> None:
        """
        Set the phase slider value
        """
        with self.__phase_slider_lock:
            self.__phase_slider_value = value

    def GetFrequencySliderValue(self) -> str:
        """
        Get the frequency slider value
        """
        with self.__frequency_slider_lock:
            return self.__frequency_slider_value
        
    def SetFrequencySliderValue(self, value: str) -> None:
        """
        Set the frequency slider value
        """
        with self.__frequency_slider_lock:
            self.__frequency_slider_value = value

    def GetAngularLabel(self) -> str:
        """
        Get the angular label
        """
        with self.__angular_label_lock:
            return self.__angular_label
        
    def SetAngularLabel(self, label: str) -> None:
        """
        Set the angular label
        """
        with self.__angular_label_lock:
            self.__angular_label = label

    def GetPeriodLabel(self) -> str:
        """
        Get the period label
        """
        with self.__period_label_lock:
            return self.__period_label
        
    def SetPeriodLabel(self, label: str) -> None:
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