from greet import greet_many

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("--name", nargs="+", default=["World"], help="One or more names to greet")
    parser.add_argument("--shout", action="store_true", help="Uppercase the greeting")
    parser.add_argument("--farewell", action="store_true", help="Say goodbye instead of hello")
    args = parser.parse_args()
    for message in greet_many(args.name, args.shout, args.farewell):
        print(message)
