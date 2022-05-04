

print('Welcome to Python Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What is Tyler Hickmans favorite programming language?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: What is Tyler Hickman favorite sport? ')
    if answer.lower()=='surfing':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: What is the name of the most popular crypto currency?')
    if answer.lower()=='bitcoin':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thanks for Playing this small quiz game, you got',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('CYA!')