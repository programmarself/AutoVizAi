import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the page config
st.set_page_config(page_title='AutoVizAi',
                   layout='centered',
                   page_icon='📊')

# Title
st.title('📊  AutoVizAi')

# Sidebar options
selected_option = st.sidebar.radio("Select an option", 
                                   ['Visualization', 'Info', 'Sample', 'Stats', 'Missing Values', 'Duplicate Values', 'Correlation Heatmap', 'Pair Plot', 'Feature Engineering'])

# File uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Read the selected CSV file
    df = pd.read_csv(uploaded_file)
    
    # Sidebar with multiple options
    if selected_option == 'Visualization':
        st.subheader("🔍 Data Visualization")
        col1, col2 = st.columns(2)

        with col1:
            # Allow the user to select columns for plotting
            x_axis = st.selectbox('Select the X-axis', options=["None"] + df.columns.tolist())
            y_axis = st.selectbox('Select the Y-axis', options=["None"] + df.columns.tolist())

        with col2:
            plot_list = ['Line Plot', 'Bar Chart', 'Scatter Plot', 'Distribution Plot', 'Count Plot']
            # Allow the user to select the type of plot
            plot_type = st.selectbox('Select the type of plot', options=plot_list)

        # Customization options for the plot
        st.write("📊 **Customize Your Plot**")
        palette = st.color_picker("Choose a plot color")
        fig_size = st.slider("Figure Size (Width, Height)", min_value=4, max_value=12, value=(6, 4))

        # Generate the plot based on user selection
        if st.button('Generate Plot'):

            fig, ax = plt.subplots(figsize=fig_size)

            if plot_type == 'Line Plot':
                sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax, color=palette)
            elif plot_type == 'Bar Chart':
                sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax, color=palette)
            elif plot_type == 'Scatter Plot':
                sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax, color=palette)
            elif plot_type == 'Distribution Plot':
                sns.histplot(df[x_axis], kde=True, ax=ax, color=palette)
                y_axis = 'Density'
            elif plot_type == 'Count Plot':
                sns.countplot(x=df[x_axis], ax=ax, color=palette)
                y_axis = 'Count'

            # Adjust labels and title
            plt.title(f'{plot_type} of {y_axis} vs {x_axis}', fontsize=14)
            plt.xlabel(x_axis, fontsize=12)
            plt.ylabel(y_axis, fontsize=12)

            # Show the results
            st.pyplot(fig)

            # Option to download the plot
            if st.button("Download Plot as PNG"):
                fig.savefig('plot.png')
                st.write("Plot saved as plot.png!")

    elif selected_option == 'Info':
        # Display dataset information
        st.subheader("📄 Dataset Information")
        buffer = df.info(buf=None)
        st.text(buffer)

    elif selected_option == 'Sample':
        # Display dataset head
        st.subheader("👀 Dataset Sample")
        st.write(df.head())

    elif selected_option == 'Stats':
        # Display descriptive statistics
        st.subheader("📊 Descriptive Statistics")
        st.write(df.describe())

    elif selected_option == 'Missing Values':
        # Display missing values and offer options to clean them
        st.subheader("❓ Missing Values")
        missing_values = df.isnull().sum()
        st.write(missing_values)
        
        if missing_values.any():
            if st.button("Fill Missing Values with Mean"):
                df.fillna(df.mean(), inplace=True)
                st.write("Missing values filled with mean.")
            if st.button("Drop Missing Values"):
                df.dropna(inplace=True)
                st.write("Missing values dropped.")

    elif selected_option == 'Duplicate Values':
        # Display duplicate values and allow the user to remove them
        st.subheader("🔍 Duplicate Values")
        duplicate_rows = df[df.duplicated()]
        st.write(duplicate_rows)
        
        if st.button("Drop Duplicate Values"):
            df.drop_duplicates(inplace=True)
            st.write("Duplicate rows dropped.")

    elif selected_option == 'Correlation Heatmap':
        # Correlation heatmap for numerical features
        st.subheader("🔗 Correlation Heatmap")
        corr = df.corr()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    elif selected_option == 'Pair Plot':
        # Pairplot to visualize relationships between numerical features
        st.subheader("📊 Pair Plot")
        st.write("A pair plot visualizes relationships between multiple variables.")
        columns = st.multiselect("Select Columns for Pair Plot", options=df.columns.tolist(), default=df.select_dtypes(include=np.number).columns.tolist())
        
        if st.button("Generate Pair Plot"):
            sns.pairplot(df[columns], diag_kind='kde', palette='coolwarm')
            st.pyplot()

    elif selected_option == 'Feature Engineering':
        # Feature engineering options
        st.subheader("🛠️ Feature Engineering")
        st.write("Transform features for better modeling:")
        feature_option = st.radio("Select Feature Engineering Option", ['Log Transformation', 'Binarization', 'Standardization'])
        
        if feature_option == 'Log Transformation':
            log_col = st.selectbox("Select Column for Log Transformation", options=df.columns)
            df[log_col + '_log'] = np.log(df[log_col] + 1)
            st.write(f"Log transformation applied to {log_col}.")
            st.write(df.head())
        
        elif feature_option == 'Binarization':
            bin_col = st.selectbox("Select Column for Binarization", options=df.columns)
            threshold = st.slider("Select Threshold", min_value=float(df[bin_col].min()), max_value=float(df[bin_col].max()))
            df[bin_col + '_bin'] = (df[bin_col] > threshold).astype(int)
            st.write(f"Binarization applied to {bin_col} with threshold {threshold}.")
            st.write(df.head())
        
        elif feature_option == 'Standardization':
            std_col = st.selectbox("Select Column for Standardization", options=df.columns)
            df[std_col + '_std'] = (df[std_col] - df[std_col].mean()) / df[std_col].std()
            st.write(f"Standardization applied to {std_col}.")
            st.write(df.head())
