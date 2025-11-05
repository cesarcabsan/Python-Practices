from AbstractMethods.DataProcessor import DataProcessor
class NumericDataProcessor(DataProcessor):
    def process_data(self, data) -> list:
        return [x * 2 for x in data]

class TextDataProcessor(DataProcessor):
    def process_data(self, data) -> list:
        return [s.upper() for s in data]