from lab8.Builders.csv_builder import CSVDataVisualizationBuilder

class Director:
    def __init__(self):
        self.builder = CSVDataVisualizationBuilder()

    def load_data(self, file_path: str):
        self.builder.load_data(file_path)

    def explore_data(self):
        self.builder.explore_data()

    def process_data(self):
        self.builder.process_data()

    def create_basic_visualization(self):
        self.builder.create_basic_visualization()

    def create_line_chart(self, x_column=None, y_column=None):
        self.builder.create_line_chart(x_column, y_column)

    def create_bar_chart(self, x_column=None, y_column=None):
        self.builder.create_bar_chart(x_column, y_column)

    def create_scatter_plot(self, x_column=None, y_column=None):
        self.builder.create_scatter_plot(x_column, y_column)

    def create_combined_visualization(self):
        self.builder.create_combined_visualization()

    def export_visualization(self, filename: str, format: str):
        self.builder.export_visualization(filename, format)
