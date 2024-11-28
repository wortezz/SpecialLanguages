from abc import ABC, abstractmethod

class DataVisualizationBuilder(ABC):
    def __init__(self):
        self._data = None
        self._processed_data = None
        self._last_figure = None

    @abstractmethod
    def load_data(self, file_path: str):
        pass

    @abstractmethod
    def explore_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def create_basic_visualization(self):
        pass

    @abstractmethod
    def create_line_chart(self, x_column=None, y_column=None):
        pass

    @abstractmethod
    def create_bar_chart(self, x_column=None, y_column=None):
        pass

    @abstractmethod
    def create_scatter_plot(self, x_column=None, y_column=None):
        pass

    @abstractmethod
    def create_combined_visualization(self):
        pass

    @abstractmethod
    def export_visualization(self, filename: str, format: str):
        pass
