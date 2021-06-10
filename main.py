import os.path

def check_existence():
    if os.path.exists('info.txt'):
        pass
    else:
        file = open('info.txt', 'w')
        file.close()


def append_new():
    # This function will append new password to the text file.
    file = open("info.txt", 'a')

    print()
    print()

    username = input("Please enter the username: ")
    password = input("Please enter the password: ")
    website = input("Please enter the website: ")

    print()
    print()

    usrnm = "Username: " + username + username + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"

    file.write("---------------------------------------------")
    file.write("\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)


def main():
    check_existence()
    append_new()
if __name__ == "__main__" :
    main()
