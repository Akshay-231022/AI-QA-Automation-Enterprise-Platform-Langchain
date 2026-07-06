import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment API keys securely
load_dotenv()

# Define generic payload structure for the chat interface
messages = [
    SystemMessage(content="You are a helpful data analyst tutor."),
    HumanMessage(content="Explain what a dataframe is in exactly 1 sentence.")
]

def run_model_example(provider_name: str, model_name: str):
    print(f"\n--- Running via {provider_name} Wrapper ({model_name}) ---")
    try:
        # The universal initialization strategy dynamically resolves standard inputs
        model = init_chat_model(
            model=model_name,
            model_provider=provider_name,
            temperature=0.2
        )
        
        # Invoke via standard LangChain Expression Language (LCEL) endpoint
        response = model.invoke(messages)
        print(f"Response: {response.content}")
        
    except Exception as e:
        print(f"Failed to execute {provider_name}: {e}")

# 1. Using ChatOpenAI wrapper implicitly
run_model_example(provider_name="openai", model_name="gpt-4o")

# 2. Swapping seamlessly to ChatGoogleGenerativeAI wrapper
run_model_example(provider_name="google_genai", model_name="gemini-2.5-flash")
