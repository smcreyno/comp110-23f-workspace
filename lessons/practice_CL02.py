a: int = 2
b: int = 6
if a > b:
    print(a-b)
elif b < 10:
    print(b/a)
else:
    print(a+b)
print(b)

x: str = "Hello"
y: int = len(x)
if y % 4 == 1:
    y *= 2
y -= 6
print(y)
print(x[y])