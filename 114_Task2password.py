passwordAunt = False

while passwordAunt != True:
    
    pass1 = input()
    pass2 = input()
    if pass1 == pass2 and len(pass1) > 8 and len(pass2) > 8:
        passwordAunt = True
        print("Вы успешно вошли!")
    else:
        passwordAunt = False
        print("Пароль меньше или не правильный, повторите попытку")

    