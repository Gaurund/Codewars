

def decode(s):
    code = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? ="
    result = ""
    for index, letter in enumerate(list(s)):
        if letter in code:
            p = code.index(letter)+1
            for i in range(index + 1):
                if p % 2 == 1:
                    p += 67
                p = p // 2
            letter = code[p - 1]
        result += letter
    return result


import codewars_test as test

@test.describe("Sample Test")
def test_group():
    @test.it("Should crack encoded message")
    def test_case2():
        test.assert_equals(decode("atC5kcOuKAr!"), "Hello World!")
        test.assert_equals(decode("bdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqHabdhpF,82QsLir"), "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")