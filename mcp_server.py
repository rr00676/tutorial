from mcp.server.fastmcp import FastMCP

from greet import greet, greet_many

mcp = FastMCP("tutorial-greeter")


@mcp.tool()
def greet_one(name: str, shout: bool = False, farewell: bool = False) -> str:
    """Greet a single person by name."""
    return greet(name, shout=shout, farewell=farewell)


@mcp.tool()
def greet_multiple(names: list[str], shout: bool = False, farewell: bool = False) -> list[str]:
    """Greet multiple people by name."""
    return greet_many(names, shout=shout, farewell=farewell)


if __name__ == "__main__":
    mcp.run()
