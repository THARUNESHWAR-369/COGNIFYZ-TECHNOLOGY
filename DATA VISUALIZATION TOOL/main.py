"""
Data Visualization Tool

This module defines a DataVisualizer class that provides methods for creating various types of plots and graphs
using Matplotlib, Seaborn, and Plotly for a given dataset in CSV format.

The class can be used to visualize data from a CSV file by creating different types of plots such as line plots,
scatter plots, bar charts, histograms, box plots, heatmaps, pie charts, violin plots, and interactive plots
using Plotly.

Usage:
    1. Create an instance of DataVisualizer with the path to the dataset in CSV format.
    2. Call the desired plotting methods to generate plots based on the dataset.

Example:
    dataset_path = 'sample_dataset.csv'  # Replace with your dataset file path
    visualizer = DataVisualizer(dataset_path)
    visualizer.plot_line('X', 'Y')
    visualizer.plot_scatter('X', 'Y')
    # ... other plotting methods ...

Author: Tharuneshwar
Date: September 2023
"""

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

class DataVisualizer:
    """
    DataVisualizer class provides methods to create various types of plots and graphs
    for a given dataset using Matplotlib, Seaborn, and Plotly.
    """
    def __init__(self, dataset_path):
        """
        Initializes a DataVisualizer instance with the dataset located at the specified path.

        Args:
            dataset_path (str): The file path to the dataset in CSV format.
        """
        self.df = pd.read_csv(dataset_path)

    def plot_line(self, x_column, y_column):
        """
        Create a line plot using Matplotlib.

        Args:
            x_column (str): The column name for the x-axis.
            y_column (str): The column name for the y-axis.
        """
        plt.figure(figsize=(8, 6))
        plt.plot(self.df[x_column], self.df[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title('Line Plot')
        plt.show()

    def plot_scatter(self, x_column, y_column):
        """
        Create a scatter plot using Matplotlib.

        Args:
            x_column (str): The column name for the x-axis.
            y_column (str): The column name for the y-axis.
        """
        plt.figure(figsize=(8, 6))
        plt.scatter(self.df[x_column], self.df[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title('Scatter Plot')
        plt.show()

    def plot_bar(self, x_column, y_column):
        """
        Create a bar chart using Matplotlib.

        Args:
            x_column (str): The column name for the x-axis.
            y_column (str): The column name for the y-axis.
        """
        plt.figure(figsize=(8, 6))
        plt.bar(self.df[x_column], self.df[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title('Bar Chart')
        plt.xticks(rotation=45)
        plt.show()

    def plot_histogram(self, column):
        """
        Create a histogram using Matplotlib.

        Args:
            column (str): The column name for which to create the histogram.
        """
        plt.figure(figsize=(8, 6))
        plt.hist(self.df[column], bins=20, edgecolor='black')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.title('Histogram')
        plt.show()

    def plot_box(self, x_column, y_column):
        """
        Create a box plot using Seaborn.

        Args:
            x_column (str): The column name for the x-axis.
            y_column (str): The column name for the y-axis.
        """
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=x_column, y=y_column, data=self.df)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title('Box Plot')
        plt.xticks(rotation=45)
        plt.show()

    def plot_heatmap(self):
        """
        Create a heatmap using Seaborn to visualize correlation between numeric columns.
        """
        plt.figure(figsize=(8, 6))
        numeric_columns = self.df.select_dtypes(include=['int64', 'float64'])
        corr_matrix = numeric_columns.corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
        plt.title('Heatmap')
        plt.show()

    def plot_pie(self, column):
        """
        Create a pie chart using Matplotlib to visualize categorical data.

        Args:
            column (str): The column name for which to create the pie chart.
        """
        plt.figure(figsize=(8, 6))
        plt.pie(self.df[column].value_counts(), labels=self.df[column].unique(), autopct='%1.1f%%', startangle=90)
        plt.title('Pie Chart')
        plt.axis('equal')
        plt.show()

    def plot_violin(self, x_column, y_column):
        """
        Create a violin plot using Seaborn.

        Args:
            x_column (str): The column name for the x-axis.
            y_column (str): The column name for the y-axis.
        """
        plt.figure(figsize=(8, 6))
        sns.violinplot(x=x_column, y=y_column, data=self.df)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title('Violin Plot')
        plt.xticks(rotation=45)
        plt.show()

    def plot_line_plotly(self, x_column, y_column):
        """
        Create an interactive line plot using Plotly.

        Args:
            x_column (str): The column name for the x-axis.
            y_column (str): The column name for the y-axis.
        """
        fig = px.line(self.df, x=x_column, y=y_column, title='Line Plot (Plotly)')
        fig.show()

    def plot_scatter_plotly(self, x_column, y_column):
        """
        Create an interactive scatter plot using Plotly.

        Args:
            x_column (str): The column name for the x-axis.
            y_column (str): The column name for the y-axis.
        """
        fig = px.scatter(self.df, x=x_column, y=y_column, title='Scatter Plot (Plotly)')
        fig.show()

# Usage example:
if __name__ == "__main__":
    dataset_path = 'dataset.csv'  # Replace with your dataset file path
    visualizer = DataVisualizer(dataset_path)

    visualizer.plot_line('Age', 'Income')
    visualizer.plot_scatter('Age', 'Income')
    visualizer.plot_bar('Gender', 'Income')
    visualizer.plot_histogram('Age')
    visualizer.plot_box('Education', 'Income')
    visualizer.plot_heatmap()
    visualizer.plot_pie('Gender')
    visualizer.plot_violin('Education', 'Income')
    visualizer.plot_line_plotly('Age', 'Income')
    visualizer.plot_scatter_plotly('Age', 'Income')
