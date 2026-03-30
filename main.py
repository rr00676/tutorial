def greet(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("--name", default="World", help="Name to greet")
    args = parser.parse_args()
    print(greet(args.name))
