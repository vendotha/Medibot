import google.generativeai as genai
import base64

# Set your Gemini API key
genai.configure(api_key="AIzaSyBoo0cTRFKVDJwdy0CXigKvmMtjIKd4oVI")

# Initialize the Gemini 1.5 Flash model
model = genai.GenerativeModel('gemini-1.5-flash')


def encode_image_to_base64(image_path):
    """
    Encode an image to base64 for Gemini API input.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def analyze_yolo_output(annotated_image_path, query):
    """
    Answer user queries based on the image and YOLO output.
    """
    # Encode the annotated image to base64
    image_base64 = encode_image_to_base64(annotated_image_path)

    # Prepare the prompt for Gemini
    prompt = f"""
    You are a highly experienced medical professional. Based on the provided medical image, answer the following query in a confident and professional manner:
    {query}

    Respond as if you are a human doctor, avoiding any disclaimers about being an AI.
    """

    # Send the image and prompt to Gemini
    response = model.generate_content(
        contents=[
            {
                "parts": [
                    {"text": prompt},
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",  # Adjust mime_type if necessary
                            "data": image_base64,
                        }
                    },
                ]
            }
        ]
    )
    return response.text


def answer_general_query(query):
    """
    Answer general medical queries using Gemini API.
    """
    # Prepare the prompt for Gemini
    prompt = f"""
    You are a highly experienced medical professional. Answer the following medical question in a confident and professional manner:
    {query}

    Respond as if you are a human doctor, avoiding any disclaimers about being an AI.
    """

    response = model.generate_content(
        contents=[
            {
                "parts": [
                    {"text": prompt},
                ]
            }
        ]
    )
    return response.text