"""
Your task in this Kata is to emulate text justification in monospace font.
You will be given a single-lined text and the expected justification width.
The longest word will never be greater than this width.

Here are the rules:

Use spaces to fill in the gaps between words.
Each line should contain as many words as possible.
Use '\n' to separate lines.
Last line should not terminate in '\n'
'\n' is not included in the length of a line.
Gaps between words can't differ by more than one space.
Lines should end with a word not a space.
Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
Last line should not be justified, use only one space between words.
Lines with one word do not need gaps ('somelongword\n').
"""

from dataclasses import dataclass
import unittest


class Test(unittest.TestCase):

    def test_justify(self):
        self.maxDiff = None
        self.assertEqual(justify("", 10), "")
        self.assertEqual(justify("123 45 6", 7), "123  45\n6")
        text = """\
Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor."""

        self.assertEqual(justify(" ".join(text.split()), 30), text)


class Word:
    def __init__(self, word):
        self.vol: str = word
        self.length: int = len(word)
        self.space: int = 0

    def render(self):
        return f"{self.vol + " " * self.space}"


class String:
    def __init__(self, width) -> None:
        self.words: list[Word] = list()
        self.gaps: int = -1
        self.length: int = 0
        self.width: int = width
        self.islast: bool = True

    def append(self, word: Word) -> None:
        if self.length + word.length + self.gaps < self.width:
            self.words.append(word)
            self.length += word.length
            self.gaps += 1
        else:
            raise Exception("String length exceeded.")

    def render(self) -> str:
        output = ""
        if self.gaps > 0:
            self.insert_spaces()
        for w in self.words:
            output += w.render()
        if not self.islast:
            output += "\n"
        return output

    def insert_spaces(self):
        spaces = self.width - self.length
        common_spc = spaces // self.gaps
        exceeded_spc_amount = spaces % self.gaps
        if self.islast:
            common_spc = 1
            exceeded_spc_amount = 0
        for i in range(exceeded_spc_amount):
            self.words[i].space += common_spc + 1
        for i in range(exceeded_spc_amount, self.gaps):
            self.words[i].space += common_spc


class Text:
    def __init__(self, text, width) -> None:
        self.width = width
        self.text = text.split(" ")
        self.words = list()
        self.strings = list()

        if len(self.text) > 1:
            self.split()
            self.fill_strings()

    def split(self) -> None:
        for w in self.text:
            self.words.append(Word(w))

    def fill_strings(self) -> None:
        string = String(width=self.width)
        for w in self.words:
            try:
                string.append(w)
            except:
                string.islast = False
                self.strings.append(string)
                string = String(width=self.width)
                string.append(w)
        self.strings.append(string)

    def render(self):
        output = ""
        for string in self.strings:
            output += string.render()
        return output


def justify(text, width) -> str:
    text = Text(text=text, width=width)
    return text.render()


unittest.main()
