import logging
import sys
from rich.console import Console
from rich.text import Text
from greet import greet_many

console = Console()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("--name", nargs="+", default=["World"], help="One or more names to greet")
    parser.add_argument("--shout", action="store_true", help="Uppercase the greeting")
    parser.add_argument("--farewell", action="store_true", help="Say goodbye instead of hello")
    parser.add_argument("--verbose", action="store_true", help="Show debug logging")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.WARNING,
        format="%(levelname)s %(name)s: %(message)s"
    )

    try:
        for message in greet_many(args.name, args.shout, args.farewell):
            text = Text(message)
            if args.shout:
                text.stylize("bold red")
            elif args.farewell:
                text.stylize("bold yellow")
            else:
                text.stylize("bold green")
            console.print(text)
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
