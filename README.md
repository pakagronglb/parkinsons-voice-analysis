# 🧠 Parkinson's Disease Voice Analysis Tool

An interactive web application for analyzing voice measurements in Parkinson's disease patients using Streamlit.

## 📋 Overview

This tool provides an interactive interface for analyzing voice measurements from Parkinson's disease patients. It allows medical professionals and researchers to explore various acoustic features extracted from voice recordings that can help in PD diagnosis.

## 🔍 Features

- **Data Overview**: Quick summary of patient count and measurement statistics
- **Voice Measurements Analysis**: 
  - MDVP (Multiple Dimensional Voice Program) measurements
  - Fundamental frequency analysis
  - Jitter and Shimmer calculations
  - Noise-to-harmonics ratios
- **Interactive Visualizations**:
  - Distribution analysis of voice parameters
  - Correlation analysis between measurements
  - Customizable plots with trend lines
- **Statistical Analysis**: Comprehensive statistical summaries of voice measurements
- **Data Export**: Capability to download processed data for further analysis

## 🎯 Voice Measurements Explained

The application analyzes several key voice parameters:
- **MDVP:Fo(Hz)**: Average vocal fundamental frequency
- **MDVP:Fhi(Hz)**: Maximum vocal fundamental frequency
- **MDVP:Flo(Hz)**: Minimum vocal fundamental frequency
- **MDVP:Jitter(%)**: Variation in fundamental frequency
- **MDVP:Shimmer(%)**: Variation in amplitude
- **NHR**: Noise-to-harmonics ratio
- **HNR**: Harmonics-to-noise ratio

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/pakagronglb/parkinsons-voice-analysis.git
cd parkinsons-voice-analysis
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

### Using the Application

1. Launch the application using the command above
2. Upload your Parkinson's disease voice measurements CSV file
3. Use the sidebar options to customize your analysis
4. Explore different visualizations and statistical summaries
5. Export processed data as needed

## 📊 Sample Data Format

The application expects a CSV file with columns containing voice measurements. The dataset should include various MDVP measurements and other voice parameters as described in the Features section.

## 🛠️ Technologies Used

- **Streamlit**: For the web interface
- **Pandas**: For data manipulation
- **Plotly**: For interactive visualizations
- **Statsmodels**: For statistical analysis

## 🙏 Acknowledgments

This project is inspired by and builds upon the work done in the Parkinson's Disease Detection project by KNOWLEDGE DOCTOR. Special thanks to:

- [KNOWLEDGE DOCTOR's Parkinson's Disease Detection Project](https://github.com/Chando0185/Multiverse_of_100-_data_science_project_series/blob/main/Parkinson's%20Disease%20Detection/Parkinson's%20Disease%20Detection.ipynb) for providing insights into Parkinson's disease voice analysis

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Contact

For any queries or suggestions, please open an issue in the repository.

---
*Note: This tool is for research and educational purposes only and should not be used as the sole basis for medical diagnosis.*