# ---------------------------------------------------
# Name: Raquib Khan Lavani
# ID: 1622108
# CMPUT 274 , Fall 2020
#
# Weekly Exercise #1: Password Validator
# ---------------------------------------------------


import random
import string


def validate(password):
    """ Analyzes an input password to determine if it is "Secure",
    "Insecure", or "Invalid" based on the assignment description criteria.

    Arguments:
        password (string): a string of characters
    Returns:
        result (string): either "Secure", "Insecure", or "Invalid".
    """
    pwdlist = list(password)
    a = []
    b = []
    c = []
    charlist = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")

    # Check length
    if len(pwdlist) < 8:
        return 'Invalid'

    # Check invalid characters
    for char in pwdlist:
        if char == '@' or char == ' ' or char == '#':
            return 'Invalid'

    # Check if password has any special charecter
    isspec = bool(any(d in password for d in charlist))

    # Parsing through the password and putting uppercase,
    # lowercase, numeric letters in different lists
    for letter in password:
        if letter.isupper() is True:
            a.append(letter)
        elif letter.islower() is True:
            b.append(letter)
        elif letter.isnumeric() is True:
            c.append(letter)

    # If all conditions are fulfilled, return Secure, else return Insecure
    if any(a) and any(b) and any(c) and isspec is True:
        return 'Secure'
    else:
        return 'Insecure'
    pass


def generate(n):
    """ Generates a password of length n which is guaranteed
    to be Secure according to the given criteria.

    Arguments:
        n (integer): the length of the password to generate, n >= 8.
    Returns:
        secure_password (string): a Secure password of length n.
    """
    charlist = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")
    if n < 8:
        return
    # Creating a linearly spaced list of the given range,
    # then shuffling it for randomness
    x = list(range(0, n))
    random.shuffle(x)
    # Creating a list with all the characters
    masterlist = list(string.ascii_uppercase) + list(string.ascii_lowercase)
    masterlist = masterlist + list(range(0, 10)) + charlist
    plist = list()

    for number in range(n):
        plist.append(random.choice(masterlist))

    # Guaranteeing a secure pwd by replacing a
    # few elements of the already shuffled plist
    # Then choosing random elements of selected lists and replacing it
    plist[x[0]] = random.choice(list(string.ascii_uppercase))
    plist[x[1]] = random.choice(list(string.ascii_lowercase))
    plist[x[2]] = random.choice(list(range(0, 10)))
    plist[x[3]] = random.choice(list("!-$%&'()*+,./:;<=>?_[]^`{|}~"))

    # Concatenating the elements of plist to a string
    secure_password = ''.join(map(str, plist))
    return secure_password
    pass


if __name__ == "__main__":
    pass
