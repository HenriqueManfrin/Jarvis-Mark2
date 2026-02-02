import ollama

stream = ollama.chat(
    model='gemma:latest',
    messages=[{'role': 'user', 'content': 'Diga Olá Mundo'}],
    stream=True,
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
