from prometheus_client import generate_latest
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page config
st.set_page_config(page_title='AutoVizAi',
                   layout='centered',
                   page_icon='📊')

# Title
st.title('📊  AutoVizAi')

selected_option = st.sidebar.radio("Select an option", ['Visualization', 'Info', 'Sample', 'Stats', 'Missing Values', 'Duplicate Values'])
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Read the selected CSV file
    df = pd.read_csv(uploaded_file)
    
    # Sidebar with multiple options
    if selected_option == 'Visualization':        
        col1, col2 = st.columns(2)

        with col1:
            # Allow the user to select columns for plotting
            x_axis = st.selectbox('Select the X-axis', options=df.columns.tolist()+["None"])
            y_axis = st.selectbox('Select the Y-axis', options=df.columns.tolist()+["None"])

        with col2:
            plot_list = ['Line Plot', 'Bar Chart', 'Scatter Plot', 'Distribution Plot', 'Count Plot']
            # Allow the user to select the type of plot
            plot_type = st.selectbox('Select the type of plot', options=plot_list)

        # Generate the plot based on user selection
        if st.button('Generate Plot'):

            fig, ax = plt.subplots(figsize=(6, 4))

            if plot_type == 'Line Plot':
                sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)
            elif plot_type == 'Bar Chart':
                sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)
            elif plot_type == 'Scatter Plot':
                sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
            elif plot_type == 'Distribution Plot':
                sns.histplot(df[x_axis], kde=True, ax=ax)
                y_axis='Density'
            elif plot_type == 'Count Plot':
                sns.countplot(x=df[x_axis], ax=ax)
                y_axis = 'Count'

            # Adjust label sizes
            ax.tick_params(axis='x', labelsize=10)  # Adjust x-axis label size
            ax.tick_params(axis='y', labelsize=10)  # Adjust y-axis label size

            # Adjust title and axis labels with a smaller font size
            plt.title(f'{plot_type} of {y_axis} vs {x_axis}', fontsize=12)
            plt.xlabel(x_axis, fontsize=10)
            plt.ylabel(y_axis, fontsize=10)

            # Show the results
            st.pyplot(fig)



    # Additional options in the sidebar
    elif selected_option == 'Info':
        # Display dataset information
        st.subheader("Dataset Information")
        st.write(df.info())

    elif selected_option == 'Sample':
        # Display dataset head
        st.subheader("Dataset Head")
        st.write(df.head())

    elif selected_option == 'Stats':
        # Display descriptive statistics
        st.subheader("Descriptive Statistics")
        st.write(df.describe())

    elif selected_option == 'Missing Values':
        # Display missing values
        st.subheader("Missing Values")
        st.write(df.isnull().sum())

    elif selected_option == 'Duplicate Values':
        # Display duplicate values
        st.subheader("Duplicate Values")
        st.write(df[df.duplicated()])


        
