"""Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the orginal array except the one at i.

For example, if our input was [1,2,3,4,5], the expected output would be [120, 60,40,30,24]
 """

 # SOLUTION

 # This problem would be easy with division: an optimal solution could just find the product of all numbers in an arry and then divide by each of the numbers.

 # To solve this, we would apply a technique in solving an array problem: precomputing results from subarrays, and building up a solution from these results.

 # We would use divide and conquer approach to solve this problem: 
 # Compute the product of all numbers before i and the product of all elements after i. And finally multiply the two products to get the desired result.


 def products(num):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)
    
    # Generate sufffix products
    suffix_products = []
    for num in reversed(num):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
        suffix_products = list(reversed(suffix_products))

        result = []
        for i in range(len(num)):
            if i == 0:
                result.append(suffix_products[i+1])
            elif i == len(num) -1 :
                result 


        

        # Generate result from the product of prefixes and suffixes
        
