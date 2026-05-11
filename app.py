
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(page_title="Smart Eco Bin", page_icon="♻️")
st.title("♻️ Smart Eco Bin - Plastic Classifier")
st.write("Upload a plastic item image to identify its recycling category.")


@st.cache_resource
def load_my_model():
    return tf.keras.models.load_model('smart_eco_bin_model.h5')

model = load_my_model()
class_names = ['1-PET', '2-HDPE', '3-PVC', '4-LDPE', '5-PP', '6-PS']


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("🔄 Classifying...")

    img = image.resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

    prediction = model.predict(img_array)
    result = class_names[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    
    st.success(f"✅ Identified Type: **{result}**")
    st.info(f"Confidence: {confidence:.2f}%")