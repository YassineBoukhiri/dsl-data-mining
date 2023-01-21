import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from os import environ as env

from dotenv import load_dotenv
load_dotenv()

# Load the pre-trained model
model = load_model("model/model.h5")

# Load the MNIST data

st.set_page_config(page_title="Prediction App",
                   page_icon=":guardsman:", layout="wide")

st.title(env['APP_NAME'])

# Get the image file from the user
image_file = st.file_uploader("Upload an image file", type=["jpg", "png"])

if image_file is not None:
    image = Image.open(image_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess the image
    image = image.resize((28, 28))
    image = image.convert("L")
    image = np.array(image)
    # Reshaping the image according to model
    shape = model.layers[0].input_shape
    if len(shape) == 4:
        image = image.reshape(1,shape[1],shape[2],shape[3])
    elif len(shape) == 2:
        image = image.reshape(1,shape[1])

    # Make a prediction
    prediction = model.predict(image)
    # Show the prediction
    st.success("The predicted digit is: {}".format(np.argmax(prediction)))