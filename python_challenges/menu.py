from LoopsListsW2.loops import tester
from ClassyFunctionsW3 import factclass
from ClassyFunctionsW3 import lcmclass
# from ClassyFunctionsW3 import lcm2

# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders

# import submain
# import keypad
# import ship
# import swap
# import heart

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
  
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
  ["Christmas Tree", "python_challenges/submain.py"],
  ["Heart", "python_challenges/rad.py"],
]

sub_menu2 = [
  ["Fibonacci", "LoopsListsW2/fibo.py"],
  ["Factorial", "ClassyFunctionsW3/fact.py"],
  ["OOP Factorial", factclass.run_factorial],
  ["OOP Lcm", lcmclass.lcm_run],
 # ["Imperative Addition", lcm2.addition],
  ["Imperative Math", "ClassyFunctionsW3/lcm2.py"],
  ["Multiplication Table", "PBLCoders/multi.py"],
]


sub_menu3 = [
  ["Keypad", "python_challenges/keypad.py"],
  ["Swap", "python_challenges/swap.py"],
  ["Loops", tester],
  ["Story", "PBLCoders/convert.py"],
  ["Quiz", "PBLCoders/8ball.py"]
]

#patterns_sub_menu = [
 #   ["Patterns", "patterns.py"],
#    ["PreFuncy", "prefuncy.py"],
#    ["Funcy", funcy.ship],
#]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Animations", submenu1])
    menu_list.append(["Math Calculation Functions", submenu2])
    menu_list.append(["Playful Functions", submenu3])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu1():
    title = "Animations" + banner
    buildMenu(title, sub_menu)

def submenu2():
    title = "Math Calculation Fun" + banner
    buildMenu(title, sub_menu2)

def submenu3():
    title = "Playful Functions" + banner
    buildMenu(title, sub_menu3)
  
#def patterns_submenu():
  #  title = "Function Submenu" + banner
  #  buildMenu(title, patterns_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()



# Menu options in print statement
# def print_menu1():
#    print('1 -- Stringy' )
  #  print('2 -- Numby' )
 #   print('3 -- Listy' )
 #   print('4 -- Exit' )
 #   runOptions()


# Menu options as a dictionary
# menu_options = {
 #   1: 'Stringy',
 #   2: 'Numby',
 #   3: 'Listy',
 #   4: 'Exit',
#}

# Print menu options from dictionary key/value pair
#def print_menu2():
 #   for key in menu_options.keys():
 #       print(key, '--', menu_options[key] )
 #   runOptions()

# menu option 1
#def stringy():
#    print('You chose \' 1 -  Stringy\'')

# menu option 2
#def numby():
#    print('You chose \' 2 - Numby\'')

# menu option 3
#def listy():
 #   print('You chose \'3 - Listy\'')


# call functions based on input choice
#def runOptions():
    # infinite loop to accept/process user menu choice
 #   while True:
   #     try:
   #         option = int(input('Enter your choice 1-4: '))
    #        if option == 1:
     #           stringy()
     #       elif option == 2:
      #          numby()
       #     elif option == 3:
      #          listy()
            # Exit menu
       #     elif option == 4:
    #            print('Exiting! Thank you! Good Bye...')
    #            exit() # exit out of the (infinite) while loop
    #        else:
    #            print('Invalid option. Please enter a number between 1 and 4.')
   #     except ValueError:
    #        print('Invalid input. Please enter an integer input.') #

