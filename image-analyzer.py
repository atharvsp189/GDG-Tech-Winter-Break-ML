import google.generativeai as genai
import streamlit as st
from PIL import Image

genai.configure(api_key="") # Paste Your API key Here

def get_gemini_repsonse(input, image, prompt):
    model = genai.GenerativeModel(model_name = "gemini-1.5-pro")
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="Gemini Food Analyzer")
st.header("Food Lable Analyzer")

input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Analyse Image")

input_prompt = """
You are a Nutritional expert. from the given food lable analyze if it is healthy to consumer or not. lable is for a food
"""

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_repsonse(input_prompt, image_data, input)
    st.subheader("The Response is")
    st.write(response)