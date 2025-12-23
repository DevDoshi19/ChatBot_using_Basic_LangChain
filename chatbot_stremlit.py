from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def get_chat_chain():
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.7)

    chat_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{query}")
    ])
    
    return chat_template | model | StrOutputParser()