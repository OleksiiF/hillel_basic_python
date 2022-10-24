# my_cool_str = "my cool string"
# my_cool_str_1 = 'more letters'
# my_cool_str_2 = '''Is it legal!?!'''
# my_cool_str_3 = """What's going on here?!"""
#
# my_cool_str_4 = str(1)
# my_cool_str_5 = str(5.6)
# my_cool_str_6 = str(True)
# my_cool_str_7 = str(None)
# my_cool_str_8 = str([1, 2, 3])
# print(my_cool_str_4, type(my_cool_str_4))
# print(my_cool_str_5)
# print(my_cool_str_6)
# print(my_cool_str_7, type(my_cool_str_7))
# print(my_cool_str_8)

################################################################
# multiplication = my_cool_str_3 * 2
# print(multiplication)
#
# sum_ = my_cool_str + "" + my_cool_str_2 + " " + my_cool_str_2
# print(sum_)
#
# usual_string = "New line here \n and tabulation \t here"
# print(usual_string)
#
# escaping_characters = "New line here \\n and tabulation \\t here"
# print(escaping_characters)
#
# raw_string = r"New line here \n and tabulation \t here"
# print(raw_string)

################################################################
# format_string = F"Put some value here - {my_cool_str}"
# print(format_string)
#
#
# format_string_2 = f"More magic - {my_cool_str_3}"
# print(format_string_2)

# There is not only one string formatting method,
# but f-string is modern
################################################################
# username = input("Please tell me your name ")
# print(username, type(username))
# result = f"Hello {username}, nice to e-meet you!"
#
# print(result)


# value_1 = int(5.9)  # removes decimal, doesn't round
# print(value_1, type(value_1))
#
# value_2 = int("3")
# print(value_2, type(value_2))
# #
# #
# value_1 = float("10")
# print(value_1, type(value_1))
#
# value_2 = float("3.7")
# print(value_2, type(value_2))
#
#
# sum_ = value_1 + value_2
# print(sum_, type(sum_))
#
#
# subtraction = value_1 - value_2
# print(subtraction, type(subtraction))
#
#
# exponentiation = value_2 ** 3
# print(exponentiation, type(exponentiation))
#
#
# square_root= value_2 ** 0.5
# print(square_root, type(square_root))
#
# division = value_1 / value_2  # if int or float are possible, the float will be used
# print(division, type(division))


# division_remainder = 9 % 2
# print(division_remainder, type(division_remainder))
#
# division_remainder_negative = -7 % 3  # MATH MEANING
# print(division_remainder_negative, type(division_remainder_negative))

# print(value_1, value_2)
# division_int = value_1 // value_2
# print(division_int, type(division_int))


# division_int_negative = -20 // 3  # MATH MEANING
# print(division_int_negative, type(division_int_negative))


# same_value = 30
# same_value += 1  # same_value = same_value + 1
# print(same_value)
#
# same_value -= 2  # same_value = same_value - 3
# print(same_value)
#
# same_value *= 3  # same_value = same_value * 3
# print(same_value)
#
# same_value /= 4  # same_value = same_value / 4
# print(same_value)
#
# same_value **= 5  # same_value = same_value ** 5
# print(same_value)
#
# same_value %= 6  # same_value = same_value % 6
# print(same_value)
#
# same_value //= 7  # same_value = same_value // 7
# print(same_value)

# str_value = "some cool string"
# print("index 0", str_value[0])
# print("index 4", str_value[4])
#
# str_index = 3
# print("index 3", str_value[str_index])
#
# last_symbol = -1
# print("last symbol", str_value[last_symbol])
# print("will rise exception", str_value[1000])  # will rise IndexError
################################################################
str_for_slice = "wegetfamiliar with index and slices"

# print("slice between 3 and 7 --> ", str_for_slice[3:7])
# print("slice between 3 and -1 --> ", str_for_slice[3:-1])
# print("slice between -10 and -2 --> ", str_for_slice[-10:-2])
#
# print("slice between -10 and till the end --> ", str_for_slice[-10:])
# print("slice start and till 6 --> ", str_for_slice[:6])
# print("copy of the string --> ", str_for_slice[:])
#
# print("end of the slice out of string --> ", str_for_slice[10:200])
# print("slice out of string --> ", str_for_slice[100:200])

print("slice with step 2 --> ", str_for_slice[2:10:2])  # start stop step
print("straight string --> ", str_for_slice[::])  # step 1 by default
print("reversed string --> ", str_for_slice[::-1])
print("reversed substring -->", str_for_slice [:-10:-1])


new_string = "my tesT strINg with \n special NON printable Symbols for string methods"
# print("length of string --> ", len(new_string))
#
# print("swap the case --> ", new_string.replace("i", "24333"))

# print("is a string made of digit --> ", new_string.isdigit())
# print("is a string made of letters --> ", new_string.isalpha())
# print("is a string made of digits or letters --> ", new_string.isalnum())
# print("is there suffix --> ", new_string.endswith("and slices"))
# print("swap the case --> ", new_string.swapcase())
# print("symbol to int--> ", ord("@"))
# print("int to character --> ", chr(123))