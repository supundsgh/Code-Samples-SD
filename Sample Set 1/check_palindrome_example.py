class CheckPalindrome:

    def palindromeCheck(x):
        '''Return True if an input integer is a palindrome, and False if not.
        Inputs: 
            x: An integer value
        Outputs: 
            True if x is a palindrome, and False if not'''

        # Convert integer to String
        y = str(x)

        # Check if the integer is a palindrome number
        if y == y[::-1]: # Check if the integer is same when read backwards
            return True
        else:            # Check if the integer is not same when read backwards
            return False
       
        
    # Test case 1
    # Assign a boolean flag: if an integer is palindrom or not
    palindrome_check_flag = palindromeCheck(1331)
    # Print assigned flag
    print(palindrome_check_flag)

    # Test case 2
    # Assign a boolean flag: if an integer is palindrom or not
    palindrome_check_flag = palindromeCheck(1332)
    # Print assigned flag
    print(palindrome_check_flag)