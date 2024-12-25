## Health Chatbot Readme

This directory contains the code for a health chatbot built using Google GenerativeAI. 

The chatbot is designed to provide informative yet short answers to health-related questions. It is important to note that this chatbot is not a substitute for professional medical advice. If you have any concerns about your health, please consult a doctor.

### Dependencies

This code requires the following Python libraries:

* google.generativeai

### Setup

1. Install the required libraries:

   ```bash
   pip install google-generativeai
   ```

2. Replace `""` in the line `genai.configure(api_key="")` with your actual Google GenerativeAI API key.

### Running the Code

1. Save the code in a Python file (e.g., `health_chatbot.py`).
2. Run the script from the command line:

   ```bash
   python health_chatbot.py
   ```

This will start the chatbot and allow you to interact with it by typing in questions.

## Food Analyzer Readme

This directory contains the code for a food analyzer web application built using Streamlit and Google GenerativeAI. 

The application allows users to upload an image of a food label and receive analysis of its nutritional content. It is important to note that this application is for informational purposes only and should not be used as a substitute for professional dietary advice.

### Dependencies

This code requires the following Python libraries:

* google.generativeai
* streamlit
* PIL

### Setup

1. Install the required libraries:

   ```bash
   pip install streamlit google-generativeai Pillow
   ```

2. Replace `""` in the line `genai.configure(api_key="")` with your actual Google GenerativeAI API key.

### Running the Code

1. Save the code in a Python file (e.g., `food_analyzer.py`).
2. Run the script from the command line:

   ```bash
   streamlit run food_analyzer.py
   ```

This will launch the Streamlit application in your web browser, where you can upload food label images and see the analysis results.
