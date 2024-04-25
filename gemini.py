import google.generativeai as genai
import os

# Load your API key from an environment variable
api_key = os.environ.get("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found. Make sure to set the OPENAI_API_KEY environment variable.")

genai.configure(api_key=api_key)


# Initializing an empty list for storing the chat messages and setting up the initial system message
history = []
# Starting the main conversation loop
def chat_with_gemini():
    
    while True:

      # Prompt user for input
      message = input("\nYou: ")

      print()

      # Exit program if user inputs "quit"
      if message.lower() == "quit":
          break
      if message == '':
        chat_with_gemini()
        break

      # Add each new message to the list
      history.append({"role": "user", "content": message})

      model = genai.GenerativeModel('gemini-pro')
      chat = model.start_chat(history=[])

      response = chat.send_message("Okay, how about a more detailed explanation to a high schooler?", stream=True)

      # Preparing the assistant message by concatenating all received chunks from the API
      assistant_message = ''
      for chunk in response:
        assistant_message += chunk.text
        print(chunk.text)

      history.append({"role": "assistant", "content": assistant_message})


if __name__ == "__main__":
  print("Start chatting with Gemini (type 'quit' to stop)!")
  chat_with_gemini()
