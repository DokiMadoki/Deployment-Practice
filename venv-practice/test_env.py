import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("MOCK_API_KEY")
environment = os.getenv("ENVIRONMENT")

if not api_key:
    print("API key is not provided")
    exit(1)
else:
    printable_key = f"{api_key[:5]}*********"
    print(f"ENVIRONMENT={environment}")
    print(f"API KEY={printable_key}")