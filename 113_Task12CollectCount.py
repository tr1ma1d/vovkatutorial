a = input()
(list(a))
b = int(a[0]) + int(a[1])
c = int(a[1]) + int(a[2])

if b > c:
    print(str(b) + str(c))
else:
    print(str(c) + str(b))