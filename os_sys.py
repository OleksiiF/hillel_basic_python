import os
import sys


# list_dir = os.listdir()
# print(f"{list_dir=}")
#
#
# list_dir = os.listdir("../")
# print(f"{list_dir=}")
##########################################################
# first_folder = "first_folder"
# second_folder = "second_folder"
# third_folder = ""
# filename = "filename.txt"
#
# list_dir = os.path.join(first_folder, second_folder, third_folder, filename)
# print(f"{list_dir=}")
#
#
# # example of f-string disadvantages
# separator = "/" or "\"
#
# formated_path = (
#     f"{first_folder}{separator}"
#     f"{second_folder}{separator}"
#     f"{third_folder}{separator}{filename}"
# )
# print(f"{formated_path=}")
##########################################################
# script_args = sys.argv
# print(f"{script_args=}, {type(script_args)=}")
# print(f"Script name is {script_args[0]}")
##########################################################
# print("Start")
#
# try:
#     sys.exit(1)
# except SystemExit:
#     print("Exception is captured")
#
# sys.exit(128)
#
# print("END")
##########################################################
# fruits = ["apple", "melon", "orange"]
# print(f"{sys.getsizeof(fruits)=}")