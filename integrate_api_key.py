#integrating your Together AI API key using OpenAI

import os
from openai import OpenAI

client = OpenAI(
  api_key=os.environ.get("TOGETHER_API_KEY"), 
  base_url="https://api.together.xyz/v1"
)

def get_embeddings(texts, model="togethercomputer/m2-bert-80M-32k-retrieval"):
   texts = [text.replace("\n", " ") for text in texts]
   outputs = client.embeddings.create(input = texts, model=model)
   return [outputs.data[i].embedding for i in range(len(texts))]

embeddings = get_embeddings(texts)
