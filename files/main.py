# filename = 'my_file.txt'

# file = open(filename)
# content = file.read()
# print(content)
# file.close()


'''opening file in python '''
# filename = 'my_file.txt'
# with open(filename, mode='r' ) as file:
#     content = file.read()
#     print(content)

'''writing file in python'''
with open('my_file.txt', mode='w') as file:
    file.write("hi my name is bobby \n i am 12 years old \n i love python ")

with open('my_file.txt', mode='r') as file:
    content = file.read()
    print(content)

with open('my_file.txt', mode='a') as file:
    file.write('\n bobby will be great')

with open('my_file.txt') as file:
    content = file.read()
    print(content)

with open('new_file.txt', mode='w') as file:
    file.write('\n hi my name is bobby \n going through a lot at the moment buy i  \n know God will come through \n Bobby will be great ')

with open('new_file.txt',  mode='r') as file:
    content = file.read()
    print(content)