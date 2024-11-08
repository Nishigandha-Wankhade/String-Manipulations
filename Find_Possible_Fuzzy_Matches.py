"""
-----------------------------------------------------------------------
Problem 4: To find fuzzy matches where all but one character in a substring match.
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



def fuzzyMatchesOnly(srch_str, sub_str):
    """
    Returns a tuple of starting positions in srch_str where sub_str appears as a fuzzy match,
    meaning that one character is different from sub_str at that position.
    Exact matches are not included.
    Input Parameters:
        srch_str (str): The string in which to search for matches.
        sub_str (str): The substring to search for within srch_str.
        
    Returns:
        tuple: A tuple containing the start indices of all fuzzy matches of sub_str in srch_str. 
    """
    len_sub = len(sub_str)
    fuzzy_matches = []

    # Get all exact match positions (to skip later)
    exact_matches = allMatchesIndices(srch_str, sub_str)
    print(f"\n\t\t Exact Matches = {exact_matches}")

    for i in range(len(srch_str) - len_sub + 1):
        # Skip exact matches
        if i in exact_matches:
            print(f"\n\t\t Exact Match found at {i}th location...so skip")
            continue
        
        # Check for fuzzy match (one-character difference)
        slice_str = srch_str[i:i + len_sub]
        mismatch_count = 0

        # Count mismatches manually .....we can use zip() too
        for j in range(len_sub):
            if slice_str[j] != sub_str[j]:
                mismatch_count += 1
                if mismatch_count > 1:
                    break  # Stop if more than one mismatch

        # Only add starting index if there is exactly one mismatch
        if mismatch_count == 1:
            fuzzy_matches.append(i)

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
    print("\n\t\t\t\t 5. To find fuzzy matches ONLY.")
    print("\n\t\t\t\t 6. Exit")
    
    choice = int(input("\n\t\t Please enter the choice [1 - 5]: "))
    if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
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
            print(f"\n\t\t There is a Exact Fuzzy Match at the position : {result}")
        else:
            print("\n\t\t SORRY....! There is NO EXACT Fuzzy Match found. ")
    elif choice == 5:
        
        result = fuzzyMatchesOnly(search_str, substr)
        if len(result) != 0:
            print(f"\n\t\t There are a Fuzzy Matches at the position : {result}")
        else:
            print("\n\t\t SORRY....! There are NO Fuzzy Matches found. ")
    elif choice == 6:
        break
    else:
        print("\n\t\t Please enter a valid choice.")

    ans = input("\n\n\t\tDo you want to continue [y/n]? ")
    if ans.lower() != 'y':
        print("\n\t\tThank you! Have a nice day!")
        break


"""
PROGRAM IS TESTED FOR THE FOLLOWING:

================================  TEST 1 ===============================

                                 ============ MENU ==============

                                 1. To find a substring ( Iterative Method).

                                 2. to find a substring ( Recursive Method).

                                 3. To find the position of a sub-string.

                                 4. To find fuzzy matches.

                                 5. To find fuzzy matches ONLY.

                                 6. Exit

                 Please enter the choice [1 - 5]: 5

                 Enter Any String: abcabcabc

                 Now enter a sub-string: anc

                 Exact Matches = ()

                 There are a Fuzzy Matches at the position : (0, 3, 6)


                Do you want to continue [y/n]? y


    ================================  TEST 2 ===============================

                 Please enter the choice [1 - 5]: 5

                 Enter Any String: mississippi

                 Now enter a sub-string: imp

                 Exact Matches = ()

                 There are a Fuzzy Matches at the position : (7,)

================================  TEST 3 ===============================                
                Please enter the choice [1 - 5]: 5

                 Enter Any String: abcdabcfgh

                 Now enter a sub-string: agb

                 Exact Matches = ()

                SORRY....! There are NO Fuzzy Matches found.

================================  TEST 4 ===============================                 
                Please enter the choice [1 - 5]: 5

                 Enter Any String: mississippi

                 Now enter a sub-string: iss

                 Exact Matches = (1, 4)

                 Exact Match found at 1th location...so skip

                 Exact Match found at 4th location...so skip

                 SORRY....! There are NO Fuzzy Matches found.

"""
