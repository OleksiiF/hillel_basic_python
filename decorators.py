# def main_decor(func_to_decor):
#     print("Inside start main_decor")
#
#     def warapper():
#         print("Inside start wrapper")
#         func_to_decor()
#         print("Inside end wrapper")
#
#     print("Inside finish main_decor")
#
#     return warapper
#
#
# def main_func():
#     print("Inside main function")
#
#
# # main_func() # usual call
#
# decorated_main_func = main_decor(main_func)
# decorated_main_func()  # decorated call
#
#
# def main_decor(func_to_decor):
#     print("Inside start main_decor")
#
#     def warapper():
#         print("Inside start wrapper")
#         func_to_decor()
#         print("Inside end wrapper")
#
#     print("Inside finish main_decor")
#
#     return warapper
#
#
# def main_func():
#     print("Inside main function")
#
#
# main_func = main_decor(main_func)
# main_func()  # decorated call
# ###########################################################
# def main_decor(func_to_decor):
#     print("Inside start main_decor")
#
#     def warapper():
#         print("Inside start wrapper")
#         func_to_decor()
#         print("Inside end wrapper")
#
#     print("Inside finish main_decor")
#
#     return warapper
#
#
# @main_decor
# def main_func():
#     print("Inside main function")
#
#
# main_func()  # decorated call
###########################################################
# def param_decorator(func_to_decor):
#     print("Inside start main_decor")
#
#     def param_warapper(argument):
#         print("Inside start wrapper")
#         func_to_decor(argument)
#         print("Inside end wrapper")
#
#     print("Inside finish main_decor")
#
#     return param_warapper
#
#
# @param_decorator
# def say_hi(name):
#     print(f"Hello {name}!")
#
#
# say_hi("World")
###########################################################
def decorator_worker(decor_argument_1, decor_argument_2):
    print("let's create a decorator")
    print(
        f"I've got {decor_argument_1=}, "
        f"{decor_argument_2=} inside decorator_worker"
    )

    def param_decorator(func_to_decor):
        print("inside start main_decor")
        print(
            f"I've got {decor_argument_1=}, "
            f"{decor_argument_2=} inside param_decorator"
        )

        def param_warapper(func_argument):
            print("inside start wrapper")
            print(
                f"I've got {decor_argument_1=}, "
                f"{decor_argument_2=}, "
                f"{func_argument=} inside param_warapper"
            )
            func_to_decor(func_argument)
            print("inside end wrapper")

        print("inside finish main_decor")

        return param_warapper

    print("decorator created")

    return param_decorator


# @decorator_worker("letter a", "letter b")  # NB!
def say_hi(name):
    print(f"Hello {name}!")


say_hi("World")  # NB!

# you can uncomment step by step algorithm, comment rows with NB!
# decorator = decorator_worker("letter a", "letter b")
# say_hi = decorator(say_hi)
# say_hi("World")
