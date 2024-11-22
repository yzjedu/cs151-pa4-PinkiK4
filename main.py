# Programmers:  [Krishon]
# Course:  CS151, [Professor Zee]
# Due Date: [11/21/2024]
# Lab Assignment:  [PA 04]
# Problem Statement:  [My program reads files to manipulate and writes new files with new file data]
# Data In: [menu option input, name of file, word to count, and if you want code to continue]
# Data Out:  [word count, average of characters per headline, new headline file, and shortest and longest length]
# Credits: [class notes and class program]
# Input Files: [the input file 'read_file_name' asks user to input the file name and checks to see it it exists before proceeding]

# Import os package into the code
import os

# Name: read_file_name
# Parameters: None
# Return: f_name
# Processes user's input and output's if user's input is invalid
def read_file_name():
    # Stores user's input in variable
    f_name = input("Enter file name: ")
    # While user's input doesn't match a file in program, asks user to input a valid file name
    while not os.path.isfile(f_name):
        f_name = input("File not exist. Enter file name: ")
    return f_name

# Name: read_file
# Parameters: file_name
# Return: headline_list
# Stores data from user-inputted file name into list
def read_file(file_name):
    # Stores an empty list in a variable
    headline_list = []
    try:
        # Opens file with read permissions
        file = open(file_name, "r")
        # For each line in the file, lines split by commas, store it in a variable, and insert line into list
        for line in file:
            row = line.split(',')
            headline_list.append(row)
        return headline_list

    except FileNotFoundError:
        print("File not found.")
        return

# Name: option_count
# Parameters: file_name, user_input
# Return: [NONE]
# Finds the count of user specified word in a file
def option_count(file_name,user_input):
    if user_input == 'S':
        try:
            # Opens file with read permissions and store file lines into variable
            file = open(file_name, "r")
            lines = file.readlines()
            file.close()
            # Stores user input in variable, word_select
            word_select = input('Please enter the want to count: ').strip().lower()
            word_count = 0
            # For each line in variable,lines, add the count of the selected word to variable.
            for line in lines:
                    word_count += line.count(word_select)
            print(f'The word {word_select} appears {word_count} times.')
        except FileNotFoundError:
            print("File not found.")

# Name: option_writeheadline
# Parameters: user_input
# Return: [NONE]
# Creates an user-named file with writing permissions, and stores user-written lines in the file
def option_writeheadline(user_input):
    if user_input == 'W':
        try:
            write_file = input('What do you want to name the file?:')
            # Opens user-named file with write permissions
            file = open(write_file, "w")
            print('Enter the headlines you want to write line by line. Type END to end(case sensitive).')
            # Store whitespace-stripped user input into variable
            line = input().strip()
            # While variable is not 'END', continue writing lines of code
            while line != 'END':
                file.write(line + '\n')
                line = input().strip()
            file.close()
        except FileNotFoundError:
            print("File not found.")

# Name: option_average
# Parameters: file_name, user_input
# Return: [NONE]
# Finds average of character per headline in a file
def option_average(file_name,user_input):
    if user_input == 'A':
        try:
            # Open file with reading permissions
            file = open(file_name, "r")
            lines = file.read()
            file.close()
            # Initialize variables at 0
            total_characters = 0
            total_lines = 0
            # Splits file lines by newlines and stores it in a variable
            new_lines = lines.splitlines()
            # For each line in list, add length of line to variable and line count to variable
            for line in new_lines:
                total_characters += len(line)
                total_lines += 1
            # If number of lines in file are greater than 0, find the average of the characters per headline in the file
            if total_lines > 0:
                average_characters = total_characters / len(new_lines)
                average_characters = round(average_characters)
                print(f'The average number of characters is {average_characters}')
            else:
                print('There are no characters.')
        except FileNotFoundError:
            print("File not found.")

# Name: option_newfile
# Parameters: user_input
# Return: [NONE]
# Reads in a newfile to manipulate when user inputs they want a new file
def option_newfile(user_input):
    if user_input == 'N':
        # Stores read_file_name function into variable and reads user_inputted file into list
        file_name = read_file_name()
        read_file(file_name)
        # Print Menu Options
        print("Specific Word Count-S\nAverage Number of Characters-A\nHeadline Length-L\nNew File-N:\nWriteHeadline-W")
        user_input = input("Please choose an option for how you want to interact with file: ")
        user_input = user_input.upper().strip()
        # Invoke functions
        option_count(file_name, user_input)
        option_average(file_name, user_input)
        option_length(file_name, user_input)
        option_writeheadline(user_input)
        option_newfile(user_input)

# Name: option_length
# Parameters: file_name, user_input
# Return: [NONE]
# Outputs length of longest headline and shortest headline in file
def option_length(file_name, user_input):
    if user_input == 'L':
        try:
            # Opens file with read permissions
            file = open(file_name, "r")
            lines = file.read()
            file.close()
            # Splits lines in file by newspace and storing it in a variable
            new_lines = lines.splitlines()
            longest_line = lines[0]
            # For each line in list, checks if variable is longest line, and assigns line to variable if it's longer
            for line in new_lines:
                if len(line) > len(longest_line):
                    longest_line = line
            print(f'The longest headline by characters: {len(longest_line)}')
            shortest_line = lines[0]
            # For each line in list, checks if variable is longest line, and assigns line to variable if it's longer
            for line in new_lines:
                if len(line) < len(shortest_line):
                    shortest_line = line
            print(f'The shortest headline by characters: {len(shortest_line)}')
        except FileNotFoundError:
            print("File not found.")

# Name: main
# Parameters:
# Return: [NONE]
# Runs main program
def main():
    # Outputs program name and purpose.
    print('Welcome to Headline Fun. The purpose of this code is to analyze headlines in files in various ways.')
    print('-'* 30)
    # Collects user's input and stores it in variable
    play = input('Would you like to have headline fun?: ')
    play = play.lower().strip()
    # While input is invalid, inform user, and recollect user input
    while play != 'yes' and play != 'no':
        print('Please choose an option.')
        play = input('Would you like to have headline fun?: ')
        play = play.lower().strip()
    # While input is not no, collect user-inputted file name and store it in variable.
    while play != 'no':
        file_name = read_file_name()
        read_file(file_name)
        # Output menu options
        print("Specific Word Count-S\nAverage Number of Characters-A\nShortest and Longest Headline-L\nNew File-N:\nWrite Headline-W")
        print('-' * 30)
        # Collects user's input and stores it in variable
        user_input = input("Please choose an option for how you want to interact with file: ")
        user_input = user_input.upper().strip()
        # While user's input is invalid, inform user, and recollect user input
        while user_input != 'S' and user_input != 'A' and user_input != 'L' and user_input != 'N' and user_input != 'W':
            print('Invalid option!')
            user_input = input("Please choose an option for how you want to interact with file: ")
            user_input = user_input.upper().strip()
        # Invoke menu option functions
        option_count(file_name,user_input)
        option_average(file_name,user_input)
        option_length(file_name,user_input)
        option_writeheadline(user_input)
        option_newfile(user_input)
        print('-' * 30)
        # Ask user if they want to play again
        play = input('Would you like to have more headline fun?: ')
    return
main()