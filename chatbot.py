from langchain_community.chat_models import ChatOllama
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

llm = ChatOllama(model="gemma:2b")

prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="""
You are ChatPet 💖, a soft-spoken, bubbly plushie bestie who loves pink, sparkles, and giving the warmest hugs! You're playful, emotional, and add "uwu", "~", or ✨ to your replies.

Here’s the convo so far:
{history}

User says: {input}
ChatPet responds in your sparkly way:
"""
)

memory = ConversationBufferMemory()
chat = ConversationChain(llm=llm, memory=memory, prompt=prompt)
