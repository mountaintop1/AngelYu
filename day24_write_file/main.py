"""Mail Merge Project"""
#TODO: Create a letter using starting_letter.txt

LETTER = """
Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Angela"""
#for each name in invited_names.txt
# FILE_PATH = r'day24_write_file\Input\Names\invited_names.txt'
# with open(r'C:\Users\Olalekan\Desktop\Python\Angela_Yu\day24_write_file\Input\Names\invited_names.txt') as name_file:
#     names = name_file.readlines()
#     for name in names:
#         name = name.strip()
#         new_letter = LETTER.replace("[name]", name)
#         with open(f"C:\\Users\\Olalekan\\Desktop\\Python\\Angela_Yu\\day24_write_file\\Output\\ReadyToSend\\letter_for_{name}.txt", mode="w") as file:
#             file.write(new_letter)

PLACEHOLDER = "[name]"

INVITE_FILE_PATH = r"C:\Users\Olalekan\Desktop\Python\Angela_Yu\day24_write_file\Input\Names\invited_names.txt"
LETTER_FILE_PATH = r"C:\Users\Olalekan\Desktop\Python\Angela_Yu\day24_write_file\Input\Letters\starting_letter.txt"

with open(INVITE_FILE_PATH) as names_file:
    names = names_file.readlines()

with open(LETTER_FILE_PATH) as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"C:\\Users\\Olalekan\\Desktop\\Python\\Angela_Yu\\day24_write_file\\Output\\ReadyToSend\\letter_for_{stripped_name}.txt", mode="w") as file:
            file.write(new_letter)

