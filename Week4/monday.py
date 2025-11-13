# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0

t = []
for i in range(3):
    t.append([])
    for j in range(3,0,-1):
        t[i].append(j)

eg = [1,2,3,4,5]

for i in range(int(len(eg)/2)):
    temp = eg[i]
    eg[i] = eg[-i-1]
    eg[-i-1] = temp

print(eg)
# for i in range(len(t)):
#     for j in range(len(t[i])):
#         print(t[i][j], end=" ")
#     print()


# for i in range(3):
#     s += t[i][i]
# print(s)

def display_list(the_list):
    for i in range(len(the_list)):
        print(the_list[i])

new_list = []
while(True):
    print("1. Add")
    print("2. Display")
    option = input("Select option:")
    print(option)
    if option in [1,"Add"]:
        new_list.append(input("Thing to add to list"))
    elif option == 2:
        display_list(new_list)
    else:
        print("Invalid input")

string = "Hello"
for i in range(len(string)):
    print(string[i], end = " ")

