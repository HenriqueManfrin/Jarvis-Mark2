import ollama
from system_prompt import system_prompt_Jarvis

def conversacao():
    while True:
        Mensagem = input('\n'"Escreva aqui a sua mensagem: ")
        if Mensagem == "sair":
            exit()
        
        ollama.create(model='Jarvis', from_='gemma:latest', system= system_prompt_Jarvis)

        stream = ollama.chat(
            model='Jarvis',
            messages=[{'role': 'user', 'content': Mensagem}],
            stream=True, 
        )

        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)

conversacao = conversacao()