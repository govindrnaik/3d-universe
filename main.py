import os
from typing import List, Optional

from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.language_models import ChatModel
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()


# Define tools
@tool
def calculator(expression: str) -> float:
    """Evaluates a mathematical expression."""
    try:
        return eval(expression)
    except Exception as e:
        return f"Error calculating: {str(e)}"


@tool
def get_current_date() -> str:
    """Returns the current date."""
    from datetime import datetime

    return datetime.now().strftime("%Y-%m-%d")


@tool
def search_info(query: str) -> str:
    """Search for information about a given query."""
    # In a real implementation, you would integrate with a search API
    # For demonstration, we'll just return a placeholder
    return f"Here's information about: {query}. This is a simulated search result."


def create_agent() -> AgentExecutor:
    """Creates and returns a LangChain agent with tools."""

    # Initialize the Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )

    # Define tools list
    tools = [calculator, get_current_date, search_info]

    # Create prompt
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful AI assistant that can use tools to answer questions. Use the following format:\n\nQuestion: the input question you must answer\nThought: you should always think about what to do\nAction: the action to take, should be one of [{tool_names}]\nAction Input: the input to the action\nObservation: the result of the action\n... (this Thought/Action/Action Input/Observation can repeat N times)\nThought: I now know the final answer\nFinal Answer: the final answer to the original input question",
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    # Create agent - using create_react_agent which is more compatible with non-OpenAI models
    agent = create_react_agent(llm, tools, prompt)

    # Create agent executor
    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
    )


def main():
    """Main function to run the chatbot."""
    # Check if API key is set
    if not os.getenv("GOOGLE_API_KEY"):
        print("Please set your GOOGLE_API_KEY environment variable or in a .env file")
        print("Creating a sample .env file...")
        with open(".env", "w") as f:
            f.write("GOOGLE_API_KEY=your-api-key-here\n")
        print(
            ".env file created. Please add your Google API key and restart the application."
        )
        return

    # Create agent
    agent_executor = create_agent()

    # Chat history
    chat_history = []

    print("Welcome to the LangChain Chatbot with Tools (Gemini model)!")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            # Invoke agent
            response = agent_executor.invoke(
                {"input": user_input, "chat_history": chat_history}
            )

            # Print response
            print(f"AI: {response['output']}")

            # Update chat history
            chat_history.append(HumanMessage(content=user_input))
            chat_history.append(AIMessage(content=response["output"]))
        except Exception as e:
            print(f"Error: {str(e)}")

    print("Chat session ended.")
