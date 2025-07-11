# 🩺 MedBot - AI-Powered Medical Diagnosis Chatbot

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.12.0-orange)
![Gemini API](https://img.shields.io/badge/Gemini-API-green)
![YOLO](https://img.shields.io/badge/YOLO-Ultralytics-red)

Welcome to **MedBot**, an AI-powered medical diagnosis chatbot that uses **YOLO-based disease detection** and **Gemini API** for medical insights. This project is designed to provide users with AI-assisted medical diagnosis and advice through an interactive and user-friendly web interface.

---

## 🌟 Features

- **CNN-Based Disease Detection**:
  - Uses YOLO models for real-time detection of medical conditions (e.g., eye diseases, lung cancer, fractures).
  - Supports multiple disease models and accepts X-rays, CT scans, MRI scans, or eye images.

- **Multi-Model AI Chatbot**:
  - Integrates multiple CNN models to create a multi-specialist AI chatbot.
  - Automatically detects which model to use based on the uploaded image.

- **Interactive Web UI**:
  - Built with **Streamlit** for a smooth and accessible user experience.
  - Allows users to upload medical images, receive detection results, and interact with the chatbot.

- **Gemini-Powered Medical Insights**:
  - Utilizes the **Gemini API** to provide contextual medical insights.
  - Explains possible causes, basic medical advice, and when to seek professional consultation.

- **Multimodal AI Chatbot**:
  - Accepts both text and image inputs.
  - Answers general medical queries even without image uploads.

- **User-Friendly Interaction**:
  - Provides multilingual support and text-to-speech (TTS) options for better engagement.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Streamlit
- Ultralytics (for YOLO models)
- Gemini API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vendotha/Medical_Diagnosis_Chatbot.git
   cd Medical_Diagnosis_Chatbot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Gemini API key:
   - Replace `"your_gemini_api_key"` in `utils/chatbot.py` with your actual API key.

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to `http://localhost:8501`.
---

🌐 Live Demo
Try MedBot now: https://medibot-r454.onrender.com

---

## 🖥️ Demo

Check out the video demo of MedBot below:

[![MedBot Demo](https://img.youtube.com/vi/RY1o3Tm1a1s/0.jpg)](https://youtu.be/RY1o3Tm1a1s)

---

## 🛠️ Project Structure

```
Medical_Diagnosis_Chatbot/
│
├── app.py                      # Main Streamlit application
├── style.css                   # Custom CSS for styling
├── logo.png                    # Logo image for the header
├── models/                     # Directory for YOLO models
│   ├── eye_disease.pt          # Pre-trained YOLO model for eye diseases
│   ├── lung_cancer.pt          # Pre-trained YOLO model for lung cancer
│   └── fracture.pt             # Pre-trained YOLO model for fractures
├── utils/                      # Utility functions
│   ├── disease_detection.py    # YOLO model inference and plotting
│   └── chatbot.py              # Gemini API integration
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🧠 How It Works

1. **Image Upload**:
   - Users upload a medical image (X-ray, CT scan, or eye image).
   - YOLO detects diseases and provides bounding boxes, labels, and confidence scores.

2. **Gemini Analysis**:
   - The annotated image and YOLO output are sent to the Gemini API for analysis.
   - Gemini provides a diagnosis, possible causes, medical advice, and recommendations.

3. **Chatbot Interaction**:
   - Users can ask questions about the detected condition or general medical queries.
   - The chatbot provides confident and professional responses.

---

## 🛠️ Technologies Used

- **Streamlit**: For building the interactive web UI.
- **YOLO (Ultralytics)**: For real-time disease detection.
- **Gemini API**: For generating medical insights and answering queries.
- **OpenCV**: For image processing and annotation.
- **Pillow**: For image handling.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## 📧 Contact

For any questions or feedback, feel free to reach out:

- **Email**: vendotha@gmail.com
- **GitHub**: [vendotha](https://github.com/vendotha)
- **LinkedIn**: [Buvananand Vendotha](https://linkedin.com/in/vendotha)

---

## 🙏 Acknowledgments

- Thanks to **Google** for the Gemini API.
- Thanks to **Ultralytics** for the YOLO models.
- Thanks to the **Streamlit** team for the amazing framework.

---

## 🌐 Live Demo

Check out the live demo of MedBot [here](#) (coming soon).

---

Made with ❤️ by [Bhuvan Vendotha](https://github.com/vendotha).

