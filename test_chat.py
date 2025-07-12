from langchain_community.chat_models import ChatOllama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = ChatOllama(model="mistral")  # or "gemma", "llama3" etc.
memory = ConversationBufferMemory()
chat = ConversationChain(llm=llm, memory=memory, verbose=True)

print("🌸 ChatPet is ready! Say hi (type 'exit' to stop):")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = chat.run(user_input)
    print("ChatPet 💕:", response)
