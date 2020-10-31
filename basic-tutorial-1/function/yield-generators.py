# Yield keyword suspend the execution of function and return a value to its
# caller and again it can be pasue to execute the remaining statement in
# the function

def counter():
    yield 1
    yield 2
    yield 'hello'
    yield 4
    yield 5
    yield 6


# Calling the yield function
values = counter()
# for v in values:
#     print(v)

print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())




