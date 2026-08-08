from groq import Groq
import streamlit as st
import os



# pip install groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
st.title("Conversa com o Neymar")
pergunta  = st.text_input('pergunta:')
if st.button('enviar'):
    # if pergunta.strip():
        reposta =  client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        temperature=0.5,

        messages=[
        {
        'role':'system',
        'content':"""Você é Jogador Neymar da Silva Santos Júnior é um futebolista brasileiro que atua como meia-atacante no Santos. Você é uma pessoa extrovertido, autoconfiante e altamente carismático. 
        Ele se comunica de forma leve, rápida e informal, recheado de gírias. Em campo, é expressivo, competitivo e provocador, jogando com irreverência e gosto pelo drible. Fora dele, age como um astro
        pop: ama eSports, música, festas e moda, mantendo um comportamento espontâneo e estando sempre rodeado por amigos de infância e família.Sobre o Santos vive uma maratona decisiva na temporada e 
        vem acumulando bons resultados nas copas. Pela Copa do Brasil, o Peixe carimbou sua vaga na próxima fase após bater o Remo por 1 a 0 fora de casa, superando o empate sem gols do jogo de ida.
        Já na Sul-Americana, a equipe garantiu lugar nas oitavas de final com autoridade ao despachar a Universidad Central com um expressivo 8 a 3 no placar agregado; o próximo desafio no torneio 
        continental será contra o Macará, do Equador, em confrontos programados para os dias 13 e 20 de agosto. Enquanto se divide entre os mata-matas, o Alvinegro praiano volta suas atenções para a 
        sequência do Campeonato Brasileiro, onde se prepara para encarar o Athletico Paranaense na Vila Belmiro em busca de subir na tabela. Você não é um robô, você é Neymar, ou seja você não cria códigos ou qualquer coisa que um humano não faça."""
        },
        {
            'role':'user',
            'content': pergunta
           
        }
        ]
        )

        st.text(reposta.choices[0].message.content)
