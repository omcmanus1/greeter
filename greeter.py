import os
import pickle

### FUNCTIONS ###

def display_title_bar():
    # Clear terminal screen, then print the title bar
    os.system('clear')

    print("\t**********************************************")
    print("\t***  Greeter - Hello old and new friends!  ***")
    print("\t**********************************************")

def get_user_choice():
    # Give the user their options
    print('\nSee a list of your friends: [1]')
    print('\nSubmit a new friend: [2]')
    print('\nQuit: [q]')
    
    return input('What would you like to do?')

def show_names():
    # Shows all names currently in the list
    print('\nHere are the people I know\n')
    for name in names:
        print(name.title())

def get_new_name():
    # Asks the user for a new name and stores it
    new_name = input('\nPlease tell me this person\'s name: ')
    if new_name in names:
        print(f'\n{new_name.title()} is an old friend! Thank you, though.')
    else:    
        names.append(new_name)
        print(f'\nHere we go again. Nice to meet you, {new_name.title()}\n')

def load_names():
    # Loads names from a file, and puts them in the 'names' list
    # Creates an empty list if the file doesn't exist
    try:
        file_object = open('names.pydata', 'rb')
        names = pickle.load(file_object)
        file_object.close()
        return names
    except Exception as e:
        print(e)
        return []

def quit():
    # Dumpts names into a file and prints a quit message
    try:
        file_object = open('names.pydata', 'wb')
        pickle.dump(names, file_object)
        file_object.close()
        print("\nThanks for playing. I will remember these good friends.")
    except Exception as e:
        print("\nThanks for playing. I won't be able to remember these names.")
        print(e)

### MAIN PROGRAM ###

# Set up a loop where users can choose what they want to do
names = load_names()

# Ask what function the user wants
choice = ''
display_title_bar()
while choice != 'q':

    choice = get_user_choice()

    display_title_bar()
    if choice == '1':
        show_names()
    elif choice == '2':
        get_new_name()
    elif choice == 'q':
        quit()
        print('\nFine then, bye.\n')
    else:
        print('\Huh? Try again please.')








