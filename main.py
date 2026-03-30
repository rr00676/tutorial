def greet(name: str, shout: bool = False, farewell: bool = False) -> str:
    greeting = "Goodbye" if farewell else "Hello"
    message = f"{greeting}, {name.capitalize()}!"
    return message.upper() if shout else message


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("--name", default="World", help="Name to greet")
    parser.add_argument("--shout", action="store_true", help="Uppercase the greeting")
    parser.add_argument("--farewell", action="store_true", help="Say goodbye instead of hello")
    args = parser.parse_args()
    print(greet(args.name, args.shout, args.farewell))
