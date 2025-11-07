my_array = [8,9,7,3,5,5,1,2,5]
second_array = [9,8,7,6,5,4]
my_array[3] = 5
print(my_array)
print(my_array[1:3])

print(5 in my_array)

my_array.insert(10, 6)
# my_array.append(second_array)
my_array.remove(5)
print(my_array)
my_array.pop(4)

print(my_array)
# print(my_array[6])

print(my_array + second_array)
# my_array = my_array + second_array

# for x in second_array:
#     my_array.append(x)

print(my_array)

for i in range(len(my_array)):
    print(my_array[i])

# my_array.sort()

print(my_array)

row_0 = [1,2,3,4]
list_2d = [[row_0], ]

table = [[1,2,3,4],
         [5,6,7,8]]

print(table[0][2])

print(table)

for rows in table:
    for x in rows:
        print(x)

