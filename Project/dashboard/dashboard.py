import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Dashboard title
st.title('Sensor Health Dashboard')

# File upload
uploaded_file = st.file_uploader("Upload file", type=['csv', 'parquet'])

# Load the PNG image using PIL (Python Imaging Library)
prediction_plot = Image.open('cycle_44.png')

# Adding a caption
st.markdown("<center>Input data and prediction for Cycle 44</center>", unsafe_allow_html=True)

# Display the image in Streamlit
st.image(prediction_plot,use_column_width=True)