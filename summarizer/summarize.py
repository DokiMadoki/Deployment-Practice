import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    print("There is no Operrouter API Key")
    exit(1)

with open ("input.txt") as f:
    content = f.read()

url = "https://openrouter.ai/api/v1/chat/completions"

prompt = f"Summarize the following: \n\n {content}"
headers = {
    "Authorization": f"Bearer {api_key}",
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-OpenRouter-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    }
payload = {
    "model": "openrouter/free",
    "messages": [
        {"role": "user", "content": prompt}
        ]
    }


response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    data = response.json()
    answer = data["choices"][0]["message"]["content"]
    tokens = data["usage"]
    print(f"The Total Tokens used for this call {tokens}")
    with open ("summary.txt", "w") as f:
        f.write(answer)

else:
    print(f"There was no response {response.status_code}: {response.text}")

