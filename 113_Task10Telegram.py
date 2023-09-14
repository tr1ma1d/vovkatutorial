word = input()
words = len(word)
priceOfWord = words * 40
rub = 0
for i in range(0,words):
    if priceOfWord >= 100:
        rub += 1
        priceOfWord -= 100

print(f"{rub} р. {priceOfWord} коп.")