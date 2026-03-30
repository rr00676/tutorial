"""Create and seed the toy sales database."""

import random
import sqlite3

random.seed(42)

PRODUCTS = [
    ("Laptop", 999.99, "Electronics"),
    ("Phone", 699.99, "Electronics"),
    ("Headphones", 149.99, "Electronics"),
    ("Desk Chair", 299.99, "Furniture"),
    ("Standing Desk", 499.99, "Furniture"),
    ("Notebook", 4.99, "Stationery"),
    ("Pen Set", 12.99, "Stationery"),
    ("Coffee Mug", 14.99, "Kitchen"),
    ("Water Bottle", 24.99, "Kitchen"),
    ("Backpack", 79.99, "Accessories"),
]

CUSTOMERS = [
    ("Alice Johnson", "alice@example.com", "New York"),
    ("Bob Smith", "bob@example.com", "London"),
    ("Carol White", "carol@example.com", "Sydney"),
    ("David Brown", "david@example.com", "Toronto"),
    ("Eva Martinez", "eva@example.com", "Madrid"),
    ("Frank Lee", "frank@example.com", "Tokyo"),
    ("Grace Kim", "grace@example.com", "Seoul"),
    ("Henry Wilson", "henry@example.com", "Berlin"),
]


def seed(db_path: str = "sales.db") -> None:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.executescript("""
        DROP TABLE IF EXISTS order_items;
        DROP TABLE IF EXISTS orders;
        DROP TABLE IF EXISTS products;
        DROP TABLE IF EXISTS customers;

        CREATE TABLE customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            city TEXT NOT NULL
        );

        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL
        );

        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL REFERENCES customers(id),
            order_date TEXT NOT NULL
        );

        CREATE TABLE order_items (
            id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL REFERENCES orders(id),
            product_id INTEGER NOT NULL REFERENCES products(id),
            quantity INTEGER NOT NULL
        );
    """)

    cur.executemany(
        "INSERT INTO customers (name, email, city) VALUES (?, ?, ?)", CUSTOMERS
    )
    cur.executemany(
        "INSERT INTO products (name, price, category) VALUES (?, ?, ?)", PRODUCTS
    )

    dates = [f"2024-{m:02d}-{d:02d}" for m in range(1, 13) for d in [5, 12, 20, 27]]
    for i, date in enumerate(dates):
        customer_id = (i % len(CUSTOMERS)) + 1
        cur.execute(
            "INSERT INTO orders (customer_id, order_date) VALUES (?, ?)",
            (customer_id, date),
        )
        order_id = cur.lastrowid
        for _ in range(random.randint(1, 3)):
            product_id = random.randint(1, len(PRODUCTS))
            quantity = random.randint(1, 4)
            cur.execute(
                "INSERT INTO order_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
                (order_id, product_id, quantity),
            )

    conn.commit()
    conn.close()
    print(f"Database seeded at {db_path}")


if __name__ == "__main__":
    seed()
