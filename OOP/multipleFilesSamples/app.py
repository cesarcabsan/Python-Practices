from AbstractMethods.DataProcessor import DataProcessor
import DataProcessors.Processors as Processors

def process_all(data_processor: DataProcessor, data) -> list:
    return data_processor.process_data(data)

num_processor = Processors.NumericDataProcessor()
text_processor = Processors.TextDataProcessor()

numeric_data = [1,2,3,4,5]
text_data = ["Learning", "Things"]

print(process_all(num_processor, numeric_data))
print(process_all(text_processor, text_data))