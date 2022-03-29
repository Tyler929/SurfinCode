{% include navigation.html %}

## Python Projects and Challenges

- [Python Files](ttps://github.com/Tyler929/tyler929.github.io)

- [Replit](https://replit.com/@Tyler929/tyler929githubio#.replit)

---

### OOP Factorial
```
class factorial:
    def __init__(self):
        self.factorial = []

    def __call__(self,n):
        if n == 1 or n == 0:
            self.print()
            return 1
        else:
            self.factorial.append(n)
            return n * self(n-1)

    def print(self):
        print("="*30, "\nSequence of Numbers: \n", *self.factorial)

def run_factorial():
    #first test
    n = 12
    facto = factorial()
    result = facto(n)
    print("="*30, "\nThe factorial of", n, "is", result)

    #second test
    n = 15
    facto = factorial()
    result = facto(n)
    print("="*30, "\nThe factorial of", n, "is", result)
```


### OOP LCM
```
# no init like the factorial because of no defined properties

class leastcm:
    def __call__(self, a, b):
        if (a > b):
            maximum = a
        else:
            maximum = b
        while (True):
            if (maximum % a == 0 and maximum % b == 0):
                break
            maximum = maximum + 1
        return maximum

def lcm_run():
    #first test
    a = 3
    b = 5
    lcm = leastcm()
    result = lcm(a,b)
    print("="*60, "\nThe LCM of", a, "and", b, "is", result)

    #second test
    a = 50
    b = 100
    result = lcm(a,b)
    print("="*60, "\nThe LCM of", a, "and", b, "is", result)

    #third test
    a = 5
    b = 7
    result = lcm(a,b)
    print("="*60, "\nThe LCM of", a, "and", b, "is", result)
```

### Factorial
```
def fact(b):
    a = 1
    for i in range(1,b+1):
        a = a * i
    return a
b = 5
number = fact(b)
print("="*30)
print("The Factorial Of 5 Is: ", number)
print("="*30)

```

## Heart

```
## imports
import time
import os

## Sets base color

Color34 = "\u001b[34m"
Color37 = "\u001b[37m"


## Prints heart animation

def heart1():
  print("_____8888888888____________________")
  print("____888888888888888_________________")
  print("__888888822222228888________________")
  print("_88888822222222288888_______________")
  print("888888222222222228888822228888______")
  print("888882222222222222288222222222888___")
  print("8888822222222222222222222222222288__")
  print("_8888822222222222222222222222222_88_")
  print("__88888222222222222222222222222__888")
  print("___888822222222222222222222222___888")
  print("____8888222222222222222222222____888")
  print("_____8888222222222222222222_____888_")
  print("______8882222222222222222_____8888__")
  print("_______888822222222222______888888__")
  print("________8888882222______88888888____")
  print("_________888888_____888888888_______")
  print("__________88888888888888____________")
  print("___________8888888888_______________")
  print("____________8888888_________________")
  print("_____________88888__________________")
  print("______________888___________________")
  print("_______________8____________________")
  print("\u001b[34m -------------------------------------------- \u001b[37m")

def heart2():
  print("  _____8888888888____________________")
  print("  ____888888888888888_________________")
  print("  __888888822222228888________________")
  print("  _88888822222222288888_______________")
  print("  888888222222222228888822228888______")
  print("  888882222222222222288222222222888___")
  print("  8888822222222222222222222222222288__")
  print("  _8888822222222222222222222222222_88_")
  print("  __88888222222222222222222222222__888")
  print("  ___888822222222222222222222222___888")
  print("  ____8888222222222222222222222____888")
  print("  _____8888222222222222222222_____888_")
  print("  ______8882222222222222222_____8888__")
  print("  _______888822222222222______888888__")
  print("  ________8888882222______88888888____")
  print("  _________888888_____888888888_______")
  print("  __________88888888888888____________")
  print("  ___________8888888888_______________")
  print("  ____________8888888_________________")
  print("  _____________88888__________________")
  print("  ______________888___________________")
  print("  _______________8____________________")
  print("\u001b[34m -------------------------------------------- \u001b[37m")

def heart3():
  print("     _____8888888888____________________")
  print("     ____888888888888888_________________")
  print("     __888888822222228888________________")
  print("     _88888822222222288888_______________")
  print("     888888222222222228888822228888______")
  print("     888882222222222222288222222222888___")
  print("     8888822222222222222222222222222288__")
  print("     _8888822222222222222222222222222_88_")
  print("     __88888222222222222222222222222__888")
  print("     ___888822222222222222222222222___888")
  print("     ____8888222222222222222222222____888")
  print("     _____8888222222222222222222_____888_")
  print("     ______8882222222222222222_____8888__")
  print("     _______888822222222222______888888__")
  print("     ________8888882222______88888888____")
  print("     _________888888_____888888888_______")
  print("     __________88888888888888____________")
  print("     ___________8888888888_______________")
  print("     ____________8888888_________________")
  print("     _____________88888__________________")
  print("     ______________888___________________")
  print("     _______________8____________________")
  print("\u001b[34m -------------------------------------------- \u001b[37m")


def heart4():
  print("         _____8888888888____________________")
  print("         ____888888888888888_________________")
  print("         __888888822222228888________________")
  print("         _88888822222222288888_______________")
  print("         888888222222222228888822228888______")
  print("         888882222222222222288222222222888___")
  print("         8888822222222222222222222222222288__")
  print("         _8888822222222222222222222222222_88_")
  print("         __88888222222222222222222222222__888")
  print("         ___888822222222222222222222222___888")
  print("         ____8888222222222222222222222____888")
  print("         _____8888222222222222222222_____888_")
  print("         ______8882222222222222222_____8888__")
  print("         _______888822222222222______888888__")
  print("         ________8888882222______88888888____")
  print("         _________888888_____888888888_______")
  print("         __________88888888888888____________")
  print("         ___________8888888888_______________")
  print("         ____________8888888_________________")
  print("         _____________88888__________________")
  print("         ______________888___________________")
  print("         _______________8____________________")
  print("\u001b[34m -------------------------------------------- \u001b[37m")

def heart5():
  print("               _____8888888888____________________")
  print("               ____888888888888888_________________")
  print("               __888888822222228888________________")
  print("               _88888822222222288888_______________")
  print("               888888222222222228888822228888______")
  print("               888882222222222222288222222222888___")
  print("               8888822222222222222222222222222288__")
  print("               _8888822222222222222222222222222_88_")
  print("               __88888222222222222222222222222__888")
  print("               ___888822222222222222222222222___888")
  print("               ____8888222222222222222222222____888")
  print("               _____8888222222222222222222_____888_")
  print("               ______8882222222222222222_____8888__")
  print("               _______888822222222222______888888__")
  print("               ________8888882222______88888888____")
  print("               _________888888_____888888888_______")
  print("               __________88888888888888____________")
  print("               ___________8888888888_______________")
  print("               ____________8888888_________________")
  print("               _____________88888__________________")
  print("               ______________888___________________")
  print("               _______________8____________________")
  print("\u001b[34m -------------------------------------------- \u001b[37m")


## Timing between each print

os.system("clear")
time.sleep(.1)
heart1()
time.sleep(.5)
os.system("clear")
heart2()
time.sleep(.5)
os.system("clear")
heart3()
time.sleep(.5)
os.system("clear")
heart4()
time.sleep(.5)
os.system("clear")
heart5()
time.sleep(.5)
os.system("clear")
```



### Tree Thing
```
## asks height and character (symbol) then prints tree

def submain():
    top = '💀'
    top_center = top.center(20, " ")
    print(top_center,end='')
    for i in range(10):
        star = '😩' * (2*i)
        center_star = star.center(20, " ")
        print(center_star)
    print('        ||||')
    print('        ||||')
```



### Swap
```
## swaps 2 numbers around

def swap(age1, age2):
    temp = age1
    age1 = age2
    age2 = temp
    print("After Swap",(age1, age2))
number1 = int(input(" Please Enter the First number : "))
number2 = int(input(" Please Enter the Second number : "))
print("Before Swap",(number1, number2))
swap(number1, number2)
```

### Keypad
```
## Creation of menu keypad for inputs.

def keypad():
    print()
    numbers = ['1 2 3','4 5 6','7 8 9','  0  ']
    key_pad = '\n'.join(numbers)
    print(key_pad)
```

### Fibonacci 
```
# Sets fibonacci sequence while printing 1 if 1.
def fibo(a):
    x = 0
    y = 1
    if a == 1:
        print(x) 
    else:
        print(x)
        print(y)
    for i in range(2,a):
        z = x + y
        x = y
        y = z
        print(x+y)
# Any Fibonacci number inputted. for fibo(n) The list of fibo numbers before up to the number chosen.

fibo(21)
```


### InfoDB Loops
```
# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)

# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition
```
 
### InfoDB Lists
```

# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Tyler",
    "LastName": "Hickman",
    "DOB": "September 29",
    "Residence": "San Diego",
    "Email": "tylerhickman29@gmail.com",
    "Favorite_Animals":["Cat","Seal","Panther", "Polar Bear"]
})

InfoDb.append({
    "FirstName": "Nadira",
    "LastName": "Haddach",
    "DOB": "August 16",
    "Residence": "San Diego",
    "Email": "nadira@gmail.com",
    "Favorite_Animals":["Cat","Dog","Shark", "Seal"]
})

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Animals: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Favorite_Animals"]))  # join allows printing a string list with separator
    print()

```




