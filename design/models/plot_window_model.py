import threading

class PlotWindowModel():

    """
    This holds all of the state information of the plot window
    """

    def __init__(self) -> None:
        self.__time_plot_x_data    = None
        self.__time_plot_y_data    = None
        self.__time_plot_data_lock = threading.Lock()
        self.__freq_plot_x_data    = None
        self.__freq_plot_y_data    = None
        self.__freq_plot_data_lock = threading.Lock()

    def GetTimePlotData(self) -> tuple[list, list]:
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

    def GetFreqPlotData(self) -> tuple[list, list]:
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