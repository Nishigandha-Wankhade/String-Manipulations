"""
-----------------------------------------------------------------------
Assignment 4 Problem 2: To find the start positions of every match between a substring and a string.
November 03, 2024 
Nishigandha Wankhade 
-----------------------------------------------------------------------
"""

from string import * # to use all possible functions from a string module / library

def countSubstrMatches(srch_str, sub_str):
    """
    Function to count the number of non-overlapping occurrences of a substring within a search string using an iterative approach.
    
    Input Parameters:
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
   
    Input Parameters:
        srch_str (str): The string to search within.
        sub_str (str): The substring to search for within srch_str.
        start (int, optional): The current starting index in srch_str for the search. Defaults to 0.
        
    Returns:
        int: The count of non-overlapping occurrences of sub_str in srch_str.
    """
    pos = srch_str.find(sub_str, start)  # find() from a string module to find the substring in the given search string
    
    if pos == -1:
        return 0  # Base case: No more occurrences
    else:
        # Recursive call, moving past the found substring
        return 1 + countSubstrRecursive(srch_str, sub_str, pos + len(sub_str))



def allMatchesIndices(srch_str, sub_str):
    """
    Function to find the start positions of every match between a substring and a string.
    
    Input Parameters:
        srch_str (str): The string in which to search for matches.
        sub_str (str): The substring to search for within srch_str.
        
    Returns:
        tuple: A tuple containing the start indices of all matches of sub_str in srch_str.
    """
    indices = []  # a List to store start positions of every matches
    start = 0

    while True:
        start = srch_str.find(sub_str, start)   # find() from a string module to find the substring in the given search string
        if start == -1:  # No more matches found
            break
        indices.append(start)  # Collect the start index
        start = start + 1  # Move to the next position to continue searching

    return tuple(indices)  # Convert the list to a tuple and return



"""
Main Program 
"""
ans = 'y'
while ans.lower() == 'y':  # Continue until the user decides to stop
    search_str = input("\n\t\t Enter Any String: ")
    substr = input("\n\t\t Now enter a sub-string: ")
    #print(f"\n\t\t Search String Entered = {search_str}")
    #print(f"\n\t\t Sub - String Entered = {substr}")

    print("\n\n\t\t\t\t ============ MENU ==============")
    print("\n\t\t\t\t 1. To find a substring ( Iterative Method).")
    print("\n\t\t\t\t 2. to find a substring ( Recursive Method).")
    print("\n\t\t\t\t 3. To find the position of a sub-string.")
    
    choice = int(input("\n\t\t Please enter the choice [1 - 3]: "))
    
    if choice == 1:
        # Iterative Function Call
        count_Itr = countSubstrMatches(search_str, substr)
        print(f"\n\t\t The count of sub-string appears in the Search String (Iterative Approach) = {count_Itr}")
    elif choice == 2:
        # Recursive Function Call
        count_Itr = countSubstrRecursive(search_str, substr)
        print(f"\n\t\t The count of sub-string appears in the Search String (Recursive Approach) = {count_Itr}")
    elif choice == 3:
        # To find the position the occurances of a substring
        position = allMatchesIndices(search_str, substr)
        print(f"\n\t\t allMatchesIndices('{search_str}', '{substr}')")
        print(f"\n\t\t {position}")
    else:
        print("\n\t\t Please enter a valid choice.")

    ans = input("\n\n\t\tDo you want to continue [y/n]? ")
    if ans.lower() != 'y':
        print("\n\t\tThank you! Have a nice day!")
        break


"""
PROGRAM IS TESTED FOR THE FOLLOWING:

Enter Any String: atatattta

Now enter a sub-string: ata


        ============ MENU ==============

        1. To find a substring ( Iterative Method).

        2. to find a substring ( Recursive Method).

        3. To find the position of a sub-string.

Please enter the choice [1 - 3]: 3

allMatchesIndices('atatattta', 'ata')

(0, 2)


Do you want to continue [y/n]? y

Enter Any String: atatatatta

Now enter a sub-string: ata


        ============ MENU ==============

        1. To find a substring ( Iterative Method).

        2. to find a substring ( Recursive Method).

        3. To find the position of a sub-string.

Please enter the choice [1 - 3]: 3

allMatchesIndices('atatatatta', 'ata')

(0, 2, 4)


Do you want to continue [y/n]? y

Enter Any String: atattatta

Now enter a sub-string: Python


        ============ MENU ==============

        1. To find a substring ( Iterative Method).

        2. to find a substring ( Recursive Method).

        3. To find the position of a sub-string.

Please enter the choice [1 - 3]: 3

allMatchesIndices('atattatta', 'Python')

()


Do you want to continue [y/n]? n

Thank you! Have a nice day!
"""