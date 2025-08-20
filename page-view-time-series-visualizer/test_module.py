import unittest
import time_series_visualizer as tsv
import matplotlib as mpl

class DataCleaningTestCase(unittest.TestCase):
    def test_data_cleaning(self):
        self.assertTrue(tsv.df["value"].quantile(0.025) >= tsv.df["value"].min())
        self.assertTrue(tsv.df["value"].quantile(0.975) <= tsv.df["value"].max())


class LinePlotTestCase(unittest.TestCase):
    def test_line_plot(self):
        fig = tsv.draw_line_plot()
        self.assertIsInstance(fig, mpl.figure.Figure)


class BarPlotTestCase(unittest.TestCase):
    def test_bar_plot(self):
        fig = tsv.draw_bar_plot()
        self.assertIsInstance(fig, mpl.figure.Figure)


class BoxPlotTestCase(unittest.TestCase):
    def test_box_plot(self):
        fig = tsv.draw_box_plot()
        self.assertIsInstance(fig, mpl.figure.Figure)


if __name__ == "__main__":
    unittest.main()
