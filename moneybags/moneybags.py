# --------------------------------------------
#   Name: Raquib Khan Lavani
#   ID: 1622108
#   CMPUT 274, Fall 2020
#
#   Weekly Exercise #7: Dr. Moneybags
# --------------------------------------------

from bisect import bisect


def threshold(moneylist):
    '''
    Main function of program which implements the algorithm. Takes in the list
    of money, and returns the threshold value of the elite club.
    Arguments: moneylist - List of 'n' people with 'w' million dollars of money
    obtained from standard input.
    Returns: Returns the threshold value a person needs to get into the club.
    '''
    # Sort the list of people by ascending order
    moneylist.sort()
    # Assigning initial value to 'm', the threshold value of the elite club
    m = 0
    # Assigning boolean value to break out of loop
    done = False
    # Main loop of program. Uses bisect to obtain the value of people having
    # less than or equal to 'm-1' dollars. Subsequently, length of whole list
    # minus the former gives the number of people who have greater than m-1
    # million dollars. This is checked to be greater than or equal to m, which
    # is then incremented. When condition fails, loop is broken and m is set at
    # a value
    while not done:
        if m <= len(moneylist) - bisect(moneylist, m-1):
            m += 1
        else:
            done = True

    # Since 'bisect' returns lesser than or 'equal to', 1 is subtracted to
    # return values purely lesser than 'm' in the loop. If input is
    # empty, returns 0.
    if m > 0:
        return m - 1
    else:
        return 0


def moneybags(n):
    '''
    Function which handles generating the list of 'n' people with 'w'
    million dollars.
    Arguments:  n - Number of applicants to the club (0 <= n <= 100000)
    Returns: moneylist - List describing applicants. Each element is a
                         single integer which is the net worth of a
                         given applicant, in millions of dollars.
                         (0 <= w <= 1000000000)
    '''
    # Initiating empty list which will hold net worth values
    moneylist = []
    # Runs loop 'n' number of times to get net worth of each
    # applicant. Then, appends that networth of applicant to
    # moneylist.
    for i in range(n):
        moneylist.append(int(input()))

    # Returning the list of networths
    return moneylist


def main():
    '''
    Function which calls the two other functions. First it takes in
    'n', the number of applicants. It then passes 'n' as a parameter to
    moneybags(n), which is passed as a paramter to threshold(moneylist).
    Prints final answer (of threshold(moneylist)) on terminal.
    Arguments: None
    Returns: None
    '''
    # Number of applicants
    n = int(input())
    # Passing n into moneybags, which inturn is passed to threshold,
    # giving final value
    print(threshold(moneybags(n)))


if __name__ == "__main__":
    # Calling main() function
    main()
