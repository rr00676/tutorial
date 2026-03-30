# Tutorial Project

A simple Python CLI project used as a learning experiment for agentic coding workflows.

## Project structure

- `greet.py` — core logic (`greet`, `greet_many`)
- `main.py` — CLI entry point using `argparse` and `rich`
- `test_main.py` — unit tests using `unittest`

## Environment

Always use the virtual environment:
```bash
source .venv/Scripts/activate
```

## Running the app

```bash
python main.py --name Alice
python main.py --name Alice Bob --farewell
python main.py --name Alice --shout
python main.py --name Alice --verbose
```

## Running checks

```bash
# Type checks
mypy

# Tests
python -m unittest test_main.py -v
```

## Communication preferences

- Explain concepts clearly — do not assume prior knowledge of git, tooling, or software engineering
- Propose what a lesson will cover and wait for confirmation before making changes
- After each change, explain what happened and why, but don't over-elaborate
- Where relevant, connect concepts back to how they apply in multi-agent/agentic workflows
- Answer side questions directly without turning them into a lesson unless asked

## Rules

- All logic goes in `greet.py`, not `main.py`
- Always run mypy and tests before committing
- Never skip the pre-commit hook
- Update `requirements.txt` with `pip freeze > requirements.txt` when adding new packages
- Commit messages should follow the pattern: `Lesson N: description`
