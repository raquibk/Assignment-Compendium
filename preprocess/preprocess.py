# --------------------------------------------
#   Name: Raquib Khan Lavani
#   ID: 1622108
#   CMPUT 274, Fall 2020
#
#   Weekly Exercise #4: Text Preprocessor
# --------------------------------------------

# Importing modules
import string
import sys

# Declaring 'cmd_list' as a global variable
global cmd_list
cmd_list = []
# Splitting command-line argument into elements of cmd_list
for t in sys.argv:
    cmd_list.append("{}".format(t))

# Making a global variable list which includes all the stopwords
global stopwords
stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves",
             "you", "yourselves", "he", "him", "his", "himself",
             "your", "yours", "yourself",
             "she", "her", "hers", "herself",
             "it", "its", "itself", "they", "them",
             "their", "theirs", "themselves",
             "what", "which", "who", "whom", "this",
             "that", "these", "those", "am", "is",
             "are", "was", "were", "be", "been",
             "being", "have", "has", "had",
             "having", "do", "does", "did", "doing",
             "a", "an", "the", "and", "but", "if",
             "or", "because", "as", "until",
             "while", "of", "at", "by", "for", "with",
             "about", "against", "between", "into",
             "through", "during", "before", "after",
             "above", "below", "to", "from", "up",
             "down", "in", "out", "on", "off", "over",
             "under", "again", "further", "then",
             "once", "here", "there", "when", "where",
             "why", "how", "all", "any", "both", "each",
             "few", "more", "most", "other",
             "some", "such", "no", "nor", "not",
             "only", "own", "same", "so", "than",
             "too", "very", "s", "t", "can", "will",
             "just", "don", "should", "now"]

# Making a global variable list which includes all the alphanumeric charecters
global alphanumeric
alphanumeric = list(string.ascii_lowercase + '0123456789')


def keep_none():
    """
    Arguments: None

    Does pre-processing of inputted text in the following steps:
    1. First, the input text turned into lowercase, and is converted
       to a list of elements.
    2. Then, each word is tested for having non Alpha-Numeric Characters.
       If there is such a charecter, the symbol/punctuation is removed,
       and the words (without non-alphanumeric charecters) is appended
       to an output list. Then, the elements of this list are scanned again
       to see if there are any words which have both numbers and letters.
       If such elements do exist, then the numeric characters are removed,
       and the word is replaced to the same word without numeric charecters.
       However, do note that if the element is purely numbers (eg '1998),
       the numeric element is left unchanged.
    3. Then, taking the same list, the function uses list comprehension to
       loop over each word and remove the stopwords from the list,
       while leaving the other elements unchanged.
    4. The output list is then joined into a string, and is
       printed to the terminal.

    Returns: None, but prints the output to the terminal.
    """

    # Taking input as a list with lowercase elements
    input_text = (list((input()).lower().split()))
    output_text = []

    # Testing each word in input, and seeing whether it has a non-
    # Alpha-Numeric Character. Then, removing that charecter and appending
    # the word to an empty list.
    for word in input_text:
        for letter in word:
            if letter not in alphanumeric:
                word = word.replace(letter, '')
        output_text.append(word)

    # Removing numeric characters from words if the word is not purely numeric
    for word in output_text:
        if word.isdigit():
            pass
        elif word.isalpha():
            pass
        else:
            new_word = ''.join([i for i in word if not i.isdigit()])
            output_text[output_text.index(word)] = new_word

    # Removing stopwords
    output_text = [word for word in output_text if word not in stopwords]

    # Removing empty elements
    while '' in output_text:
        output_text.remove('')

    # Convert list to string
    output_text = ' '.join(output_text)
    print(output_text)


# Function which implements preprocessing without removing numeric charecters
def keep_digits():
    """
    Arguments: None

    Does pre-processing of inputted text using the same way
    as mentioned above; However, the function does not modify words
    which have both numbers and letters.

    Returns: None, but prints the output to the terminal.
    """

    # Taking input as a list with lowercase elements
    input_text = (list((input()).lower().split()))

    output_text = []

    # Removing numeric characters from words if the word is not purely numeric
    for word in input_text:
        for letter in word:
            if letter not in alphanumeric:
                word = word.replace(letter, '')
        output_text.append(word)

    # Remove stopwords
    output_text = [word for word in output_text if word not in stopwords]

    # Removing empty elements
    while '' in output_text:
        output_text.remove('')

    # Convert list to string
    output_text = ' '.join(output_text)
    print(output_text)


