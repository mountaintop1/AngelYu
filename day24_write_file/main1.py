"""writing to files"""

FILE_PATH = r'C:\Users\Olalekan\Desktop\Python\Angela_Yu\day24_write_file\my_file.txt'

# with open(FILE_PATH, 'a') as file:
#     file.write('\nmy name is Olalekan Adegoke')
#     # content = file.read()
#     # print(content)

with open("Angela_Yu\day24_write_file\my_file.txt") as file:
    content = file.read()
    print(content)


# file = open(file_path, mode='w')
# file = open(file_path)
# content = file.read()
# print(content)
# file.close()
