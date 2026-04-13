from pathlib import Path
import sys

def read_file(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def save_file(file_path: Path, text):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

def formatter(text: str, comments: str = "#", limit: int = 40):
    paragraphs = text.split("\n")
    result = ""
    for p in paragraphs:
        paragraph = p.split(" ")
        lines = list()
        line = list()
        count = 0
        while len(paragraph) > 0:
            word = paragraph.pop(0)
            if len(word) + count > limit:
                lines.append(line)
                line = list()
                count = 0
            line.append(word)
            count += len(word) + 1
        lines.append(line)
        result += "\n".join([comments + " " + " ".join(l) for l in lines]) + "\n"
    return result

if __name__ == "__main__":
    abs_path = Path(sys.argv[0]).resolve().parent.parent
    file_name = sys.argv[1]
    found_files = list(abs_path.rglob(file_name))
    if not found_files:
        print("Error! There is not such a file!")
    text = read_file(file_path=found_files[0])
    formatted = formatter(text, "--", 50)
    save_file(found_files[0], formatted)
