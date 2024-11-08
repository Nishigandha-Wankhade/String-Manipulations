"""
-----------------------------------------------------------------------
Assignment 4 Problem 1: To count the number of times a substring matches within another string.
November 03, 2024 
Nishigandha Wankhade 
-----------------------------------------------------------------------
"""

from string import * # to use all possible functions from a string module / library

def countSubstrMatches(srch_str, sub_str):
    """
    Function to count the number of non-overlapping occurrences of a substring within a search string using an iterative approach.
    
    Parameters:
        srch_str (str): The string in which to search.
        sub_str (str): The substring to find within srch_str.
        
    Returns:
        int: The number of times sub_str appears in srch_str.
    """
    count_Itr = 0
    start = 0
    
    while True:
        start = srch_str.find(sub_str, start)
        if start == -1:  # No more occurrences
            break
        count_Itr += 1      # if occurrence found increment the count
        start = start + len(sub_str)  # Move past this match to avoid overlaps

    return count_Itr



def countSubstrRecursive (srch_str, sub_str, start = 0):
    """
    Function to find the substring and how many times a substring appears (Recursive approach)
   
    Parameters:
        srch_str (str): The string to search within.
        sub_str (str): The substring to search for within srch_str.
        start (int, optional): The current starting index in srch_str for the search. Defaults to 0.
        
    Returns:
        int: The count of non-overlapping occurrences of sub_str in srch_str.
    """
    pos = srch_str.find(sub_str, start)  # find function from a string module to find the substring in the given search string
    
    if pos == -1:
        return 0  # Base case: No more occurrences
    else:
        # Recursive call, moving past the found substring
        return 1 + countSubstrRecursive(srch_str, sub_str, pos + len(sub_str))



"""
Main Program 
"""
ans = 'y'
while ans.lower() == 'y':  # Continue until the user decides to stop
    search_str = input("\n\t\t Enter Any String: ")
    substr = input("\n\t\t Now enter a sub-string: ")
    print(f"\n\t\t Search String Entered = {search_str}")
    print(f"\n\t\t Sub - String Entered = {substr}")

    # Iterative Function Call
    count_Itr = countSubstrMatches(search_str, substr)
    print(f"\n\t\t The count of sub-string appears in the Search String (Iterative Approach) = {count_Itr}")

    # Recursive Function Call
    count_Itr = countSubstrRecursive(search_str, substr)
    print(f"\n\t\t The count of sub-string appears in the Search String (Recursive Approach) = {count_Itr}")

    ans = input("\n\n\t\tDo you want to continue [y/n]? ")
    if ans.lower() != 'y':
        print("\n\t\tThank you! Have a nice day!")
        break


"""
PROGRAM IS TESTED FOR THE FOLLOWING:

Enter Any String: ahgdghdgdhgdhgh

Now enter a sub-string: gd

Search String Entered = ahgdghdgdhgdhgh

Sub - String Entered = gd

The count of sub-string appears in the Search String (Iterative Approach) = 3

The count of sub-string appears in the Search String (Recursive Approach) = 3


Do you want to continue [y/n]? y

Enter Any String: jojhthjojuytgjojillkjo

Now enter a sub-string: jo

Search String Entered = jojhthjojuytgjojillkjo

Sub - String Entered = jo

The count of sub-string appears in the Search String (Iterative Approach) = 4

The count of sub-string appears in the Search String (Recursive Approach) = 4


Do you want to continue [y/n]? n

Thank you! Have a nice day!

"""