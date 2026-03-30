def greet(name: str, shout: bool = False, farewell: bool = False) -> str:
    greeting = "Goodbye" if farewell else "Hello"
    message = f"{greeting}, {name.capitalize()}!"
    return message.upper() if shout else message


def greet_many(names: list, shout: bool = False, farewell: bool = False) -> list:
    return [greet(name, shout, farewell) for name in names]
