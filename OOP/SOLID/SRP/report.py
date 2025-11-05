class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        # Logic to generate report
        return f"Report Data: {self.data}"

class ReportPrinter:
    def print_report(self, report):
        print(report)

class ReportSaver:
    def save_report(self, report, filename):
        with open(filename, 'w') as file:
            file.write(report)

# Usage
report_generator = ReportGenerator("Sales Data")
generated_report = report_generator.generate_report()

report_printer = ReportPrinter()
report_printer.print_report(generated_report)

report_saver = ReportSaver()
report_saver.save_report(generated_report, 'reporttest.txt')