import math

# STRING METHODS

# name = "johny"
# print(len(name)) - 5
# print(name.find("y")) - 4
# print(name.capitalize()) - Johny
# print(name.upper()) - JOHNY
# print(name.lower()) - (JOHNY - johny)
# print(name.isdigit()) - False
# print(name.isalpha()) - True (jo hny - False)
# print(name.count("j")) - 1
# print(name.replace("j", "b")) - bohny
# print(name*3) - johnyjohnyjohny

# MATH FUNCTIONS

# pi = 3.14
# x = 1
# y = 2
# z = 3
# print(round(pi)) - 3
# print(math.ceil(pi)) - 4
# print(math.floor(pi)) - 3
# print(abs(pi)) - (-3.14 = 3.14)
# print(pow(5,2)) - 25
# print(math.sqrt(144)) - 12.0
# print(max(x,y,z)) - 3
# print(min(x,y,z)) - 1


# LISTS - "магазин" для нескольких предметов в одной переменной

# food = ["pizza", "potato", "hotdog", "spaghetti"]
#
# food[2] = "churos"
# food.append("ice cream")
# food.remove("churos")
# food.pop()
# food.insert(0, "cake")
# food.sort()
# food.clear()
# food.sort()
# print(food[2])
#
# for i in food:
#     print(i)


# 2D LISTS - массив массивов

# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]
#
# food = [drinks, dinner, dessert]
# print(food[1][0])


# TUPLES - кортежи (упорядоченные неизменяемые коллекции, полезны для группировки связанных данных)

# student = ("Bro", 21, "male")
#
# print(student.count("Bro"))
# print(student.index("male"))
#
# for x in student:
#     print(x)
#
# if "Bro" in student:
#     print("Bro is here!")


# SETS - неупорядоченная, неиндексированная коллекция, не допускающая повторяющихся значений

# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}
#
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)
# dinner_table = utensils.union(dishes)
#
# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))
#
# for x in dinner_table:
#     print(x)


# DICTIONARY - (словарь) изменяемый неупорядоченный набор уникальных пар ключ:значение, используют хеширование

# capitals = {"USA":"Washington DC",
#             "India":"New Dehli",
#             "China":"Beijing",
#             "Russia":"Moscow"}
#
# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Las Vegas"})
# capitals.pop("China")
# capitals.clear()

# print(capitals["Russia"])
# print(capitals.get("Germany"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key,value in capitals.items():
#     print(key, value)


# INDEX OPERATOR [] - доступ к элементам последовательности (str, list, tuples)

# name = "bro Code"

# if(name[0].islower()):
#     name = name.capitalize()
# first_name = name[:3].upper()
# last_name = name[4:].lower()
# last_character = name[-1]
#
# print(first_name)
# print(last_name)
# print(last_character)


#SCOPE123