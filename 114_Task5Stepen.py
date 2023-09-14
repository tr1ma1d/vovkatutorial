num = float(input())
b = 0

while num != 1:
    if num % 2 != 0:
        print("Net")
        break
    else:
        num //= 2
        b += 1

print(b)