from mcp.server.fastmcp import FastMCP

# ------------------------------------------------------------------------------------------------------------------------

mcp = FastMCP("Weather")


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    
    if location.lower() == "san antonio":
        return "It's currently partly cloudy and 85 degrees fahrenheit in San Antonio"
    elif location.lower() == "new york":
        return "It's currently sunny and 70 degrees fahrenheit in New York"
    else:
        return f"It's currently pleasant weather in {location}"


if __name__ == "__main__":
    mcp.run(transport="sse")
