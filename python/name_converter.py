import sys
from pathlib import Path
import re


def sanitize_filename(filename: str) -> str:
    sanitized = re.sub(r"[^a-zA-Z0-9 ._-]", "", filename)
    sanitized = re.sub(r"\s+", " ", sanitized).strip()

    # Handle potential empty string if all characters were illegal
    if not sanitized:
        return "untitled_file"

    return sanitized.lower().replace(" ", "_")


def folder_extention_choice(key: str) -> list[str]:
    match key:
        case "-j" | "-js" | "-javascript":
            return ["js", ".js"]
        case "-h" | "-php":
            return ["php", ".php"]
        case "-y" | "-py" | "-python":
            return ["python", ".py"]
        case "-s" | "-sql":
            return ["sql", ".sql"]
        case _:
            return ["", ".txt"]


def make_file(filename: str, key: str) -> None:
    san_filename = sanitize_filename(filename)
    folder, extention = folder_extention_choice(key)
    path = Path(folder + "/" + san_filename + extention)
    path.touch()


if __name__ == "__main__":
    args = sorted(sys.argv[1:])
    filename = args.pop()
    key = args.pop()
    make_file(filename, key)