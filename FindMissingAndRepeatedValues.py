class Solution:                                         #common convention structure for LeetCode problems
    def findMissingAndRepeatedValues(self, grid): #function to find missing and repeated values
        # Flatten the grid to a single list
        nums = [num for row in grid for num in row] #flatten the grid to a single list

        # Initialize count dictionary
        count = {} #initialize count dictionary
        for num in nums: #for loop to iterate through the list
            if num in count: #if statement to check if the number is in the count dictionary
                count[num] += 1 #increment the count of the number
            else: #else statement if the number is not in the count dictionary
                count[num] = 1 #initialize the count of the number to 1

        # Initialize variables for missing and repeated numbers
        n = len(grid)  # since it's n by n grid
        repeated = None #initialize repeated variable to None
        missing = None #initialize missing variable to None

        # Check up to n*n as per the problem statement
        for i in range(1, n*n + 1): #for loop to iterate through the range of numbers
            if i not in count: #if statement to check if the number is not in the count dictionary
                missing = i     #set the missing variable to the number
            elif count[i] == 2: #else if statement to check if the count of the number is 2
                repeated = i #set the repeated variable to the number

        return [repeated, missing] #return the repeated and missing numbers in a list
