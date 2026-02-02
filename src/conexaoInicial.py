import ollama

MensagemInicial = input("Escreva aqui a sua mensagem: ")

stream = ollama.chat(
    model='gemma:latest',
    messages=[{'role': 'user', 'content': MensagemInicial}],
    stream=True, 
)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
