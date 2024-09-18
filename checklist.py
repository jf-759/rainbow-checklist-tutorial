checklist = list()

# def create(item):
#     checklist.append('Blue')

def create(item):
    checklist.append(item)

# checklist[0]

# def read(index):
#     item = checklist[index]
#     return item

def read(index):
    return checklist[index]

# checklist = ['Blue', 'Orange']
# checklist [1] = 'Cats'
# print(checklist)

def update(index, item):
    checklist [index] = item

# checklist = ['Blue', 'Cats']
# checklist.pop(1)
# print(checklist)

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1

def mark_completed(index):
    checklist[index] = ("{} {}" .format("√", checklist[index]))

def select(function_code):
   
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    elif function_code == "R":
        item_index = user_input("Index Number?")

        read(item_index)

    elif function_code == "P":
        list_all_items()

    else:
        print("Unknown Option")

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def test():
    
    create("purple sox")
    create ("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    
    destroy(1)

    print(read(0))
    # print(read(1))
    
    select("C")

    list_all_items()

    select("R")

    list_all_items()

    user_value = user_input("Please Enter a value:")
    int(user_value)
    print(user_value)
 
test()
