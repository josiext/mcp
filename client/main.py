import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent


async def main():
    client = MultiServerMCPClient(
        {
            "weather": {
                "transport": "http",
                # Ensure you start your weather server on port 8000
                "url": "http://localhost:8000/mcp",
            },
        }
    )

    all_tools = await client.get_tools()

    print("all tools:", all_tools)

    selected_tool_names = ["get_weather"]
    tools = [tool for tool in all_tools if tool.name in selected_tool_names]

    agent = create_agent(
        "gemini-2.5-flash",
        tools,
    )

    weather_response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "what is the weather in nyc",
                }
            ]
        }
    )

    print("last response:", weather_response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
