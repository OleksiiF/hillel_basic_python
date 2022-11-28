# class MyEmptyClass:  # class itself
#     """
#     Represents empty without data or functionality
#     """
#     pass
#
#
# empty_obj = MyEmptyClass()  # object of class
#
# print(f"{type(empty_obj)=}, {empty_obj=}")
# print(f"{dir(empty_obj)=}")  # don't look to the __double_undescors__
#
#######################################################################
# class Animal:
#     population: int = 30  # attribute of the class
#
#
# animal = Animal()
#
# print(f"{dir(animal)=}")
# print(f"{animal.population=}")
#######################################################################
# class Animal:
#     population: int = 30
#
#
# animal = Animal()
# print(f"{animal.population=} object attr before change")
#
# animal.population = 40  # change attribute of the object of class
# print(f"{animal.population=} object attr after change")
# print(f"{Animal.population=} after object attr was changed")
#
# animal_1 = Animal()
# print(f"{animal_1.population=} new object with class attr")
# Animal.population = 50  # change attribute of the class
# print(f"Animal.population was changed, now it {Animal.population}")
#
# animal_2 = Animal()
# print(f"{animal_2.population=} after new class attr")  # the object has new attribute from class
#
# # the existing object doesn't change, because the object attr was setup explicitly
# print(f"{animal.population=} after new class attr")
#
# # the existing object change, because the object attr wasn't setup
# print(f"{animal_1.population=} after new class attr")
#######################################################################
# class Animal:
#     population: int = 30
#
#
# standalone_animal = Animal()
# print(f"{dir(standalone_animal)=}")
#
# standalone_animal.super_power = "BARK"
# print(f"{dir(standalone_animal)=}")
# print(f"{standalone_animal.super_power=}")
#
# standalone_animal_1 = Animal()
# try:
#     standalone_animal_1.super_power
# except AttributeError:
#     print("You have no power here!")
#######################################################################
# class Animal:
#     population: int = 30
#
#     def get_population(self) -> int:  # method of the class
#         return self.population
#
#
# animal = Animal()
# print(f"{dir(animal)=}")
#
# animal_population = animal.get_population()
# print(f"{animal_population=}")
#######################################################################
# class Animal:
#     population: int = 30
#
#     def __init__(self, species_name: str, animal_name: str):
#         self.species: str = species_name
#         self.animal_name: str = animal_name
#         Animal.population += 1
#
#     def get_population(self) -> int:
#         return self.population
#
#     def print_animal_report(self) -> None:
#         print(f"{self.animal_name}, {self.species}")
#
#
# lion = Animal(species_name="lion", animal_name="Simba")  # __init__ work here
# # print(f"{dir(lion)=}")
#
# animal_population = lion.get_population()
# print(f"{animal_population=} after lion")
#
# crocodile = Animal(species_name="crocodile", animal_name="Dundee")
# # print(f"{dir(crocodile)=}")
#
# animal_population = crocodile.get_population()
# print(f"{animal_population=} after crocodile")
################################################################################
# class Animal:
#     population: int = 30
#
#     def __init__(self, species_name: str, animal_name: str):
#         self.species: str = species_name
#         self.animal_name: str = animal_name
#         Animal.population += 1
#
#     def get_population(self) -> int:
#         return Animal.population
#
#     def print_animal_report(self) -> None:
#         print(f"{self.animal_name}, {self.species}")
#
#     def newborn_animal(self, name: str):
#         return Animal(species_name=self.species, animal_name=name)
#
#     def caught_animal(self) -> None:
#         Animal.population -= 1
#         print(f"{self.animal_name} was caught and moved to the zoo")
#
#
# lion = Animal(species_name="lion", animal_name="Simba")
# animal_population = lion.get_population()
# print(f"{animal_population=} after lion {lion.animal_name}")
#
# crocodile = Animal(species_name="crocodile", animal_name="Dundee")
# animal_population = crocodile.get_population()
# print(f"{animal_population=} after crocodile {crocodile.animal_name}")
#
# new_born_crocodile = crocodile.newborn_animal('Jr. Dundee')
# # equivalent to -> Animal(species_name="crocodile", animal_name='Jr. Dundee')
#
# animal_population = new_born_crocodile.get_population()
# print(f"{animal_population=} after crocodile {new_born_crocodile.animal_name}")
#
# crocodile.caught_animal()
# animal_population = crocodile.get_population()
# print(f"{animal_population=} after crocodile was caught")
# print(f"{Animal.population=}")
################################################################################
# class MyDict:
#     def __init__(self, data: dict):
#         self.data: dict = data
#
#     def __validate(self, obj):
#         if not isinstance(obj, MyDict):
#             raise ValueError("You must provide MyDict instance")
#
#     def __add__(self, second_dict):  # +
#         tmp = self.data.copy()
#         for key, value in second_dict.data.items():
#             if key in tmp:
#                 key = f"{key}_2"
#
#             tmp.update({key: value})
#
#         return MyDict(data=tmp)
#
#
#     def __sub__(self, second_dict):  # -
#         self.__validate(second_dict)
#
#         tmp = self.data.copy()
#         for key, value in second_dict.data.items():
#             if key in tmp:
#                 tmp.pop(key)
#
#         return MyDict(data=tmp)
#
#     def __str__(self):
#         return f"Dictionary content is {self.data}"
#
#     def __repr__(self):
#         return f"{self.data}"
#
#
# my_dict_1 = MyDict({"a": 1, "b": 2, "c": 3})
# my_dict_2 = MyDict({"a": 1, "c": 3})
#
# my_dict_3 = my_dict_1 - my_dict_2
# print(f"{my_dict_3=}")
#
# my_dict_4 = my_dict_1 + my_dict_2
# print(f"{my_dict_4=}")
# print(my_dict_1)