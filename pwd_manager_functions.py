import os.path

def instruction():
    instruction = """
        /\/\/\ Select one of the following instructions /\/\/\/
            Choose new to add new data
            Choose view to copy previous data
            Choose q or quit to exit
        """
    print(instruction)


def check_existence():
    if os.path.exists('info.txt'):
        pass
    else:
        #file = open('info.txt', 'w')
        file_opener(file_mode='w')
        file.close()


def file_opener(file_mode):
    file = open('info.txt', mode=file_mode)
    return file


def add_new_password():
    # This function will append new password data to the database.
    try:

        file = file_opener(file_mode='a')
   
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
