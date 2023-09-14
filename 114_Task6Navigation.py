
tunnel = int(input())
border = tunnel
steps = 0
count = 0
metr = 0
while metr != 1:
    nav = input()
    if nav.lower() == "вперед":
        count += 1 
        steps = int(input()) 
        if steps == 1:
            metr = 1
        else: print()
        count += 1
        border = border - steps
        
        if(border < 0):
            print("разворот")
            count += 1
        else:
            print()
    elif nav.lower() == "разворот":
        border = tunnel - border
    else:
        metr = 1

print(count)
    
    

  
    