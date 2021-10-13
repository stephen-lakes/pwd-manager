import os.path


def create_database(database_name):
    '''
    '''
    pass


def instruction():
    instruction = """
        /\/\/\ Select one of the following instructions /\/\/\/
            Choose new to save a new password.
            Choose view to remember previously saved passwords.
            Choose q or quit to exit.
            Choose g to generate a secure password.
            Create database.
        """
    print(instruction)


def check_existence():
    """ Create a database if there is none. """
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
    # Add new data to the database.
    print("\t\t\tFILL THE FORM BELOW\n")
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
