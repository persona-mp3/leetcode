"""
    Question: Two Sum
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
"""

# i wouldn't touch anything here if i were you

def transpose_algo(array: list, target: int):
    original_array = array.copy()
    array_len = len(array)
    
    i = 0
    
    array = array
    mutated_array = []
    mutation_count = 1
    
    
    
    
    while True:
        if (mutation_count == array_len):
            print('the code has gone through the whole array  and has found nothing', mutation_count)
            return False
    
        for index in range(array_len):
            if (mutation_count == array_len):
                # print('code has gone ', mutation_count)
                return False
    
       
            if len(array) == 1:
                print('rearrange array')
                array.clear()
                print('mutation count increased-->', mutation_count)
                mutated_array.insert(len(mutated_array), first_element)
                
                mutated_array.insert(0, mutated_array[1])
                array.extend(mutated_array)
                mutated_array.clear()
                array.pop(2)
                mutation_count += 1
                
               
            # for every mutation, the first and last elment in the array must always be different
            first_element = array[0]
            last_element = array[ -1]
            
            # we are checking the total of the two elements against the target
            total = first_element + last_element
            
            # if the sum of two numbers found in the array has be met
            # map the values of the mutated array to the orignal array to find its indices
            if total == target:
                print('target found ---->,', total)
                first_position = original_array.index(first_element)
                last_position = original_array.index(last_element)
                return [first_position, last_position]
        
            
            # this runs if the target hasn't been met
            # so it removes the last item in the current array
            # and appends it to the mutated array   
            if (total != target) or len(array) != 1:
                poped_item = array.pop(-1)
                mutated_array.append(poped_item)
                continue
            


# answer = transpose_algo([1, 2, 4, 3, 5 ,8], 11)
# answer = transpose_algo([3, 2, 4], 6)
# answer = transpose_algo([2, 7, 11, 15], 9)
answer = transpose_algo([3, 3], 6)
print(answer)


# 1 --> 2, 3, 5
# 1 --> 2, 3,5
# 1 ---> 2, 3
# 1 --> 2, 
# 1 --> rearrange

# [2, 3, 5, 8, 1]
# 2 --> 3, 5, 8
# 2 --> 3, 5
# 2 --> 3
# 2 ---> rearrange


# [3, 5, 8, 1, 2]
# 3 --> 5, 8, 1
#3 ---> 5, 8,
# 3 --> 11 //found it

# if target was 13
# [5, 8, 1, 2, 3] 
# 5 --> 8, 1, 2
# 5 --> 8, 1
# 5 --> 8 found ir
##rearrange











"""
    The previous solution was quite overengineered and complex, but considering it was your first attempt at a data structure leetcode question with 0 knowledge, i'd say it was good. The previous solution was gearing towards O[n] to 0[n2] compelxity, as it kept re-arranging the items in the array and continued iterating through all of them, again till it met the target.
    Kind of like following n! = n(n-1)!
    
    However, this solution uses a dictionary (hash map) where it stores the values and index of the array in key value pairs, kind of like how you would do in javascript. 

    It iterates through the dictionary once, checking if the target - the_current_value exists in the dictionary, if it doesnt exist, it means that the twoSum is None.
    
    This way, you don't have to keep track of multiple loops and various mutations within the code. It was quite a simple approach, but somehow a complex soution, but it still worked and the thought process was outstanding too.
"""
def two_sum(array: list, target: int):
    
    hash_map = {}
    solution = []
    
    for item in range(len(array)):
        array_item = array[item]
        hash_map[array_item] = item
    
    for i in range(len(array)):
        desired_pair = target - array[i]
        
        if desired_pair not in hash_map:
            print('not found ---->',desired_pair) 
            continue
        elif (desired_pair == i):
            print('duplicates found --->', desired_pair, i)
            continue
        else:
            solution.append(hash_map[desired_pair])
            solution.append(i)
            
    return solution
        


answer = two_sum([1, 2, 4, 3, 5 ,8], 13)
print(answer)