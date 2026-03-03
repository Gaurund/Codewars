import sys

def convert(s: str) -> str:
    return s.lower().replace(" ", "_")

print(convert(sys.argv[1]))