from groq import Groq
from modulo.submodulo.funcoes import mostar_text


text  =  input('Digite um texto: ')


print(mostar_text(text))




# pip install groq 
while True: 
    client = Groq (
    api_key = "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"
    )


    pergunta =  st.text_input('pergunta: ')
    reposta =  client.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    temperature=0.7,
    messages=[
    {
    'role':'system',
    'content':"Você é um piloto de avião."
    },
    {
        'role':'user',
        'content': pergunta
        
    }
    ]
    )
    st.write(reposta.choices[0].message.content)