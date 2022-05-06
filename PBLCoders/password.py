username = 'Tyler85'

password = 'surfing29'

userInput = input("What is your username?\n (Hint: Tyler85):")

if userInput == username:
    a=input("Password?\n (Hint: surfing29)")   
    if a == password:
        print("Welcome Tyler!")
    else:
        print("Wrong password.")
else:
    print("Wrong username.")