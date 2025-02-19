import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="Parkinson's Disease Data Explorer",
    page_icon="🧠",
    layout="wide"
)

# Title and introduction
st.title("🧠 Parkinson's Disease Data Explorer")
st.markdown("""
This tool helps analyze Parkinson's disease data through various biomedical voice measurements. 
The dataset contains various acoustic features extracted from voice recordings that can help in PD diagnosis.

Key features you can explore:
- Voice frequency measurements
- Amplitude variations
- Voice perturbation metrics
- Harmonic-to-noise ratios
""")

# Sidebar for file upload and options
with st.sidebar:
    st.header("📁 Data Upload")
    uploaded_file = st.file_uploader(
        "Upload Parkinson's dataset (CSV)",
        type="csv",
        help="Upload a CSV file containing voice measurements"
    )
    
    if uploaded_file is not None:
        st.success("Dataset successfully loaded!")
        
        st.header("⚙️ Analysis Options")
        show_preview = st.checkbox("Show Data Overview", value=True)
        show_stats = st.checkbox("Show Voice Measurements Statistics", value=True)
        show_viz = st.checkbox("Show Voice Analysis Visualizations", value=True)

        st.markdown("""
        ### 📋 Feature Information
        - **MDVP:Fo(Hz)**: Average vocal fundamental frequency
        - **MDVP:Fhi(Hz)**: Maximum vocal fundamental frequency
        - **MDVP:Flo(Hz)**: Minimum vocal fundamental frequency
        - **MDVP:Jitter(%)**: Variation in fundamental frequency
        - **MDVP:Shimmer(%)**: Variation in amplitude
        - **NHR**: Noise-to-harmonics ratio
        - **HNR**: Harmonics-to-noise ratio
        """)

# Main content
if uploaded_file is not None:
    # Load the data
    df = pd.read_csv(uploaded_file)
    
    # Dataset Overview
    st.header("🔍 Patient Data Overview")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Patients", df.shape[0])
    with col2:
        st.metric("Voice Measurements", df.shape[1])
    with col3:
        st.metric("Missing Values", df.isna().sum().sum())

    # Data preview
    if show_preview:
        st.header("📊 Voice Measurements Preview")
        st.markdown("Sample of voice measurements from the dataset:")
        st.dataframe(df.head(), use_container_width=True)

        st.header("📋 Measurement Details")
        st.markdown("Summary of voice measurement parameters:")
        col_info = pd.DataFrame({
            'Measurement Type': df.dtypes,
            'Valid Readings': df.count(),
            'Missing Readings': df.isna().sum(),
            'Unique Values': df.nunique()
        })
        st.dataframe(col_info, use_container_width=True)

    # Basic statistics
    if show_stats:
        st.header("📊 Statistical Analysis")
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        if len(numeric_cols) > 0:
            st.markdown("Statistical summary of voice measurements:")
            st.dataframe(df[numeric_cols].describe(), use_container_width=True)

    # Visualizations
    if show_viz and len(numeric_cols) > 0:
        st.header("📈 Voice Measurement Analysis")
        
        # Distribution Analysis
        st.subheader("Voice Parameter Distribution")
        col1, col2 = st.columns([2, 1])
        with col1:
            col_to_plot = st.selectbox(
                "Select voice parameter to analyze:",
                numeric_cols,
                help="Choose a voice measurement to view its distribution"
            )
        with col2:
            bin_count = st.slider("Distribution detail level:", min_value=5, max_value=100, value=30)
        
        fig = px.histogram(df, x=col_to_plot, nbins=bin_count)
        st.plotly_chart(fig, use_container_width=True)

        # Correlation Analysis
        st.subheader("Parameter Correlation Analysis")
        st.markdown("Explore relationships between different voice measurements:")
        col1, col2 = st.columns(2)
        with col1:
            x_axis = st.selectbox("Select first parameter:", numeric_cols)
        with col2:
            y_axis = st.selectbox("Select second parameter:", numeric_cols, index=min(1, len(numeric_cols)-1))
        
        fig = px.scatter(df, x=x_axis, y=y_axis, trendline="ols")
        st.plotly_chart(fig, use_container_width=True)

    # Download section
    st.header("💾 Export Analysis Data")
    st.markdown("Download the processed voice measurements data:")
    st.download_button(
        label="Download Analysis Data",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='parkinsons_analysis.csv',
        mime='text/csv',
    )

else:
    st.info("👈 Please upload the Parkinson's disease dataset (CSV) using the sidebar to begin analysis") 