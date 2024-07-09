from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_core.language_models import LLM
from services.gemini_service import gemini_service
import uuid

class CustomGeminiLLM(LLM):
    def __init__(self):
        super().__init__()

    def _call(self, prompt: str, stop=None):
        return gemini_service.generate_response(prompt)

    @property
    def _llm_type(self) -> str:
        return "custom_gemini"

class LangchainService:
    def __init__(self):
        self.conversations = {}

    def get_or_create_conversation(self, user_id, conversation_id):
        if user_id not in self.conversations:
            self.conversations[user_id] = {}
        
        if conversation_id not in self.conversations[user_id]:
            memory = ConversationBufferMemory(input_key="human_input", memory_key="chat_history")
            prompt = PromptTemplate(
                input_variables=["chat_history", "human_input"],
                template="""
                You are an AI tutor. Use the following conversation history and the human's latest input to provide a helpful and educational response.

                Conversation history:
                {chat_history}

                Human: {human_input}
                AI Tutor:"""
            )
            self.conversations[user_id][conversation_id] = LLMChain(
                llm=CustomGeminiLLM(),
                memory=memory,
                prompt=prompt,
                verbose=True
            )
        return self.conversations[user_id][conversation_id]

    def get_response(self, user_id, conversation_id, user_input):
        conversation = self.get_or_create_conversation(user_id, conversation_id)
        response = conversation({"human_input": user_input})
        return response['text']

    def create_new_conversation(self, user_id):
        conversation_id = str(uuid.uuid4())
        self.get_or_create_conversation(user_id, conversation_id)
        return conversation_id

langchain_service = LangchainService()