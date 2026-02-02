import ollama

response = ollama.generate(model='gemma:latest', prompt='Diga Olá Mundo')
print(response)
