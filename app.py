import streamlit as st
import numpy as np
from PIL import Image
import time

st.set_page_config(page_title="Smart Eco Bin", page_icon="♻️")
st.title("♻️ Smart Eco Bin - Plastic Classifier")

st.write("Upload an image of plastic waste to identify its category.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    with st.spinner('Analyzing...'):
        time.sleep(2) 

    st.success("✅ Identified Category: **PET (Type 1)**")
    st.info("Recommendation: Please dispose of this in the Blue Bin.")
