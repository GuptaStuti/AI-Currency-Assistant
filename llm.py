from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from config import HF_TOKEN

# -----------------------------
# Create HuggingFace Endpoint
# -----------------------------

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    huggingfacehub_api_token=HF_TOKEN,
    task="text-generation",
    temperature=0.2,  # i want the conversion to be deterministic and not creative
    max_new_tokens=512,  # Enough for explainations without waisting tokens
)

# -----------------------------
# Chat Model
# -----------------------------

chat_model = ChatHuggingFace(llm=llm)
