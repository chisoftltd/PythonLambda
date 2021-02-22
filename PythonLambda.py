#Python Lambda
x = lambda a : a + 10
print(x(55))
print()

x = lambda a, b : a * b + b / a
print(x(2, 4))

# Why Use Lambda Functions?
# anonymous function
def myfunc1(n):
    return lambda a : a / n

mydivider = myfunc1(1.2)
print(mydivider(3))
print()

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(0.2)
mytripler = myfunc(3.2)

print(mydoubler(1.1))
print(mytripler(11.0))