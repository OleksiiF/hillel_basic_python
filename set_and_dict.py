# empty_set = set()
# print(f"{type(empty_set)=}, {empty_set=}")
#
# alphabet = set("abcdefghijklmnopqrstuvwxyz")
# print(f"{type(alphabet)=}, {alphabet=}")
#
# el_a, el_b, el_c, *leftover = alphabet
# print(f"{el_a=}, {el_b=}, {el_c=}, {leftover=}, {type(leftover)=}")
#
# for i, letter in enumerate(alphabet):
#     if i % 2 == 0 and letter in "jklmnopq":
#         print(letter)
#################################################################
# different_types = [-3, None, "I'm inside set", True, 4.5]
# print(f"{type(different_types)=}, {different_types=}")
#
# set_inside = {1, True, different_types, None}  # will rise TypeError
#################################################################
# set_a = {1, 3, 5, 7, 9, -1}
# set_b = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
#
# sub_set = set_a.issubset(set_b)
# print(f"{sub_set=}, {id(sub_set)=}")
# print(f"set_a <= set_b --> {set_a <= set_b}")
#################################################################
# super_set = set_a.issuperset(set_b)
#
# print(f"{super_set=}, {id(super_set)=}")
# print(f"set_a >= set_b --> {set_a >= set_b}")
#################################################################
# union = set_a.union(set_b)
#
# print(f"{union=}, {id(union)=}")
# print(f"set_a | set_b --> {set_a | set_b}")
#################################################################
# intersection = set_a.intersection(set_b)
#
# print(f"{intersection=}, {id(intersection)=}")
# print(f"set_a & set_b --> {set_a & set_b}")
#################################################################
# difference = set_a.difference(set_b)
#
# print(f"{difference=}, {id(difference)=}")
# print(f"set_a - set_b --> {set_a - set_b}")
#################################################################
# symmetric_difference = set_a.symmetric_difference(set_b)
#
# print(f"{symmetric_difference=}, {id(symmetric_difference)=}")
# print(f"set_a ^ set_b --> {set_a ^ set_b}")
#################################################################
# mix_set = {"1", "2", "f", "5", "poi", "j", "4", "df"}
# mix_set = {el for el in mix_set if el.isdigit()}
# mix_set_ternary = {el if el.isdigit() else -1 for el in mix_set}
#
# print(f"{mix_set=}")
# print(f"{mix_set_ternary=}")
#################################################################
# element = "dfgdfg"
# print(f"{set_a=}, {id(set_a)=}")
# set_a.add(element)
# print(f"{set_a=}, {id(set_a)=}")
#
# element_two = 'dfgdfg'
# set_a.discard(element)
# print(f"{set_a=}, {id(set_a)=}")
#
# result = set_a.pop()  # NB! RANDOM
# print(f"{result=}")
# print(f"{set_a=}, {id(set_a)=}")
#################################################################
# usual_set = set('qwerty')
# frozen_set = frozenset('qwerty')
#
# minus = usual_set - frozen_set
# print(f"{type(minus)=}, {minus}")
#
# union = usual_set | frozen_set
# print(f"{type(union)=}, {union}")
#
# usual_set.add(1)
# frozen_set.add(1)  # will rise AttributeError
#################################################################
#################################################################
# empty_dict = {}
# empty_dict = dict()
#
# print(f"{type(empty_dict)=}, {empty_dict=}")
#
# alphabet = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }
# print(f"{type(alphabet)=}, {alphabet=}")
#################################################################
# some_dict = {"key": (1,2,3,4,5,6,7,8), "key_1": 2}
# value = some_dict["key"]
# print(f"{value=}")
#
# try:
#     some_dict["unexisting_key"]
# except KeyError:
#     print("Huston, we have a problem here")
#################################################################
# people = [
#     {
#         "name": "Alex",
#         "age": 22,
#         "voted": True,
#         "result": {
#             1: 34.5,
#             2: 3,
#             3: 13,
#             "time": 45
#         }
#     },
#     {
#         "name": "Bob",
#         "age": 45,
#         "voted": False,
#         "result": {
#             1: 0.3,
#             "time": 1
#         }
#     },
# ]
#
# max_result_first_attempt = max([
#     human["result"]["age"]
#     for human in people
# ])
#
# print(max_result_first_attempt)
#################################################################
# etalon_dict = {
#     1: True,
#     "inside_dict": {"some_key": "some_value"}
# }
#
# etalon_dict[2] = False
# print(f"{etalon_dict=}")
#
# etalon_dict["inside_dict"]["new_key"] = "new_value"
# print(f"{etalon_dict=}")
#
# etalon_dict[1] = "replaced_true"
# print(f"{etalon_dict=}")
#################################################################
# default_dict = dict.fromkeys(["key1", "key2", "key3"], "my value")
# print(f"{default_dict=}")
#################################################################
# one_more_dict = {"wind": 0, "temperature": 10}
#
# print(f"{one_more_dict.get('is rain')=}")
# print(f"{one_more_dict.get('is rain', False)=}")
#################################################################
# etalon_dict = {1: [1, 2, 3]}
# other_dict = {1: True, None: False}
#
# etalon_dict.update(other_dict)
#
# print(f"{etalon_dict=}")
#################################################################
# one_more_dict = {"wind": 0, "temperature": 10}
# temperature = one_more_dict.pop("temperature")
#
# print(f"{temperature=}")
# print(f"{one_more_dict=}")
#################################################################
# dict_with_digits = {"zero": 0, "one": 1, "two": 2, "three": 3}
#
# for digit in dict_with_digits.values():
#     print(digit)
#
# print(
#     f"{type(dict_with_digits.values())=},\n"
#     f"{dict_with_digits.values()}"
# )
#################################################################
# dict_with_digits = {"zero": 0, "one": 1, "two": 2, "three": 3}
#
# for key in dict_with_digits.keys():
#     print(key)
#
# print(
#     f"{type(dict_with_digits.keys())=},\n"
#     f"{dict_with_digits.keys()}"
# )
#################################################################
# dict_with_digits = {"zero": 0, "one": 1, "two": 2, "three": 3}
#
# pairs = dict_with_digits.items()
# print(f"{type(pairs)=},\n{pairs=}")
#
# for pair in pairs:
#     print(f"{pair=}, {type(pair)=}")
#
# for key, item in pairs:
#     print(f"{key=}, {item=}")
#################################################################
# generated_dict = {element**2: element for element in range(10)}
# print(f"{generated_dict=}")
#
# generated_dict_1 = {
#     str(key/2): bool(value%3)
#     for key, value in generated_dict.items()
# }
#
# print(f"{generated_dict_1=}")

# for el in range(10):
#
#     if el / 2:  # bool( el / 2)
#         print(el)
#
# print('sdlkjfhdfkljfhjdsfklj', el % 2)

