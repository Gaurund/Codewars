def foo(n):
    return lambda a: a + n

five = foo(5)

print(five(1))

