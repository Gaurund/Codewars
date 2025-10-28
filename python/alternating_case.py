"""
altERnaTIng cAsE <=> ALTerNAtiNG CaSe
Define String.prototype.toAlternatingCase (or a similar function/method such as 
to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; 
see the initial solution for details) such that each lowercase letter becomes 
uppercase and each uppercase letter becomes lowercase. 
"""

import codewars_test as test

def to_alternating_case(string):
    return "".join([l.lower() if l.isupper() else l.upper() for l in list(string)] )

@test.describe("Basic tests")
def test_bacics():
    @test.it("should work for fixed tests (provided in the description)")
    def test_fixed():
        test.assert_equals(to_alternating_case("hello world"), "HELLO WORLD")
        test.assert_equals(to_alternating_case("HELLO WORLD"), "hello world")
        test.assert_equals(to_alternating_case("hello WORLD"), "HELLO world")
        test.assert_equals(to_alternating_case("HeLLo WoRLD"), "hEllO wOrld")
        test.assert_equals(to_alternating_case("12345"), "12345")
        test.assert_equals(to_alternating_case("1a2b3c4d5e"), "1A2B3C4D5E")
        test.assert_equals(to_alternating_case("String.prototype.toAlternatingCase"), "sTRING.PROTOTYPE.TOaLTERNATINGcASE")
        test.assert_equals(to_alternating_case(to_alternating_case("Hello World")), "Hello World")
        
        
    @test.it("should work for the title of this Kata")
    def test_title():
        title = "altERnaTIng cAsE"
        title = to_alternating_case(title)
        test.assert_equals(title, "ALTerNAtiNG CaSe")
        title = to_alternating_case(title)
        test.assert_equals(title, "altERnaTIng cAsE")
        title = to_alternating_case(title)
        test.assert_equals(title, "ALTerNAtiNG CaSe")
        title = to_alternating_case(title)
        test.assert_equals(title, "altERnaTIng cAsE")
        title = "altERnaTIng cAsE <=> ALTerNAtiNG CaSe"
        title = to_alternating_case(title)
        test.assert_equals(title, "ALTerNAtiNG CaSe <=> altERnaTIng cAsE")
        title = to_alternating_case(title)
        test.assert_equals(title, "altERnaTIng cAsE <=> ALTerNAtiNG CaSe")
        title = to_alternating_case(title)
        test.assert_equals(title, "ALTerNAtiNG CaSe <=> altERnaTIng cAsE")
        title = to_alternating_case(title)
        test.assert_equals(title, "altERnaTIng cAsE <=> ALTerNAtiNG CaSe")

