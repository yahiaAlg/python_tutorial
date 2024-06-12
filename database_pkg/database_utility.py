# IMPORTS

from pprint import pprint

# GLOBAL VARIABLES
user_datababse = [
    ("ahmed", "ahmed@gmail", "ahmed123"),
    ("aymen", "aymen@gmail", "aymen123"),
    ("yahia", "yahia@gmail", "yahia123"),
    ("meriem", "meriem@gmail", "meriem123"),
    ("nesrine", "nesrine@gmail", "nesrine123"),
]

# STRUCTURES
user_datababse_dict = {user[0]: {"password": user[2], "email": user[1]} for user in user_datababse}
# FUNCTIONS DEFINITIONS
def create_user(email:str, password:str, username:str="guest")->None:
    """
    create a new user if it not found in the database and will notify with a message if the username is already registered 
    
    Keyword arguments:
        email (str, required) -- user email which is about to be registered in the new tuple,
        password (str, required) -- the password for the registered,
        username (str, optional) -- the new user name to be given Defaults to "guest"
    Return: None
    """
    

    user = user_datababse_dict.get(username, "")
    if user:
        print(f"username {username} is already taken !")
    else:
        user = (username, email, password)
        user_datababse.append(user)
        pprint(user_datababse)

def update_user_info(username:str, email:str="", password:str="")->None:
    if username.isalpha():
        user = user_datababse_dict.get(username, "")
        if user:
            if email and password:
                updated_user = (username, email, password)
            elif not email:
                updated_user = (username, user.get("email"), password)
            elif not password:
                updated_user = (username, email, user.get("password"))
            else:
                updated_user = (username, user.get("email"), user.get("password"))

            # find the row of the user by index
            for i in range(len(user_datababse)):
                if username == user_datababse[i][0]:
                    break
            user_datababse[i]=updated_user
            pprint(user_datababse)

        else:
            print(f"user {username} is not in the database to be updated")
    else:
        print("give a valid username")


print("this is the " + __name__ + " script\n")
