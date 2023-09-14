inputSizeX = int(input())

count = 0
step = int(input())


borderX = inputSizeX - step



exitX = inputSizeX / 2
exitTunnel = ""



while step != 1:
    control = input()
    
    if control.lower() == "вперед" or control.lower() == "вперёд":
        count += 1
        step = int(input())
        count += 1
        borderX = borderX - step
        exitX += 1 
    elif control.lower() == "разворот":
        borderX = inputSizeX - borderX
        exitX *= -1
  
    else:
        step = 1
    
    if exitX < 0:
        exitTunnel = "слева"
    elif exitX > 0:
        exitTunnel = "справа"
    else:
        exitTunnel = "Вам никуда не надо"

    
print()
print(f"{count}\n{exitTunnel} ")
    