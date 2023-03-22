student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas

data = pandas.read_csv("./day26_nato_phonetic_alp/nato_phonetic_alphabet.csv")
student_data_frame = pandas.DataFrame(data)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
result = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [result[letter] for letter in word]
print(output_list)
