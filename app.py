# Importing required libraries
import streamlit as st  # For building the web application
from rembg import remove  # For removing the background from images
from PIL import Image  # For image handling and processing
from io import BytesIO  # For handling byte data in memory
import base64  # For encoding and decoding binary data

# Setting the page configuration
st.set_page_config(layout="wide", page_title="Image Background Remover")  # Sets a wide layout and custom title for the app

# Title and description of the web app
st.write("## Say goodbye to backgrounds!")  # Display the main title of the app
st.write(
    "🐾 Upload an image to see the background disappear. Once you're happy, grab the final version from the sidebar."
)

# Sidebar header
st.sidebar.write("## Upload and download :gear:")  # Sidebar section for uploading and downloading images

# Setting the maximum file size for uploads
MAX_FILE_SIZE = 5 * 1024 * 1024  # Limit the uploaded file size to 5MB

# Function to convert an image into byte format for downloading
def convert_image(img):
    buf = BytesIO()  # Creates an in-memory bytes buffer
    img.save(buf, format="PNG")  # Saves the image in PNG format to the buffer
    byte_im = buf.getvalue()  # Retrieves the byte data of the image
    return byte_im  # Returns the byte representation of the image

# Function to process and display the uploaded image
def fix_image(upload):
    image = Image.open(upload)  # Opens the uploaded image using PIL
    col1.write("Original Image :camera:")  # Writes a label for the original image column
    col1.image(image)  # Displays the original image in the first column

    fixed = remove(image)  # Removes the background from the uploaded image
    col2.write("Fixed Image :wrench:")  # Writes a label for the processed image column
    col2.image(fixed)  # Displays the processed image in the second column
    st.sidebar.markdown("\n")  # Adds spacing in the sidebar

    # Adds a download button in the sidebar to download the processed image
    st.sidebar.download_button(
        "Download fixed image", convert_image(fixed), "fixed.png", "image/png"
    )

# Creating two columns to display original and processed images
col1, col2 = st.columns(2)

# Sidebar file uploader for uploading images
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Checking if a file is uploaded
if my_upload is not None:
    # Validates the file size and processes it if it's within the limit
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")  # Displays an error message for oversized files
    else:
        fix_image(upload=my_upload)  # Processes and displays the uploaded image
else:
    # Processes and displays a default image if no file is uploaded
    fix_image("./elon musk.jpg")
