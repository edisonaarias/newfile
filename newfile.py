# pet_name = "Denali"
# hair_color = "black"

# if(pet_name == "lambeau"):
#     print('Best pet name ever!')
#     if (hair_color == "black" or hair_color == "brown"):
#         print("Beautiful looking dog")
# elif(pet_name == "Denali"):
#     print("she is a yellow lab")
# elif(pet_name == "Rocky"):
#     print("Super cool name!")
# else:
#     print("That is not the name of one of my pets")


# while loop 

#age = 10 
#cant_drive = True

#while cant_drive is True:
    #if age == 16:
        #cant_drive = False
        #print("The wait is over! I can drive!")
    #else:
        #age += 1

# for loop 
# best_football_team = "packers"

#print(best_football_team[2])

# for character in best_football_team:
#     if(character == 'c'):
#         continue
#     print(character)

# def add_two_numbers(number_one, number_two):
#     result = number_one + number_two
#     return result

# result_from_function = add_two_numbers(300, 200)
# print(result_from_function)

# def add_names(first_name, last_name):
#     result = first_name + last_name
#     return result 

# result_from_second_function = add_names("edison", "arias")
# print(result_from_second_function)

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# num = int(input('Enter a number:'))

# if num%2 == 0:
#     print('Even number')
# else:
#     print('Odd number')
    
# my_dict = {
#     'name': 'Tim', 
#     'name': 'John',
#     'nationality': 'South African',
#     'age': 87,
#     'is_tall': True,
#     'Qualification': 'College',
#     'friends': ['Peter', 'Paul', 'Precious']
# }
# x = my_dict['name']
# print(x)

my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
for lists in my_list:
    for row in lists:
        print(row)