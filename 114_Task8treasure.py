minimal = 0
x = int(input())
y = int(input())
arrOfLocal = [0,0]
move = input()

if x== 0 and y==0:
    print("Никуда не надо")

while move != "стоп":
    steps = int(input())
    minimal += 1
    if move == 'север':
        arrOfLocal[1] += steps
    elif move == "запад":
        arrOfLocal[0] -= steps
    elif move == "юг":
        arrOfLocal[1] -= steps
    elif move == 'восток':
        arrOfLocal[0] += steps

    if x == arrOfLocal[0] and y == arrOfLocal[1]:
        print(minimal)
        break
    move = input()

