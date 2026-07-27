"""
A string is considered to be in title case if each word in the string is either
(a) capitalised (that is, only the first letter of the word is in upper case) or
(b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case,
given an optional list of exceptions (minor words).
The list of minor words will be given as a string with each word separated by a space.
Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.
"""


def title_case(title: str, minor_words: str = "") -> str:
    if title == "":
        return ""
    result = title.lower().split()
    check_list = minor_words.lower().split()
    result[0] = result[0].capitalize()
    for i,e in enumerate(result, start=0):
        if not e in check_list:
            result[i] = e.capitalize()
    return " ".join(result)


print(title_case("a clash of KINGS", "a an BB the of"))
print(title_case("the quick brown fox"))
