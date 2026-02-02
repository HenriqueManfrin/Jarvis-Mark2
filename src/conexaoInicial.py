import ollama
def conversacao():
    while True:
        MensagemInicial = input('\n'"Escreva aqui a sua mensagem: ")
        if MensagemInicial == "sair":
            exit()

        stream = ollama.chat(
            model='gemma:latest',
            messages=[{'role': 'user', 'content': MensagemInicial}],
            stream=True, 
        )

        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)

conversacao = conversacao()