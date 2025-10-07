import os
from openai import AzureOpenAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

endpoint = "https://aoi-internship.openai.azure.com/"
model_name = "gpt-4o"
deployment = "gpt-4o"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=os.getenv("AZURE_OPENAI_KEY"),
)

def get_completion_from_messages(messages, model=deployment, temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    messages.append({"role": "assistant", "content": response.choices[0].message.content})
    return response.choices[0].message.content

# context = [{"role": "system", "content": "You are a helpful assistant."}]

# while True:
#     response = get_completion_from_messages(context)
#     print("AI:", response)
#     user_input = input("User: ")
#     if user_input.lower() in ["exit", "quit"]:
#         break
#     context.append({"role": "user", "content": user_input})