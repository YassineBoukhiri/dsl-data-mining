import streamlit as st
from PIL import Image
import numpy as np

# Load the pre-trained model

# Load the MNIST data

st.set_page_config(page_title="MNIST Image Prediction",
                   page_icon=":guardsman:", layout="wide")

st.title("MNIST Image Prediction App")

# Get the image file from the user
image_file = st.file_uploader("Upload an image file", type=["jpg", "png"])

if image_file is not None:
    image = Image.open(image_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    image = image.resize((28, 28))
    image = image.convert("L")
    image = np.array(image)
    image = image.reshape(1, 28, 28, 1)

    # Make a prediction
    # Show the prediction
    st.success("The predicted digit is: {}".format(0))
