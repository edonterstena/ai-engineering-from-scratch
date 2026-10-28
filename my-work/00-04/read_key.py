import os
from dotenv import load_dotenv

load_dotenv()
key = os.environ.get("DEMO_API_KEY")

if key is None:
    print("No key found. Did you create the .env file?")
else:
    print("Key loaded:", key[:7] + "...")