# Function which implements pre-processing without removing symbols
def keep_symbols():
    """
    Arguments: None

    Does pre-processing of inputted text using the same way as mentioned above;
    However, the function does not modify words with nonalphanumeric characters
    like punctuations, symbols in them.

    Returns: None, but prints the output to the terminal.
    """

    # Taking input as a list with lowercase elements
    input_text = (list((input()).lower().split()))

    output_text = input_text

    # Removing numeric characters from words if the word is not purely numeric
    for word in output_text:
        if word.isdigit():
            pass
        elif word.isalpha():
            pass
        else:
            new_word = ''.join([i for i in word if not i.isdigit()])
            input_text[input_text.index(word)] = new_word

    # Remove stopwords
    input_text = [word for word in input_text if word not in stopwords]
    output_text = input_text

    # Removing empty elements
    while '' in output_text:
        output_text.remove('')

    # Convert list to string
    output_text = ' '.join(output_text)
    print(output_text)


# Function which implements pre-processing without removing stopwords
def keep_stops():
    """
    Arguments: None

    Does pre-processing of inputted text using the same way as mentioned above;
    However, the function does not remove stopwords from the processed list.

    Returns: None, but prints the output to the terminal.
    """

    # Taking input as a list with lowercase elements
    input_text = (list((input()).lower().split()))

    output_text = []

    # Remove non-alphanumeric characters
    for word in input_text:
        for letter in word:
            if letter not in alphanumeric:
                word = word.replace(letter, '')
        output_text.append(word)

    # Removing numeric characters from words if the word is not purely numeric
    for word in output_text:
        if word.isdigit():
            pass
        elif word.isalpha():
            pass
        else:
            new_word = ''.join([i for i in word if not i.isdigit()])
            output_text[output_text.index(word)] = new_word
    # Convert list to string

    # Remove empty elements from list
    while '' in output_text:
        output_text.remove('')

    output_text = ' '.join(output_text)
    print(output_text)


def input_handler():
    """
    Arguments: None

    This function handles the input given by the user as standard input in
    the terminal along with performing error handling.
    - If the user writes 'python3 preprocess.py', it calls the function
      keep_none() which preprocesses the text by removing stopwords,
      removing numbers from a word containing both numbers and letters
      and removing non alphanumeric characters.
    - If the user writes 'python3 preprocess.py keep-digits', it calls
      the function keep_digits() which preprocesses the text in the same way,
      except it does not remove digits.
    - If the user writes 'python3 preprocess.py keep-symbols', it calls the
      function keep_symbols() which preprocesses the text in the same way,
      except it does not remove non alphanumeric characters.
    - If the user writes 'python3 preprocess.py keep-stops', it calls the
      function keep_stops() which preprocesses the text in the same way,
      except it does not remove stopwords.

    ERROR HANDLING

    - If the user inputs a value for the mode other than the ones listed above,
      it prints an error message, specifies the correct format, and exits
      the code immediately.
    - If the user inputs more than one mode, it prints a message specifying
      the user has inputted too many arguments, specifies the correct format,
      and exits the code immediately.
    """

    # If no mode is given, implement full pre-processing
    if len(cmd_list) == 1:
        keep_none()

    # If mode is specified (cmd-argument length will be 2)
    elif len(cmd_list) == 2:
        # If 'keep-digits' is specified, keep numbers
        if cmd_list[1] == 'keep-digits':
            keep_digits()
        # If 'keep-digits' is specified, keep non-alphanumeric charecters
        elif cmd_list[1] == 'keep-symbols':
            keep_symbols()
        # If 'keep-digits' is specified, keep stopwords
        elif cmd_list[1] == 'keep-stops':
            keep_stops()
        # Specifies the correct way to input if the mode specified is
        # not identified
        # Immediately exits the program
        else:
            print("############## ERROR ##############")
            print('The mode name specified is not correct.')
            print('Please input in the following format:')
            print(' ')
            print('python3 preprocess.py <mode>')
            print(' ')
            print('<mode> can be:')
            print('1. "keep_digits"')
            print('2. "keep_stops"')
            print('3. "keep_symbols"')
            print('4. Blank')
            print('###################################')
            sys.exit()
    # If command-line argument is greater than 2,
    # the code specifies the correct
    # format and immediately exits
    else:
        print("############## ERROR ##############")
        print(' ')
        print('There are too many arguments specified.')
        print('Please input in the following format:')
        print(' ')
        print('python3 preprocess.py <mode>')
        print('<mode> can be:')
        print('1. "keep_digits"')
        print('2. "keep_stops"')
        print('3. "keep_symbols"')
        print('4.  Blank')
        print(' ')
        print('###################################')
        sys.exit()


if __name__ == "__main__":
    input_handler()
