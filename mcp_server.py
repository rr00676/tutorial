import sqlite3

from mcp.server.fastmcp import FastMCP

from greet import greet, greet_many

DB_PATH = "sales.db"
mcp = FastMCP("tutorial-greeter")


@mcp.tool()
def greet_one(name: str, shout: bool = False, farewell: bool = False) -> str:
    """Greet a single person by name."""
    return greet(name, shout=shout, farewell=farewell)


@mcp.tool()
def greet_multiple(names: list[str], shout: bool = False, farewell: bool = False) -> list[str]:
    """Greet multiple people by name."""
    return greet_many(names, shout=shout, farewell=farewell)


@mcp.tool()
def list_tables() -> list[str]:
    """List all tables in the sales database."""
    conn = sqlite3.connect(DB_PATH)
    tables = [row[0] for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")]
    conn.close()
    return tables


@mcp.tool()
def get_schema(table_name: str) -> list[dict]:
    """Get the column names and types for a table."""
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(f"PRAGMA table_info({table_name})").fetchall()
    conn.close()
    return [{"column": row[1], "type": row[2]} for row in rows]


@mcp.tool()
def query(sql: str) -> list[dict]:
    """Run a read-only SQL query against the sales database and return results."""
    if not sql.strip().upper().startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(sql).fetchall()
    conn.close()
    return [dict(row) for row in rows]


if __name__ == "__main__":
    mcp.run()
