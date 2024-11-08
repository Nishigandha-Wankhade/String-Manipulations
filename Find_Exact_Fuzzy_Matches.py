"""
-----------------------------------------------------------------------
Problem 3: To find EXACT fuzzy matches where all but one character in a substring match.
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



def fuzzyMatching(subOne, subTwo, subOneLen):
    """
    Function to find fuzzy matches where all but one character in a substring match.
    
    Input Parameters:
        subOne (tuple): The tuple of matching start positions for the first substring.
        subTwo (tuple): The tuple of matching start positions for the second substring.
        subOneLen (int): The length of the first substring.
        
    Returns:
        tuple: A tuple containing the start positions of all fuzzy matches.
    """
    fuzzy_matches = []

    # The number of characters to skip (wild card count) is always 1 for fuzzy matching as per given requirement 
    wild_card_count = 1

    
    for start_pos in subOne:   # To iterate over each start position in the first substring tuple
        
        print(f"\n {start_pos} + {subOneLen} + {wild_card_count}")    
        fuzzy_pos = start_pos + subOneLen + wild_card_count    # To calculate the position where the second substring should start for a fuzzy match
        print(f"\n Fuzzy_pos = {fuzzy_pos}")

        if fuzzy_pos in subTwo:        # To check if this calculated position exists in subTwo
            fuzzy_matches.append(start_pos)

    # Return the results as a tuple
    return tuple(fuzzy_matches)



"""
Main Program 
"""
ans = 'y'
while ans.lower() == 'y':  # Continue until the user decides to stop
    
    print("\n\n\t\t\t\t ============ MENU ==============")
    print("\n\t\t\t\t 1. To find a substring ( Iterative Method).")
    print("\n\t\t\t\t 2. to find a substring ( Recursive Method).")
    print("\n\t\t\t\t 3. To find the position of a sub-string.")
    print("\n\t\t\t\t 4. To find fuzzy matches.")
    
    choice = int(input("\n\t\t Please enter the choice [1 - 4]: "))
    search_str = input("\n\t\t Enter Any String: ")
    substr = input("\n\t\t Now enter a sub-string: ")
    
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
    elif choice == 4:
        substr2 = input("\n\t\t Now enter a SECOND sub-string: ")
        
        # To find the position the occurances of a substring
        subOne = allMatchesIndices(search_str, substr)
        print(f"\n\t\t\tsubOne = {subOne} ")
        subTwo = allMatchesIndices(search_str, substr2)
        print(f"\n\t\t\tsubTwo = {subTwo}")

        subOneLen = len(substr)
        print(f"\n\t\t Substring1 Length = {subOneLen}")
        # To find fuzzy matches where all but one character in a substring match.
        result = fuzzyMatching(subOne, subTwo, subOneLen)
        if len(result) != 0:
            print(f"\n\t\t There is a Fuzzy Match at the position : {result}")
        else:
            print("\n\t\t SORRY....! There is NO Fuzzy Match found. ")

    else:
        print("\n\t\t Please enter a valid choice.")

    ans = input("\n\n\t\tDo you want to continue [y/n]? ")
    if ans.lower() != 'y':
        print("\n\t\tThank you! Have a nice day!")
        break


"""
PROGRAM IS TESTED FOR THE FOLLOWING:

================================  TEST 1 ===============================
 Please enter the choice [1 - 4]: 4

                 Enter Any String: abcdefgabad
                 Now enter a sub-string: a

                 Now enter a SECOND sub-string: cd

                        subOne = (0, 7, 9)

                        subTwo = (2,)

                 Substring1 Length = 1

 0 + 1 + 1

 Fuzzy_pos = 2

 7 + 1 + 1

 Fuzzy_pos = 9

 9 + 1 + 1

 Fuzzy_pos = 11

                 There is a Fuzzy Match at the position : (0,)

================================  TEST 2 ===============================
Enter Any String: abcdefg

                 Now enter a sub-string: ab

                 Now enter a SECOND sub-string: de

                        subOne = (0,)

                        subTwo = (3,)

                 Substring1 Length = 2

 0 + 2 + 1

 Fuzzy_pos = 3

                 There is a Fuzzy Match at the position : (0,)


================================  TEST 3 ===============================
Please enter the choice [1 - 4]: 4

                 Enter Any String: abxcdabcd

                 Now enter a sub-string: abc

                 Now enter a SECOND sub-string: d

                        subOne = (5,)

                        subTwo = (4, 8)

                 Substring1 Length = 3

 5 + 3 + 1

 Fuzzy_pos = 9

                 SORRY....! There is NO Fuzzy Match found.

 ================================  TEST 4 ===============================
 Please enter the choice [1 - 4]: 4

                 Enter Any String: mississippi

                 Now enter a sub-string: iss

                 Now enter a SECOND sub-string: ppi

                        subOne = (1, 4)

                        subTwo = (8,)

                 Substring1 Length = 3

 1 + 3 + 1

 Fuzzy_pos = 5

 4 + 3 + 1

 Fuzzy_pos = 8

                 There is a Fuzzy Match at the position : (4,)

"""
