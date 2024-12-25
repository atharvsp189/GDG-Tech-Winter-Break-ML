import os
import google.generativeai as genai

genai.configure(api_key="")  # Paste Your API key Here

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="You are a Health ChatBot. Provide the information to the question asked about? keep the response informative yet short. If the question is different from the provided context the just say \"I'm trained on providing answers related to health\"",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Hello give me information about nutritional content of an egg.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Certainly! Here's a brief overview of the nutritional content of a large egg:\n\n*   **Calories:** About 70\n*   **Protein:** Approximately 6 grams (high-quality protein)\n*   **Fats:** Around 5 grams (including both saturated and unsaturated fats)\n*   **Cholesterol:** Roughly 186 mg (mostly in the yolk)\n*   **Vitamins:** Rich in Vitamin B12, Vitamin D, Vitamin A, riboflavin, and folate.\n*   **Minerals:** Contains phosphorus, selenium, and choline.\n\nEggs are a nutrient-dense food and a great source of protein.\n",
      ],
    },
  ]
)


while(True):
    message = input("Enter Message : ")
    response = chat_session.send_message(message)
    print(response.text)