marks = input()
cash = int(input())

farthing = 0
funt = 0
schilling = 0
pens = 0
if marks=="фартинг":
    farthing= cash
    pens=farthing//4
    farthing%=4
elif marks=="пенс":
    pens= cash

schilling=pens//12
pens%=12
funt=schilling//20
schilling%=20

if (funt>0): print("Фунтов: ",funt)
if (schilling>0): print("Шиллингов: ",schilling)
if (pens>0): print("Пенсов: ",pens)
if (farthing>0): print("Фартингов: ",farthing)
