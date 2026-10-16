# ------------------------------------------------------
#        Name: Kathryn Tanaka
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """
        This function checks a user-input string for "dog" or "food"
        Parameters:
            my_answer - user-input string
    """
    my_answer = input("Give me a sentence: ")
    while "dog" not in my_answer or secret_word not in my_answer:
        if "dog" in my_answer:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
        elif secret_word in my_answer:
            print("You used the secret word!")
            break
        else:
            print("Try again")
            my_answer = input("Give me a sentence: ")
            
    
# Task 2
def check_greater():
    """
        This function takes two user-input numbers and checks which is greater than the other. If they are equal, user must enter new numbers
        Parameters:
            a - number 1
            b - number 2
    """
    a=int(input("Give me the first number: "))
    b=int(input("Give me the second number: "))
    while a == b:
        print("Try again")
        a=int(input("Give me the first number: "))
        b=int(input("Give me the second number: "))
    if a > b:
        print("First is Greater")
    elif b > a:
        print("Second is Greater")
        
# Task 3
def get_special_numbers():
    """
        This function prints the numbers between 1 and 41 that are odd, a multiple of 3, and not a multiple of 5

    """
    for i in range(1, 41):
        if (i %2 == 1) and (i %3 == 0) and (i %5 != 0):
            print(i)
            i+=1


# Task 4.a
def my_for_loop():
    """
        This function takes a user-input string, checks if there are 2-5 letters, then lists each letter and if it's a consonant or vowel
        
        Parameters:
            user_str - user-input word
            x - length of the word
    """
    user_str = input("Give me a word: ")
    x=len(user_str)
    if x in range(2,6) and (" " not in user_str):
        for index, letter in enumerate(user_str):
            if letter in ["a", "e", "i", "o", "u"]:
                print(f"{letter} is a vowel")
            else:
                print(f"{letter} is a consonant")
    else:
        print("bad word")
        return

# Task 4.b
def my_while_loop():
    """
    This function gives the user a choice between a, b, or c and gives feedback based on their choice
    
    Paramters:
        a - reprints menu
        b - prints Goodbye
        c - exits
    """
    choice = input("Choose one option: a, b, or c: ")
    while choice != "c":
        if choice == "a":
            choice = input("Choose one option: a, b, or c: ")
        elif choice == "b":
            print("Goodbye")
            return
        else:
            print("try again")
            choice = input("Choose one option: a, b, or c: ")
    if choice == "c":
        exit()

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
