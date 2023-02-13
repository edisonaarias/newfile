pet_name = "Denali"
hair_color = "black"

if(pet_name == "lambeau"):
    print('Best pet name ever!')
    if (hair_color == "black" or hair_color == "brown"):
        print("Beautiful looking dog")
elif(pet_name == "Denali"):
    print("she is a yellow lab")
elif(pet_name == "Rocky"):
    print("Super cool name!")
else:
    print("That is not the name of one of my pets")


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
best_football_team = "packers"

#print(best_football_team[2])

for character in best_football_team:
    if(character == 'c'):
        continue
    print(character)

def add_two_numbers(number_one, number_two):
    result = number_one + number_two
    return result

result_from_function = add_two_numbers(300, 200)
print(result_from_function)

def add_names(first_name, last_name):
    result = first_name + last_name
    return result 

result_from_second_function = add_names("edison", "arias")
print(result_from_second_function)
