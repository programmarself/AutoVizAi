# AutoVizAi 📊

**AutoVizAi** is a simple, intuitive web application built using Streamlit for quick data visualization and exploration. It allows users to upload CSV files and explore data through customizable visualizations, descriptive statistics, correlation heatmaps, and feature engineering techniques.

## Live Demo

Check out the live version of **AutoVizAi** here: [AutoVizAi Live Demo](https://cyberfantics-autovizai-main-znfbqe.streamlit.app/)

## Features

- 📊 **Data Visualization**: Generate Line Plots, Bar Charts, Scatter Plots, Distribution Plots, and Count Plots with various customization options like color, markers, and gridlines.
- 👀 **Data Sample Viewer**: View the first few rows of the dataset to understand its structure.
- 📊 **Descriptive Statistics**: Automatically compute descriptive statistics like mean, median, standard deviation, etc.
- ❓ **Missing Values Handling**: Identify missing values and clean them by filling with mean or dropping them.
- 🔍 **Duplicate Values Detection**: Find and remove duplicate rows from the dataset.
- 🔗 **Correlation Heatmap**: Visualize correlations between numerical columns using a heatmap.
- 🛠 **Feature Engineering**: Apply transformations like log transformation, binarization, and standardization for better data preprocessing.

## Installation

To run AutoVizAi on your local machine, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/cyberfantics/AutoVizAi.git
    cd AutoVizAi
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    streamlit run app.py
    ```

## Usage

1. **Upload a CSV file**: Use the file uploader to upload your dataset.
2. **Select an option**: Choose an action from the sidebar—whether you want to visualize the data, check for missing or duplicate values, generate statistics, or apply feature engineering.
3. **Customize visualizations**: For plots, select the columns, plot type, and customize colors, gridlines, and markers.
4. **Download plots**: Save any generated plots as PNG images for later use.

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- NumPy

Install all the dependencies with:

```bash
pip install -r requirements.txt
```
