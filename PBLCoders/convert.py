# asks for name and gender

def storyStart(name, gender):
    pronoun = ''
    if gender == 'm':
        pronoun = 'He'
        pronoun1 = "his"
    elif gender == 'f':
        pronoun = 'She'

# prints variable arguments 
    print('One stormy day, ' + name + ' was attempting to mine bitcoin.')
    print(pronoun + ' was desperate to mine, but couldn\'t, the malware overtook ' + pronoun1 + ' computer!' )

userName = input('What is your name? ')
gender = input('Are you male or female (type m or f)? ')


# program
storyStart(userName, gender)


