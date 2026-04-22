import json
from pathlib import Path
import re
import sys
import requests
from bs4 import BeautifulSoup

languages = {
    "javascript": ["js", ".js"],
    "php": ["php", ".php"],
    "python": ["python", ".py"],
    "sql": ["sql", ".sql"],
}

comment = {
    "javascript": ["/*", "*/"],
    "php": ["<!--", "-->"],
    "python": ['"""', '"""'],
    "sql": ["/*", "*/"],
}


def load_page(url: str) -> requests.Response:
    headers = {
        "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6,es;q=0.5",
        "priority": "i",
        "referer": "https://www.codewars.com/",
        "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "image",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "cross-site",
        "sec-fetch-storage-access": "active",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    return response


def get_info(page: requests.Response):
    soup = BeautifulSoup(page.text, "html.parser")

    script_tag = soup.find_all("script")

    for s in script_tag:
        if "App.setup" in s.text:
            script_text = s.text
            break

    match_ = re.search(r"\(\"\{.*\}\"\)\,", script_text).group()[1:-2]
    data_ = json.loads(json.loads(match_))
    challenge_name = data_["challengeName"]
    description = data_["description"]
    return challenge_name, description


def clean_name(name: str) -> str:
    sanitized = re.sub(r"[^a-zA-Z0-9 ._-]", "", name)
    sanitized = re.sub(r"\s+", " ", sanitized).strip()
    if not sanitized:
        return "untitled_file"
    return sanitized.lower().replace(" ", "_")


def tokenizer(lines: str) -> list:
    lines_ = lines.split("\n")
    tokens = list()
    temp = {"cmd": [], "text": []}
    for line in lines_:
        if line.startswith(("```", "~~~")) and len(line) > 3:
            temp["cmd"] = line[3:].split(":")
        elif line.startswith(("```", "~~~")):
            tokens.append(temp)
            temp = {"cmd": [], "text": []}
        else:
            temp["text"].append(line)
    tokens.append(temp)
    return tokens


def parser(tokens: list, lang: str) -> str:
    text = ""
    for token in tokens:
        if (
            (
                len(token["cmd"]) != 0
                and token["cmd"][0] == "if-not"
                and token["cmd"][1] != lang
            )
            or (
                len(token["cmd"]) != 0
                and token["cmd"][0] == "if"
                and token["cmd"][1] == lang
            )
            or len(token["cmd"]) == 0
        ):
            text += "\n".join(token["text"]) + "\n"
    return text


def formatter(description: str, lang: str, limit: int = 80) -> str:
    paragraphs = description.split("\n")
    result = list()
    for para in paragraphs:
        if len(para) > limit:
            words = para.split(" ")
            line = list()
            count = 0
            while len(words) > 0:
                word = words.pop(0)
                if len(word) + count > limit:
                    result.append(" ".join(line))
                    line = list()
                    count = 0
                line.append(word)
                count += len(word) + 1
            result.append(" ".join(line))
        else:
            result.append(para)
    return f'{comment[lang][0]}{"\n".join(result)}{comment[lang][1]}'


def save_new(path: Path, text: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def validate(abs_path, folder, name, extension) -> Path:
    while True:
        path = abs_path / folder / (name + extension)
        if not path.is_file():
            return path
        print_alarm("Файл с подобным именем уже существует.")
        name = input("Введите новое имя: ")
        name = clean_name(name)


def make_path(name: str, lang: str) -> Path:
    abs_path = Path(sys.argv[0]).resolve().parent.parent
    folder, extension = languages.get(lang, ["", ".txt"])
    cleaned_name = clean_name(name)
    path = validate(abs_path, folder, cleaned_name, extension)
    return path


def main(url: str) -> None:
    lang = url.split("/")[-1]
    page = load_page(url)
    challenge_name, description = get_info(page)
    path = make_path(challenge_name, lang)
    tokens = tokenizer(description)
    parsed = parser(tokens, lang)
    formatted = formatter(parsed, lang)
    save_new(path, formatted)


def print_alarm(msg: str) -> None:
    print(f'{"*" * (len(msg) + 4)}\n* {msg} *\n{"*" * (len(msg) + 4)}')


if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except IndexError:
        print_alarm("Необходим полный адрес страницы с заданием на сайте CodeWars!")
    else:
        main(url)
