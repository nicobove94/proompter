import openai
import sys
import os
openai.api_key = os.getenv('PROOMPTER_KEY')

# ensure the question is passed as command line argument
if len(sys.argv) != 2:
    print("Please provide a question as a command line argument.")
    sys.exit()

question = sys.argv[1]
prompt = "What is the optimal way to phrase this query for ChatGPT-4?'" + question + "'"

response = openai.Completion.create(
  engine="text-davinci-003",  # You can change the engine as per your needs
  prompt=prompt,
  temperature=0.5,
  max_tokens=100
)

# print the reformulated question
print(response.choices[0].text.strip())
