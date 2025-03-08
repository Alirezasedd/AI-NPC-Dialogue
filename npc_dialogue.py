import openai
from textblob import TextBlob
import pyttsx3  # Adding AI voice synthesis
import re

# OpenAI API Key (replace with your key or use an alternative NLP model)
OPENAI_API_KEY = "your_api_key_here"

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to generate NPC dialogue using OpenAI GPT
def generate_npc_dialogue(prompt):
    """
    Generates a dynamic NPC dialogue response using OpenAI's GPT model.
    :param prompt: User input prompting NPC dialogue.
    :return: AI-generated NPC response.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an NPC in a fantasy game. Respond naturally."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

# Function to filter dialogue for inappropriate content
def filter_dialogue(dialogue):
    """
    Filters NPC dialogue for inappropriate or offensive content.
    :param dialogue: AI-generated NPC response.
    :return: Filtered response or original response if no issues detected.
    """
    inappropriate_words = ["violence", "curse", "offensive"]  # Expand as needed
    if any(word in dialogue.lower() for word in inappropriate_words):
        return "[Filtered: NPC response contained inappropriate content.]"
    return dialogue

# Function to analyze sentiment of dialogue
def analyze_sentiment(dialogue):
    """
    Analyzes the sentiment of NPC dialogue to ensure appropriate tone.
    :param dialogue: AI-generated NPC response.
    :return: Adjusted response if sentiment is overly negative, otherwise returns original response.
    """
    blob = TextBlob(dialogue)
    sentiment = blob.sentiment.polarity  # Returns a value between -1 (negative) and 1 (positive)
    if sentiment < -0.3:
        return "[Adjusted: NPC dialogue was too negative.]"
    return dialogue

# Function to convert text-to-speech
def speak_dialogue(dialogue):
    """
    Uses text-to-speech to vocalize the NPC dialogue.
    :param dialogue: AI-generated NPC response.
    """
    engine.say(dialogue)
    engine.runAndWait()

# Example Usage
if __name__ == "__main__":
    user_input = "Tell me a story about the ancient kingdom."
    raw_dialogue = generate_npc_dialogue(user_input)
    filtered_dialogue = filter_dialogue(raw_dialogue)
    final_dialogue = analyze_sentiment(filtered_dialogue)
    
    print("User: ", user_input)
    print("NPC: ", final_dialogue)
    speak_dialogue(final_dialogue)
