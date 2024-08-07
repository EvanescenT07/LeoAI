from openai import OpenAI


API_KEY = open("API_KEY", "r").read()
client = OpenAI(
      api_key=API_KEY,
)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "What is your name?"
    }
  ],
  max_tokens=500,
)

print(response.choices[0].message.content)

