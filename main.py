from generate import generate_password
from pwm_functions import *

def main():
    check_existence()
    

    while True:
        instruction()

        command = input("> ").lower().strip()

        if command == "n" or command == "new":
            condition = True
            while condition:
                add_new_password()
                decision = input("Do you want to save another password(Y/N)? ").lower().strip()
                if decision in ("n", "no"):
                    condition = False

        if command == "v" or command == "view":
            view_password()

        if command == "q" or command == "quit":
            print("BYE!!!")
            break

        if command == "g" or command == "":
            prompt = int(input("How long do you want your password to be? "))
            print("Generated password: ", generate_password(prompt))

    

if __name__ == "__main__" :
    main()
