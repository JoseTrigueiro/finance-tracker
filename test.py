from openai import OpenAI
import os

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key=os.getenv("HUGGING_FACE_HUB_TOKEN"),
)

completion = client.chat.completions.create(
    model="microsoft/Phi-3-mini-4k-instruct", messages=[{"role": "user", "content": "Tell me a joke"}]
)

print(completion.choices[0].message)
