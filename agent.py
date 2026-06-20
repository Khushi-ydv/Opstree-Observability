import argparse

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

load_dotenv()

MODEL = "gemini-2.5-flash"


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    if city.lower() == "atlantis":
        raise ValueError(f"No weather data available for unknown city: {city}")
    return f"It's sunny and 72F in {city}."


def build_agent():
    llm = ChatGoogleGenerativeAI(model=MODEL, temperature=0)
    return create_react_agent(llm, [get_weather])


def run_agent(query: str) -> str:
    agent = build_agent()
    result = agent.invoke({"messages": [("user", query)]})
    return result["messages"][-1].content


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--break", dest="break_mode", action="store_true")
    args = parser.parse_args()

    query = (
        "What's the weather in Atlantis?"
        if args.break_mode
        else "What's the weather in Paris?"
    )
    print(f"Query: {query}")
    print(run_agent(query))
