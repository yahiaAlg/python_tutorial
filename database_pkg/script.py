from .database_utility import *
# MAIN PROGRAM
if __name__ == "__main__":
    print("this is the "+__name__+" script\n")
    print("welcome".center(20, "*"))
    print("create user".center(20, "*"))
    create_user("yahia2001@gmail.com", "system", "yahia")
    create_user("omar@gmail.com", "system2001", "omar")

    print("before updating user".center(20, "*"))
    pprint(user_datababse)
    print("after updating user".center(20, "*"))
    update_user_info("yahia", "yahia@hotmail", "yahia2001")
