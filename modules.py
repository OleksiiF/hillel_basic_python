# import random
#
#
# print(random.randint(0, 100))
###########################################
# import time as new_time_name
# from random import random, randint as custom_randint
#
#
# print(f"{random()=}")
# print(f"{custom_randint(0, 100)=}")
# print(f"{new_time_name.time()=}")
###########################################
# from functions_two import factorial
#
#
# y=factorial(46)
# print(y)
###########################################
import requests


def get_name():
    print(f"{__name__=} inside function")



if __name__ == '__main__':
    get_name()

