import ollama

# Initializing an empty list for storing the chat messages and setting up the initial system message
chat_messages = []

# Defining a function to create new messages with specified roles ('user' or 'assistant')
def create_message(message, role):
  return {
    'role': role,
    'content': message
  }

# Starting the main conversation loop
def chat_with_llama3():
  while True:
  # Prompt user for input
    message = input("You: ")

    # Exit program if user inputs "quit"
    if message.lower() == "quit":
      break

    # Add each new message to the list
    chat_messages.append({"role": "user", "content": message})

    # Calling the ollama API to get the assistant response
    response = ollama.chat(model='llama3', stream=True, messages=chat_messages)

    # Preparing the assistant message by concatenating all received chunks from the API
    assistant_message = ''
    for chunk in response:
      assistant_message += chunk['message']['content']
      print(chunk['message']['content'], end='', flush=True)
      
    # Adding the finalized assistant message to the chat log
    chat_messages.append({"role": "assistant", "content": assistant_message})


if __name__ == "__main__":
    print("Start chatting with Gemini (type 'quit' to stop)!")
    chat_with_llama3()