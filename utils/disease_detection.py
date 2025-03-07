from ultralytics import YOLO
import cv2

# Load pre-trained YOLO models
eye_disease_model = YOLO("models/eyeDisease.pt")
lung_cancer_model = YOLO("models/liverDisease.pt")
fracture_model = YOLO("models/fracture.pt")

def classify_image_type(image):
    """
    Classify the type of medical image (eye, lung, bone).
    This is a placeholder function. You can implement a proper classifier if needed.
    """
    # For simplicity, assume the image type is provided by the user or inferred from metadata.
    return "eye"  # Replace with actual logic

def detect_disease(image_path):
    """
    Detect diseases in the uploaded image using YOLO models.
    """
    # Load image
    image = cv2.imread(image_path)
    image_type = classify_image_type(image)

    # Run YOLO model inference
    if image_type == "eye":
        results = eye_disease_model(image)
    elif image_type == "lung":
        results = lung_cancer_model(image)
    elif image_type == "bone":
        results = fracture_model(image)
    else:
        raise ValueError("Unsupported image type")

    # Plot results on the image
    annotated_image = results[0].plot()
    return annotated_image, results[0].boxes.data.tolist()