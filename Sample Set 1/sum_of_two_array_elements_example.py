class SumOfTwoArrayElements:

    def sumOfTwoArrayElements(nums, target):
        '''For a given array of integers, return indices of the integers that sum up to a target integer
        Inputs:
            nums: (list[int]) A array of integers
            target: (int) The expected sum of two elements
        Output: 
            (list[int]) Indices of two integers that sum up to a target
            Returns None if there are no elements that sum up to the target'''

        # Initiate return variable
        result = None
        
        # Iterate through the indices, i, of the array elements
        for i in range(0,len(nums)):

            # Iterate through the of the indices after i
            for j in range(i+1,len(nums)):

                # Sum of the two elements at each index 
                sumOfNums = nums[i] + nums[j]

                # Check if the above sum is equal to the target integer
                if sumOfNums == target:
                    # Save the indices
                    result = [i,j]

        # Return the saved indices
        return result
    
    
    # --- Test case 1 ---
    # Example array of integers 
    num_array = [1,2,3,4,5,6]
    # Examplem target integer
    target = 10
    # Indices of array elements that sum up to target
    saved_indices = sumOfTwoArrayElements(num_array, target)
    # Print the indices
    print(saved_indices)


    # --- Test case 2 ---
    # Example array of integers 
    num_array = [4,12,6,10,34,2]
    # Examplem target integer
    target = 38
    # Indices of array elements that sum up to target
    saved_indices = sumOfTwoArrayElements(num_array, target)
    # Print the indices
    print(saved_indices)


    # --- Test case 3 ---
    # Example array of integers 
    num_array = [4,12,6,10,34,2]
    # Examplem target integer
    target = 39
    # Indices of array elements that sum up to target
    saved_indices = sumOfTwoArrayElements(num_array, target)
    # Print the indices
    print(saved_indices)

