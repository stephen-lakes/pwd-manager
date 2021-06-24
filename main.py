import os.path


def check_existence():
    if os.path.exists('info.txt'):
        pass
    else:
        #file = open('info.txt', 'w')
        open_file(file_mode='w')
        file.close()


def open_file(file_mode):
    file = open('info.txt', mode=file_mode)
    return file


def append_new():
    # This function will append new password data to the database.
    try:

        file = open_file(file_mode='a')
   
    except:
        print("Oops something went wrong !!!!, please try again")
    
    else:

        username = input("Please enter the username: ")
        email    = input("Please enter the email: ")
        password = input("Please enter the password: ")
        website  = input("Please enter the website: ")

        print()

        usrnm = "Username: " + username + "\n"
        email = "Email   : " + email + "\n"
        pwd   = "Password: " + password + "\n"
        web   = "Website : " + website + "\n"

        file.write("---------------------------------------------")
        file.write("\n")
        file.write(usrnm)
        file.write(email)
        file.write(pwd)
        file.write(web)

    finally:
        file.close()



def view_password():
    file = open('info.txt', 'r')
    for l in file:
        print(l)


def main():
    check_existence()


    while True:
        append_new()

        


if __name__ == "__main__" :
    main()
