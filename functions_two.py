# def outside():
#     number = 0
#
#     def inside():
#         nonlocal number
#
#         number += 1
#         print(f"{number=}")
#
#     return inside
#
#
# func = outside()  # closure itself, inside func + env of inside func
# func()
# func()
# func()
#########################################################################
# def multiply(operand_a):
#
#     def inside(operand_b):
#         return operand_a * int(input('operand b'))
#
#     return inside
#
#
# closure_func = multiply(5)
#
# print(f"{closure_func(5)=}")
# print(f"{closure_func(6)=}")
# print(f"{closure_func(7)=}")
#########################################################################
# def factorial(n):
#     if n == 0:
#         return 1
#
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5))
#
# x = [
#     1,
#     [
#         3,
#         4,
#         [3,5,6,[0]]
#     ],
#     4,
#     [3],
#     [[[[[[0]]]]]]
# ]
#
# def denested(arg_list):
#     result = []
#     for el in arg_list:
#         if isinstance(el, list):
#             result.extend(denested(el))
#         else:
#             result.append(el)
#
#     return result
#
# print(denested([x, x, x]))
#########################################################################
# message = lambda: print("Hello World")
# message()
#
# square = lambda n: n * n
# print(square(2))
#
# custom_sum = lambda a, b: a + b
# print(custom_sum(3, -5))
#
# sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_sequence = list(map(
#     lambda x: x**2 + sum([el for el in range(x)[::3]]),
#     sequence
# ))
#
#
# print(f"{new_sequence=}")
#########################################################################
# def print_hello(name: str) -> None:
#     print(f"Hello {name}")
#
#
# print_hello('World')
#
#
# def get_sum(operand_a: int or float, operand_b: int or float) -> int or float:
#     return operand_a + operand_b
#
#
# sum_result: int or float = get_sum(3, -4.9)
# print(f"{sum_result=}")
#########################################################################
# def get_multiply(a: int or float, b: int or float, c=0) -> int or float:
#     """
#     Return sum of multiplication of all arguments.
#
#     :param a: arg1
#     :type a: int
#     :param b: arg2
#     :type b: int
#     :param c: arg3, defaults to 0
#     :type c: int, optional
#
#     :raises ValueError: if arg1 is equal to arg2
#
#     :rtype: int
#
#     :return: multiplication of all arguments
#     """
#     if a == b:
#         raise ValueError('arg1 must not be equal to arg2')
#
#     return a * b * c
#########################################################################
