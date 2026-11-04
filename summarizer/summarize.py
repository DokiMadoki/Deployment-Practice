import requests
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

base_dir = Path(__file__).resolve().parent
input_path = base_dir / "input.txt"
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    print("There is no Openrouter API Key")
    exit(1)

with open (input_path) as f:
    content = f.read()

url = "https://openrouter.ai/api/v1/chat/completions"

prompt = f"Summarize the following: \n\n {content}"
headers = {
    "Authorization": f"Bearer {api_key}",
    }
payload = {
    "model": "openrouter/free",
    "messages": [
        {"role": "user", "content": prompt}
        ]
    }

summary_path = base_dir / "summary.txt"
try:
    response = requests.post(url, headers=headers, json=payload, timeout=15)
except requests.exceptions.RequestException as error:
    print(f"Error Occured {error}")
    exit(1)

if response.status_code == 200:
    data = response.json()
    answer = data["choices"][0]["message"]["content"]
    tokens = data["usage"]
    print(f"The Total Tokens used for this call {tokens}")
    with open (summary_path, "w") as f:
        f.write(answer)

else:
    print(f"There was no response {response.status_code}: {response.text}")

