# if 3 < 5:  # let's check these options 3 < 5, bool(True), "not empty"
#     print("if block done")
#
# if not 0 == 5:
#     print("second if block done")
#
# print('Finish')
###################################################
# if 3 < 5:
#     print("if block done")
# else:
#     print("else block done")
###################################################
# value = 10
#
# if value > 10 and 1 == 1:
#     value **= 2
#
# elif value > 4 or False: # True or False
#     pass
#
# elif value > (6-1):
#     value -= 1
#
# else:
#     value /= 3
#
#
# print(f"{value=}")
###################################################
# result = int(15/2)
#
# if result == 7:
#     print("usual case")
#
# if (result := int(15/2)) == 7:
#     print("walrus is cool")
###################################################
# operand = 3
# result = operand ** 0.5 if operand >= 3 else operand ** 2
#
# # equ to
# if operand >= 3:
#     result = operand ** 0.5
# else:
#     result = operand ** 2
#
# print(f"{result=}")
###################################################
# response_code = 200
#
# match response_code:
#     case 200:
#         print("OK")
#
#     case 500:
#         print("Internal Server Error")
#
#     case _:  # default case is recommended
#         print("Default case for all other results")
###################################################
# etalon_code = 200   # try change to other
# response_code = 200  # requests()
#
# match response_code:
#     case 200 if response_code == etalon_code:
#         print("OK")
#
#     case 500:
#         print("Internal Server Error")
#
#     case 418:
#         print("I'm a teapot")
#
#     case 300 | 301 | 302:
#         print("Some 300th responses")
#
#     case _:
#         print("Default case for all other results")
###################################################
# try:
#     result = 1 / 0
#
# except:
#     print("It's broken, sorry...")
#
#
# print("done")
###################################################
# try:
#     result = 1 / 0
#
# except:
#     print("It's too hard for me")
#
# else:
#     print(f"Easy peasy, {result=}")
#
#
# print("done")
###################################################
# try:
#     # 1 run as is
#     # 2 uncomment divider
#     # 3 let's check these options for divider "10.0", int("10.0"), float("10.0")
#     # divider = float("10.0")
#     result = 1 / divider
#
# except ZeroDivisionError:
#     print("You can't dividing on zero")
#
# except NameError:
#     print("Unknown variable")
#
# except (TypeError, ValueError):
#     print("You make me sad")
#
# except Exception as error:  # like else
#     print(f"Unxpectable error - {error}")
#
# else:
#     print(f"Easy peasy, {result=}")
###################################################
# try:
#     result = 1 / 0
#
# except ZeroDivisionError:
#     print("You can't dividing on zero")
#
# except:
#     print("It's too hard for me")
#
# else:
#     print(f"Easy peasy, {result=}")
#
# finally:
#     print("Done")
###################################################
# try:
#     result = 1 / 0
# finally:
#     print("Done")
###################################################
# letter = input("Type the letter ")
#
#
# if letter in "abc":
#     error_message = "ALARM!!!"
#     raise Exception(error_message)
#
#
# print("All right")
###################################################
number = float(input("Give me the number: "))

if number < 0:
    result = number * -1

elif 0 > number > 1:
    result = number ** 0.5


else:
    result = number * 2 if number < 100 else number % 100

    try:
        result = 100 / number

        if result % 2 == 1:
            result += 1

        match result:
            case 10 | 15 | 20:
                result /= 2
            case _:
                pass

    except ZeroDivisionError:
        print("You have no power here")
