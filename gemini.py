import google.generativeai as genai

GOOGLE_API_KEY='...'
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-pro')

print('\nReady to chat...')

while True:
  input= input("You: ")
  response = model.generate_content(input, stream=True)
  for chunk in response:
    print(chunk.text)