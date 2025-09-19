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



def justify(text, width) -> str:
    result = ""
    text_arr: list = text.split(" ")
    string = list()
    for word in text_arr:
        string_len = sum([len(w) + 1 for w in string])
        if (string_len + len(word)) > width:
            spaces = width - sum([len(w) for w in string])
            while spaces:
                for i in range(len(string)-1):
                    if spaces > 0:
                        string[i] += " "
                        spaces -= 1
            for w in string:
                result = result + w
            result = result + "\n"
            string = [word]
        else:
            string.append(word)
    for i in range(len(string)-1):
        string[i] += " "
    for w in string:
        result = result + w 

    return result

unittest.main()