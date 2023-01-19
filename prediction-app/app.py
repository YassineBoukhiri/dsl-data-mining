import streamlit as st
from PIL import Image
import numpy as np
import tensorflow.keras as keras
from tensorflow.keras.models import load_model


# Load the pre-trained model
model = load_model("mnist-model.h5")

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
    prediction = model.predict(image)
    # Show the prediction
    st.success("The predicted digit is: {}".format(np.argmax(prediction)))
