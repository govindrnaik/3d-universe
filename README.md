# LangChain Chatbot with Tools

This is a simple chatbot application that uses LangChain to interact with various tools. The chatbot can perform calculations, provide the current date, and simulate searching for information.

## Features

- Uses the latest LangChain packages
- Implements an agent that can use multiple tools:
  - Calculator: Evaluates mathematical expressions
  - Date tool: Returns the current date
  - Search: Simulates information search
- Maintains chat history for context

## Setup

1. Make sure you have Python 3.8 or later installed.
2. Install the required dependencies:
   ```
   pip install -e .
   ```
   or
   ```
   pip install langchain langchain-openai langchain-core python-dotenv pydantic langchainhub
   ```
3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Usage

Run the chatbot with:

```
python main.py
```

You can then chat with the bot in the terminal. The bot will automatically use the appropriate tools based on your questions.

Example prompts:
- "What is 2 + 2?"
- "What's the current date?"
- "Can you search for information about Python programming?"

Type 'exit' to end the conversation.

## Extending

To add more tools to the chatbot:
1. Create a new function with the @tool decorator
2. Add the function to the tools list in the create_agent function
3. The agent will automatically be able to use your new tool

## Requirements

See `pyproject.toml` for the full list of dependencies.