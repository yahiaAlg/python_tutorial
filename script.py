#!python
import os
from pprint import pprint


print(os.getcwd())
example_sample = os.path.join("usr", "bin", "env", "python3")
print(example_sample)
os.chdir("./geometry")

print("after changing the directory:")
print(os.getcwd())
new_dir = os.path.join(".", "tree_folder", "subfolder")
print(new_dir)
os.chdir("../")
# os.makedirs(new_dir)
print(os.path.sep)

example_sample = r"C:\Users\Yahia\Desktop\python_basics\tutorials\script.py"
print(example_sample)
filename = os.path.basename(example_sample)
base_dir = os.path.dirname(example_sample)

print("filename is :", filename)
print("base_dir is :", base_dir)
print("is it a base directory?: ", os.path.isdir(base_dir))
print("is it a base filename?: ", os.path.isfile(filename))

path_info = os.path.split(example_sample)
print(path_info)
print("the size is ", os.path.getsize(example_sample))

# pprint(os.listdir())

# for path in os.listdir():
#     if path.endswith(".py"):
#         file = open(path, "rt")
#         file_content = file.read()
#         print(path.center(50, "-"))
#         pprint(file_content)
#         file.close()

# TEXT_FILE_NUMBERS = 4
# for i in range(1, TEXT_FILE_NUMBERS):
#     filename = "text_file_v2_0" + str(i) + ".txt"

#     file = open(filename, "w")
#     file.write("")
#     print(f" created successfully {filename} ".center(50, "*"))
#     file.close()

print(
    os.path.exists(
        r"C:\Users\Yahia\Desktop\python_basics\tutorials\text_file_v2_01.txt"
    )
)
print(
    os.path.exists(
        r"C:\Users\Yahia\Desktop\python_basics\tutorials\text_file_v3_01.txt"
    )
)


users = [
    {
        "name": "yahia",
        "age": 19,
        "email": "yahia@gmail.com",
        "address": {"city": "setif", "street": "cite 1014 logts"},
    },
    {
        "name": "oussama",
        "age": 23,
        "email": "oussama@gmail.com",
        "address": {"city": "setif", "street": "cite 240 logement"},
    },
]


import json

# pprint(users)
with open("users.json", "w") as jsondb:  # second method for opening files
    json.dump(users, jsondb)
    print("created the database successfully")


with open("users.json", "r") as usersdb:
    users2 = json.load(usersdb)

    pprint(users2[0]["address"]["street"])

import shutil

# os.makedirs("./backup")
shutil.copyfile("users.json", "./backup/users_bk.json")
print("copy of the database success!")
if os.path.exists("./backup") and os.path.exists("users.json"):
    # shutil.rmtree("./backup")  # equal to rm -r <path>
    os.unlink("users.json")  # rm <path>

import zipfile


print(os.path.relpath(example_sample))
print(os.path.abspath("./script.py"))

backup_zip_obj = zipfile.ZipFile("backup.zip")

for file_in_zip in backup_zip_obj.namelist():
    bk_info_zip = backup_zip_obj.getinfo(file_in_zip)
    print(
        f"{file_in_zip}: compress_size: {bk_info_zip.compress_size} original_size:{bk_info_zip.file_size}"
    )


backup_zip_obj.extract("backup/users_bk.json", "./backup2")
