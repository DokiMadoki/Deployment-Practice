# Summarizer
This is a simple program that summarizes the content in input.txt and writes that output to summary.txt.
The file needs to be run inside a venv
```bash
# Create and activate
python3 -m venv .venv
source .venv/bin/activate
```
requirements.txt has the required things to run it. 
```bash
python -m pip install -r requirements.txt
```

we need a .env file with your openrouter API key. use .env.example to create one.
Copy that file and save it as .env 
```bash
cp .env.example .env
```
You should be able to see OPENROUTER_API_KEY=your_api_key which takes your Openrouter API Key.
replace 'your_api_key' with your Key



The output should be in summary.txt and the command will tell you the token usage after it runs. 
use 
```bash
python summarize.py 
```