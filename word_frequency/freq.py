# --------------------------------------------
#   Name: Raquib Khan Lavani
#   ID: 1622018
#   CMPUT 274, Fall 2020
#
#   Weekly Exercise 3: Word Frequency
# --------------------------------------------

# Importing necessary modules
import sys
import os.path

# Declaring 'list' as a global variable
global list
list = []
# Splitting command-line arguments into different elements of list
for t in sys.argv:
        list.append("{}".format(t))


# Creating a function to read the input from a file, and
# store each line as the elements of a list
def input_file():

    global alist

    # Checking if inputted file name exists, and exiting if it does not
    while not os.path.isfile(list[1]):
        print('Filename does not exist')
        print('Please run the program with an existing file.')
        sys.exit()

    # Proceeding if inputted command-line argument is valid
    if len(list) == 2:
        infile = open(list[1], 'r')
        alist = infile.read().splitlines()

    # Exiting program if there are too many command line arguments
    elif len(list) > 2:
        print('There are too many command-line arguments')
        print('Please enter the argument as:')
        print('python3 freq.py <input_file_name>')
        sys.exit()

    # Exiting program if there are too many command line arguments
    elif len(list) < 2:
        print('There are too few command-line arguments')
        print('Please enter the argument as:')
        print('python3 freq.py <input_file_name>')
        sys.exit()

    # Closing the file from which input is taken
    infile.close()


# Creating a function to count frequency of words in the input file
def word_counter():

    # Defining global variable which will be used to calculate word frequency
    global outputlist

    # Assigning the varaibles empty values
    wordlist = []
    wordfreq = []
    outputlist = []
    wordcount = {}

    # Creating a nested list by splitting input file lines to words
    for word in alist:
        wordlist.append(word.split())

    # Flattening the former list to be a single list with string elements
    # This makes a list of all the words in the file, including repeated words
    wordlist = [word for phrases in wordlist for word in phrases]

    # Creating a set which has all unique words in the input file
    uniqset = set(wordlist)
    # Sorting this set alphabetically
    # This ensures that when a dictionary is made later on, the dictionary is
    # sorted alphabetically
    uniqset = sorted(uniqset)

    # Setting initial count of each word as 0 in dictionary
    for word in uniqset:
        wordcount[word] = 0

    # Adding 1 for each instance of a repeated word to the corresponding value
    # in the dictionary
    # Hence, we now have a dictionary with the count of each word
    for x in uniqset:
        for y in wordlist:
            if x == y:
                wordcount[x] += 1

    # Creating a new list which has the frequency of occurence of each word
    for z in uniqset:
        wordfreq.append(str(round(wordcount[z]/len(wordlist), 3)))

    # Creating a frequency table as list by appending to a list the
    # key of dictionary, corresponding value and relative frequency
    for i in range(len(uniqset)):
        outputlist.append(uniqset[i])

    for i in range(len(uniqset)):
        outputlist[i] += ' ' + str(wordcount[uniqset[i]]) + ' ' + wordfreq[i]


# Creating a file which prints frequency table inside a new file
def output_file():

    # Defining the name of the output file
    outname = list[1] + '.out'
    # Opening the le in 'write' format
    outfile = open(outname, "w")

    # Taking each element of a list and printing it to a new line
    # of the output file
    for row in outputlist:
        outfile.write(row + '\n')

    # Closing the output file
    outfile.close()


if __name__ == "__main__":

    # Calling all the functions
    input_file()
    word_counter()
    output_file()

    pass
