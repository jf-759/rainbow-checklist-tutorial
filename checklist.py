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

def test():
    
    create("purple sox")
    create ("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    # print(read(1))

test()
