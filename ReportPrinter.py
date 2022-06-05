import pandas as pd

class ReportPrinter:
    def __init__(self, current_file, report_interval, interval):
        self.path = current_file
        self.report_dataframe = self.get_report_dataframe()
        self.rows = (report_interval * 24 * 60 * 60) // interval


    def get_report_dataframe(self):
        report_df = pd.read_csv(self.path, nrows=self.rows)
        return report_df

    def draw_chart(self):
        pass
