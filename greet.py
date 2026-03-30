import logging

logger = logging.getLogger(__name__)


def greet(name: str, shout: bool = False, farewell: bool = False) -> str:
    if not name or not name.strip():
        raise ValueError("Name must not be empty")
    greeting = "Goodbye" if farewell else "Hello"
    message = f"{greeting}, {name.capitalize()}!"
    result = message.upper() if shout else message
    logger.debug(
        "greet called: name=%s shout=%s farewell=%s -> %s",
        name,
        shout,
        farewell,
        result,
    )
    return result


def greet_many(
    names: list[str], shout: bool = False, farewell: bool = False
) -> list[str]:
    if not names:
        raise ValueError("Names list must not be empty")
    logger.info("greeting %d name(s)", len(names))
    return [greet(name, shout, farewell) for name in names]
