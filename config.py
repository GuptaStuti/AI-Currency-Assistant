import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
EXCHANGE_RATE_API = os.getenv("EXCHANGE_RATE_API_KEY")
