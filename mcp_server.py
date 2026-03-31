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


@mcp.tool()
def get_top_spenders(limit: int = 5, category: str | None = None) -> list[dict]:
    """Return customers ranked by total spend, optionally filtered by product category.

    Each result has: customer_name, city, total_spend, order_count.
    """
    if category is not None:
        sql = """
            SELECT c.name AS customer_name, c.city,
                   ROUND(SUM(oi.quantity * p.price), 2) AS total_spend,
                   COUNT(DISTINCT o.id) AS order_count
            FROM customers c
            JOIN orders o ON o.customer_id = c.id
            JOIN order_items oi ON oi.order_id = o.id
            JOIN products p ON p.id = oi.product_id
            WHERE p.category = ?
            GROUP BY c.id
            ORDER BY total_spend DESC
            LIMIT ?
        """
        params: tuple = (category, limit)
    else:
        sql = """
            SELECT c.name AS customer_name, c.city,
                   ROUND(SUM(oi.quantity * p.price), 2) AS total_spend,
                   COUNT(DISTINCT o.id) AS order_count
            FROM customers c
            JOIN orders o ON o.customer_id = c.id
            JOIN order_items oi ON oi.order_id = o.id
            JOIN products p ON p.id = oi.product_id
            GROUP BY c.id
            ORDER BY total_spend DESC
            LIMIT ?
        """
        params = (limit,)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(sql, params).fetchall()
    conn.close()
    return [dict(row) for row in rows]


@mcp.tool()
def get_sales_by_category() -> list[dict]:
    """Return total revenue and units sold, broken down by product category.

    Each result has: category, total_revenue, units_sold, order_count.
    """
    sql = """
        SELECT p.category,
               ROUND(SUM(oi.quantity * p.price), 2) AS total_revenue,
               SUM(oi.quantity) AS units_sold,
               COUNT(DISTINCT o.id) AS order_count
        FROM order_items oi
        JOIN products p ON p.id = oi.product_id
        JOIN orders o ON o.id = oi.order_id
        GROUP BY p.category
        ORDER BY total_revenue DESC
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(sql).fetchall()
    conn.close()
    return [dict(row) for row in rows]


if __name__ == "__main__":
    mcp.run()
