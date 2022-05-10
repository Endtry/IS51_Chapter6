

import util
# util.help()
# my_tuple = (2,3,1)
# list(my_tuple).sort()
# print("my_sorted_tuple_converted_to_list: ", list)
# x = 23
# print(x.endswith(3))
# x = "23"
# print(x.endswith("3"))
# infile = open("Textese.txt", "r")
# my_list = [1, 2, 3, 50, 99]
# not_exist = my_list[9]

key_pairs = {
    "a": "alpha",
    "b": "bravo",
    # "c": "charlie"
}


# word = key_pairs["c"]

# print("word ===> ", word)
# none = None
# nill = none
# y = "2,3,4".split(",") # ["2,3,4"], ["2", "3", "4"]
# x = len(y)

# print(x)


# print(6/"2")


# a = "a"
# a = "19"
# print(int(a))

# print(1/0)

prompt = "Enter number of dependents: "

try:
    num_dependents = int(input(prompt))
    print("num_dependents", num_dependents)
except ValueError as err:
    print("WARNING FOR DEVELOPERS ONLY: ", err)
    print("Please specify a number value for dependents!")
except FileNotFoundError as err:
    print("WARNING FOR DEVELOPERS ONLY: ", err)
    print("Please specify a number value for dependents!")
except IndexError as err:
    print("WARNING FOR DEVELOPERS ONLY: ", err)
    print("Please specify a number value for dependents!")
finally:
    print("ALL DONE")