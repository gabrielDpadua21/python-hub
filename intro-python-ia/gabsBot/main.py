import os

from langchain.chains.qa_with_sources.stuff_prompt import template
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import YoutubeLoader

os.environ['GROQ_API_KEY'] = "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"
CHAT = ChatGroq(model='llama-3.3-70b-versatile')

def bot_youtube_transcript(messages):
    url = input("Input video url: ")
    loader = YoutubeLoader.from_youtube_url(url, language=['pt'])
    list_documents = loader.load()
    documents = ''
    for docs in list_documents:
        documents = documents + docs.page_content
    template = ChatPromptTemplate.from_messages([
        ('system', 'Você é um assistent amigavel chamado GabzzBot, e tem acesso a transcrição de um video do YouTube para dar suas respostas: {documents}'),
        ('user', '{input}')
    ])
    chain = template | CHAT
    return chain.invoke({'documents': documents, 'input': messages}).content



def bot_answer(messages):
    messages_model = [('system', 'Você é um assistente amigavel chamado GabzzBot')]
    messages_model += messages
    template = ChatPromptTemplate.from_messages(messages_model)
    chain = template | CHAT
    return chain.invoke({}).content


def bot_scrapping(messages):
    url = input("Write the host: ")
    loader = WebBaseLoader(url)
    list_documents = loader.load()
    documents = ''
    for docs in list_documents:
        documents = documents + docs.page_content
    template = ChatPromptTemplate.from_messages([
        ('system', 'Você é um assistente amigavel chamado GabzzBot, e tem acesso as seguintes informações para dar as suas respostas: {documents}'),
        ('user', '{input}')
    ])
    chain = template | CHAT
    return chain.invoke({'documents': documents, 'input': messages}).content

if __name__ == "__main__":
    print("Welcome to GabzzBot IA")
    name = input("tell me your name: ")
    print(f"Hello, {name}")
    msgs = []

    while True:
        key = input("Write type X to Exit or \n 1 (Scrapper Bot) \n 2 (Transcript Bot) \n 3 (Answer Bot): ")
        if key.lower() == "x": break
        question = input("User: ")
        msgs.append(('user', question))
        answer = ''
        if key == '1': answer = bot_scrapping(msgs)
        elif key == '2': answer = bot_youtube_transcript(msgs)
        elif key == '3': answer = bot_answer(msgs)
        msgs.append(('assistant', answer))
        print(f"GabzzBot: {answer}")


    print("******************************")
    print("Thanks for using gabs bot, bye")