import openai
import speech_recognition as sr
from dotenv import load_dotenv
import pyttsx3
import os

load_dotenv()

# Set your OpenAI API key
api_key = os.getenv("API_KEY")
openai.api_key = api_key

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to generate responses using LLM
# def generate_response(prompt):
#     response = openai.Completion.create(
#         engine="text-davinci-003",  # Use the LLM engine
#         prompt=prompt,
#         max_tokens=150,  # Adjust as needed
#         stop=None,  # Stop generating text at a certain point
#         temperature=0.7,  # Adjust the creativity of responses
#     )
#     return response.choices[0].text.strip()


def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the chat model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content'].strip()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main chatbot loop
print("PDF Chatbot: Hi! How can I assist you today?")
while True:
    user_input = input("User (text): ")

    if user_input.lower() == "exit":
        print("PDF Chatbot: Goodbye!")
        break

    # Check if the user wants to search for documents
    if "search for documents" in user_input.lower():
        query = input("User: Enter your document search query (text): ")
        # Implement your document search logic here and store results in relevant_documents

        relevant_documents = []  # Replace with actual relevant documents

        if not relevant_documents:
            print("PDF Chatbot: No relevant documents found.")
        else:
            print("PDF Chatbot: Here are some relevant documents:")
            for doc in relevant_documents:
                print(doc)

    # Generate a response based on user input
    chatbot_response_text = generate_response(f"User (text): {user_input}\nPDF Chatbot:")
    print(f"PDF Chatbot (text): {chatbot_response_text}")

    # Convert text response to speech
    speak(chatbot_response_text)

    # Allow the user to speak (audio input)
    user_audio_input = input("User (audio): Speak or type 'exit' to end: ")

    if user_audio_input.lower() == "exit":
        print("PDF Chatbot: Goodbye!")
        break

    if "search for documents" in user_audio_input.lower():
        query = input("User: Enter your document search query (audio): ")
        # Implement your document search logic here and store results in relevant_documents

        relevant_documents = []  # Replace with actual relevant documents

        if not relevant_documents:
            print("PDF Chatbot: No relevant documents found.")
        else:
            print("PDF Chatbot: Here are some relevant documents:")
            for doc in relevant_documents:
                print(doc)

    # Convert audio input to text
    with sr.Microphone() as source:
        print("PDF Chatbot: Listening for audio input...")
        audio = r.listen(source)
    
    try:
        user_audio_input = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("PDF Chatbot: Could not understand audio.")
        continue

    # Generate a response based on user audio input
    chatbot_response_audio_text = generate_response(f"User (audio): {user_audio_input}\nPDF Chatbot:")
    print(f"PDF Chatbot (audio text): {chatbot_response_audio_text}")

    # Convert text response to speech
    speak(chatbot_response_audio_text)