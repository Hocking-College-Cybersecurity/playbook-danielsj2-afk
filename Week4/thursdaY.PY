
# lists / arrays

my_list = ["oranges", "apples", "pears"]

# remove value = 1

if 5 in my_list:
    my_list.remove(5)
else:
    print("item not in list")

try:
    my_list.remove(5)
except:
    print("item not in list")

print(my_list)

for i, x in enumerate(my_list):
    print(str(i+1) + " : " + x)



# # tuple

# my_tuple = (1,2,3,4)

# # my_tuple[1] = 5

# print(my_tuple[1])

# # dictionary / map

# my_dictionary = { "oranges" : 5, "apples" : 2}

# print(my_dictionary)

# my_dictionary

# print(my_dictionary["oranges"])

# my_dictionary["oranges"] = 2

# my_dictionary.pop("apples")

# print(my_dictionary.get("apples"))

# var = "original string"

# def my_example_function(test_string = "", my_int = 0):
#     """
#     This function prints a phrase
#     Inputs: The test string, an integer
#     Returns: The result string
#     """
#     var = "a new string"

#     print("this is my test string:" + test_string + str(my_int)+"\n")

#     return var, test_string


# modified_var, original_string = my_example_function("example", 5)

# print(modified_var)

# # print(my_example_function("example", 5))

# print(var)

