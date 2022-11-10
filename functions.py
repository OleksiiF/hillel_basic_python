# def zero_func():
#     print("my_zero_func_result")
#
#
# result = zero_func()
#########################################################
# def first_func():
#     return "my_first_func_result"
#
#
# first_func_result = first_func()
# print(f"{first_func_result=}")
#
#
# first_func_obj = first_func  # TODO 3, 'sdf'
# print(f"{first_func_obj=}, {type(first_func_obj)=}, {id(first_func_obj)=}")
# print(f"{first_func=}, {type(first_func)=}, {id(first_func)=}")
#
# result = first_func_obj()
# print(f"{result=}")
#########################################################
# def send_message(msg):  # good option
#     # send some message here
#     return None
#
#
# def send_message(msg):  # no so good option
#     # send some message here
#      pass
#
#
# result = send_message('some message')
# print(result)
#########################################################
# def add(operand_a, operand_b):
#     return operand_a + operand_b
#
#
# sum_result = add(13, 5)
# print(f"{sum_result=}")
#
#
# sum_result_1 = add(-4, 18)
# print(f"{sum_result_1=}")
#########################################################
# def multiply(operand_a, operand_b):
#     return operand_a * operand_b
#
#
# multiply_result = multiply(operand_a=3, operand_b=2)
# print(f"{multiply_result=}")
#
#
# multiply_result_1 = multiply(operand_b=-3, operand_a=5.5)
# print(f"{multiply_result_1=}")
#########################################################
# def super_add(operand_a, operand_b, operand_c, operand_d, operand_e):
#     return operand_a + operand_b + operand_c + operand_d + operand_e
#
#
# super_add_result = super_add(
#     3,  # operand_a
#     2,  # operand_b
#     operand_d=4,
#     operand_c=31,  # you can't use just 31 here
#     operand_e=12,  # you can't use just 12 here
# )
# print(f"{super_add_result=}")
#
# super_add_result_1 = super_add(
#     -3,  # operand_a
#     12,  # operand_b
#     3.1,  # operand_c
#     operand_d=4,
#     operand_e=1,  # you can't use just 1 here
# )
# print(f"{super_add_result_1=}")
#########################################################
# def get_slice(string, start, stop, step):
#     return string[start:stop:step]
#
#
# slice = get_slice("string for slice", 5, 10)  # will be exception
#########################################################
# def get_slice(string, start, stop, step=1):
#     return string[start:stop:step]
#
#
# slice = get_slice("string for slice", 5, 10)
# print(f"{slice=}")
#########################################################
# def get_slice(string, start, stop=1, step=1):
#     return string[start:stop:step]
#
#
# is not right --> def get_slice(string, start, stop=1, step):
#########################################################
# def my_unlimited_add(a, b, *args, **kwargs):
#     if args:
#         print(f"Extra position arguments {type(args)=}, {args=}")
#
#     if kwargs:
#         print(f"Extra keyword arguments {type(kwargs)=}, {kwargs=}")
#
#     usual_sum = a + b
#     print(f"{usual_sum=}")
#
#     return usual_sum + sum(args) + sum(kwargs.values())
#
#
# result_add_unlim = my_unlimited_add(1, 2, 3, 4, 5, c=4, d=18, e=34)
# print(f"{result_add_unlim=}")
#########################################################
# def some_only_position_args(a, b, /, c):
#     return a + b + c
#
#
# some_only_position_args(10, 21, -3)  # correct
# some_only_position_args(10, 21, c=-3)  # correct
#
# some_only_position_args(10, b=21, c=-3)  # will rise exception
# some_only_position_args(a=10, b=21, c=-3)  # will rise exception
#########################################################
# def some_only_keyword_args(a, *, b, c):
#     return a ** b / c
#
#
# some_only_keyword_args(-3.5, b=4, c=18)  # correct
# some_only_keyword_args(a=-3.5, b=4, c=18)  # correct
#
# some_only_keyword_args(-3.5, 4, c=18)  # will rise exception
# some_only_keyword_args(-3.5, 4, 18)  # will rise exception
#########################################################
# def both_kind_args(a, b, /, c, d=18, *, e, f):
#     return sum([a, b, c, d, e, f])
#
#
# both_kind_args(1, 2, 3, 4, e=5, f=6)
#########################################################
# first_word = "Hi"
#
#
# def get_message(name):
#     second_word = name.capitalize()
#     result = f"{first_word}, {second_word}"
#
#     return result
#
#
# msg: str = get_message("John")
# print(f"{msg=}")
#
# try:
#     print(f"{name=}")
# except NameError as error:
#     print(error)
#
# try:
#     print(f"{result=}")
# except NameError as error:
#     print(error)
#########################################################
# word = "GLOBAL"
#
#
# def new_word():
#     word = "LOCAL"
#     print(f"Cool word is {word}")
#
#
# new_word()
# print(f"{word=}")
#########################################################
# name = "Robbert"
# print(f"Initial name - {name}")
#
#
# def greetings():
#     global name
#     name = "Artur"
#     print(f"Hello {name}")
#
#
# def congratulations():
#     print(f"Congratulate {name}")
#
#
# greetings()
# print(f"Name after greetings - {name}")
#
# congratulations()
# print(f"Name after congratulations - {name}")
#########################################################
# def grandfather():
#     number = 1
#
#     def father():
#         number = 2  # it will be changed
#
#         def son():
#             nonlocal number
#             number = 3
#
#             def grand_son():
#                 number = 4
#                 print(f"grand_son's {number=}")
#
#             grand_son()
#             print(f"son's {number=}")
#
#         son()
#         print(f"father's {number=}")
#
#     father()
#     print(f"grandfather's {number=}")
#
#
# grandfather()
#########################################################
# sequence = [1, 2, 3, 4]
#
#
# def modify(seq: list):
#     seq.append("New element")
#
#     return None
#
#
# modify(sequence)
# print(f"{sequence=}")
