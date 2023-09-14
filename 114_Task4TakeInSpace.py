count = 0 
mn = float('inf')
mx = float('-inf')
data = input()

while data != '!':
    height = float(data)
    if 150 <= height <= 190:
        count += 1
        if height < mn:
            mn = height
        elif height > mx:
            mx = height
    data = input()

print(count, "\n",mn, mx) 