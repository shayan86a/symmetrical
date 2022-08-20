x = input(":")
y = 0
d = -1
c = len(x)
c = c // 2

while c > y:
    if x[y] == x[d]:
        y += 1
        d -= 1
    else:
        break
if c == y:
    print("is symmetrical")
else:
    print("is not symmetrical")
