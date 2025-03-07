import streamlit as st
from PIL import Image
import cv2
import os
from utils.disease_detection import detect_disease
from utils.chatbot import analyze_yolo_output, answer_general_query

# Set page title and favicon
st.set_page_config(
    page_title="MedBot - AI-Powered Medical Diagnosis",
    page_icon="🩺",
    layout="wide"
)

# Add custom CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Add a header with a logo and description
st.image("logo.jpeg", width=150)  # Add a logo image file
st.title("MedBot - AI-Powered Medical Diagnosis")
st.write("""
Welcome to MedBot, your AI-powered medical assistant. Upload a medical image (X-ray, CT scan, or eye image) to get a diagnosis and medical advice.
""")

# Sidebar for chatbot interaction
with st.sidebar:
    st.title("Chatbot")
    st.write("Ask a medical question or upload an image for diagnosis.")
    user_input = st.text_input("Enter your question or upload an image:")

# Image upload section
uploaded_file = st.file_uploader("Upload a medical image", type=["jpg", "png", "jpeg"])

# Initialize session state to store annotated image path
if "annotated_image_path" not in st.session_state:
    st.session_state.annotated_image_path = None

if uploaded_file is not None:
    # Save the uploaded file
    image_path = f"temp_{uploaded_file.name}"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display the uploaded image
    st.subheader("Uploaded Image")
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Detect disease using YOLO
    annotated_image, detection_results = detect_disease(image_path)
    st.subheader("Annotated Image")
    st.image(annotated_image, caption="Annotated Image", use_column_width=True)

    # Save the annotated image
    annotated_image_path = f"annotated_{uploaded_file.name}"
    cv2.imwrite(annotated_image_path, annotated_image)
    st.session_state.annotated_image_path = annotated_image_path

    if detection_results:
        # Display Gemini analysis on the right side
        with st.expander("Gemini Analysis"):
            insights = analyze_yolo_output(annotated_image_path, "Explain the detected condition.")
            st.write(insights)
    else:
        st.write("No disease detected in the image.")

    # Remove the temporary uploaded file
    os.remove(image_path)

# Chatbot interaction
if user_input:
    if "upload" in user_input.lower():
        st.sidebar.write("Please upload an image using the file uploader above.")
    else:
        if st.session_state.annotated_image_path:
            # If an annotated image is available, use analyze_yolo_output to answer the query
            response = analyze_yolo_output(st.session_state.annotated_image_path, user_input)
        else:
            # If no image is uploaded, use answer_general_query for general medical questions
            response = answer_general_query(user_input)
        st.sidebar.write("Chatbot Response:", response)