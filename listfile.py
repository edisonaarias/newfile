# creating a list
first_names = ['Mina','Momo','Sana']
print(first_names)

# adding a value
first_names.append('Dahyun')
print(first_names)

# accessing a value
element_at_second_index = first_names [2]
print(element_at_second_index)

# changing a value

first_names [2] = 'Chaeyoung'
print(first_names)

# popping a value 

popped_element = first_names.pop()
print(popped_element)

# removing a value

first_names.remove('Mina')
print(first_names)

# looping over a list

for first_name in first_names:
    print(first_name)

# list fuction example

def deternime_can_drive(list_of_ages):
    amount_of_people = 0
    for age in list_of_ages:
        if age >= 16:
            amount_of_people += 1
    total_amount_of_people = len(list_of_ages)
    print(f'{amount_of_people}/{total_amount_of_people} can drive.')

ages = [16, 34, 13, 45, 12, 56]
deternime_can_drive(ages)