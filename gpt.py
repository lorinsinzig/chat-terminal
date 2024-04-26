from openai import OpenAI
import pyttsx3
import os

# Load your API key from an environment variable
api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found. Make sure to set the OPENAI_API_KEY environment variable.")

openai = OpenAI(api_key=api_key)

# Initialize the TTS library
engine = pyttsx3.init()

def chat_with_gpt():

    # Create a list to store all the messages for context
    messages = [
        {"role": "system", "content": "Du bist GPT, eine lebensechte intelligente Serviceassistentin. Du antwortest immer auf Deutsch, und immer möglichst kurz, aber bleibst trotzdem lebendig. Sie sollen im Gespräch ein möglichst menschenmögliches Erlebnis vermitteln."},
        {"role": "user", "content": "Du weisst das alles bereits: Ich bin Lorin Sinzig. Ich lebe in der Schweiz, bin 18 Jahre alt."},
    ]

    # Keep repeating the following
    while True:
        # Prompt user for input
        message = input("You: ")

        # Exit program if user inputs "quit"
        if message.lower() == "quit":
            break

        # Add each new message to the list
        messages.append({"role": "user", "content": message})

        # Request gpt-3.5-turbo for chat completion
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )

        # Print the response and add it to the messages list
        chat_message = completion.choices[0].message.content
        messages.append({"role": "assistant", "content": chat_message})

        # Print the response of GPT
        print(f"GPT: {chat_message}")

        # Play the text as voice
        #engine.say(chat_message)
        #engine.runAndWait()


if __name__ == "__main__":
    print("Start chatting with GPT (type 'quit' to stop)!")
    chat_with_gpt()