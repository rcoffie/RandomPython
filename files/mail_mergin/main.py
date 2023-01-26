filename = 'invited_names.txt'
file2 = "starting_letter.txt"
PLACEHOLDER = "[name]"


# Reading text in file containing names
with open(filename, mode='r') as file:
    ''' reading files in by each line'''
    names = file.readlines()
    # print(names)



# Read letter content create letter for each individual 
with open(file2, mode='r') as letter_file:
    ''' read text in letter content file '''
    letter_content = letter_file.read()
    # print(letter_content)
    ''' looping through names '''
    for name in names:
        # print(name)
        ''' strip names to avoid white spaces '''
        stripped_name = name.strip()
        # print(stripped_name)
        ''' replace the  name variable in the letter with the names that were looped through '''
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        '''' create a letter a text file with the name of each invited users'''
        with open(f'{stripped_name}.txt', mode='w') as completed_letter:
            pass
            # ''' write write invitation in each file created for each user  '''
            completed_letter.write(new_letter)


      