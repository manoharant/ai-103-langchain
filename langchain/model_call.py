# pip install langchain langchain-openai
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
deployment_name = os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"]
api_key = os.environ["AZURE_OPENAI_API_KEY"]

client=ChatOpenAI(
    base_url=endpoint,
    api_key=api_key,
    model=deployment_name
)

response=client.invoke("What are the three main benefits of using managed AI endpoints in the cloud?")
print(response.content)