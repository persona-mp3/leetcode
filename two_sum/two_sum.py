"""
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.
"""

## returning the indices
# and adding the values of the indices that sum up to target
# [3,  12, 4], target= 7
# return [0, 2]


## ---> index looping, iterate through each element in the array
## ----> we need to get two indices at a time
## ----> sum these two indices



def two_sum(array: list):
    # target = 6
    # set start of array to be 0
    array_length = len(array)
    target = 9
    
    for i in range(array_length):
        
        # if i == (len(array) -1):
        #     print('done')
        #     return
       
        total =  array[i]  +  array[-i-1]
        # total = array[i+1] + array[-i-1]
        
        print(total)
        # print(array[i])
        # print(array[-i-1])
        
        if total == target:
            print('found it')
            end_index = len(array) - i - 1
            start_index = i
            # print(i, -i-1)
            print('target found is ----> ',total)
            print('at indices ----->', [start_index, end_index])
            return
        
        
      # print(total)
      
      
      
      
def two_summ(array: list):
    array_length = len(array)
    target = 9
    
    
    
   
    pass
        
    


#two_sum([1, 2, 3, 5, 8]) # 11

# 1. iterating throught the array checked
# 2. have a fixed ref point checked
# 3. have a moving point checked
# 4. for each sum(iteration), if target isnt met, pop the elemet from the array 
# 5. repeat step 1 checked
# 6. if target isnt found we need to rearrange the array moving rearrange
# 7. new array = [second_elemnet, x, y, z, first_element]
# 7. new array = [third_elemnet, x, y, z, first_element, second_element]


def transpose_algo(array: list, target: int):
    original_array = array.copy()
    array_len = len(array)
    array_search = array
    
    i = 0
    # mutation_count = 1
    
    # first_element = array[i]
    
    array = array
    mutated_array = []
    mutation_count = 1
    
    
    while True:
        if (mutation_count == array_len):
            print('balonnyy', mutation_count)
            return False
    
        for index in range(array_len):
            if (mutation_count == array_len):
                print('balonnyy', mutation_count)
                return False
    
       
            
            # array = mutated_array
            # array = array
            
            if len(array) == 1:
                print('rearrange array')
                array.clear()
                print('mutation count increased-->', mutation_count)
                mutated_array.insert(len(mutated_array), first_element)
                
                # mutated_array.pop(1)
                mutated_array.insert(0, mutated_array[1])
                # print(array, mutated_array)
                array.extend(mutated_array)
                mutated_array.clear()
                # print('cleared mutation --->', mutated_array)
                array.pop(2)
                mutation_count += 1
                # print('new arrat', array)
                
                # array.pop(0)
                # array.extend(mutated_array) 
                # mutation_count+=1
                # print(mutation_count, '<----- mutation count')
                # print(array)
                
               

            first_element = array[0]
            last_element = array[ -1]
            # print('last-element--->', last_element)
            # print('first-elemet ---->', first_element)
            total = first_element + last_element
            print('------------------------')
            # print('total --->', total)
            # print(total)
            
            if total == target:
                print('target found ---->,', total)
                first_position = original_array.index(first_element)
                last_position = original_array.index(last_element)
                # print('indexes found are--->', first_position, last_position)
                
                # return [last_position, first_position]
                return [first_position, last_position]
        
        
            if (total != target) or len(array) != 1:
                poped_item = array.pop(-1)
                mutated_array.append(poped_item)
                continue
            
            # if len(array
            
            
            # total = first_element = array[i+1]
            
     
    pass


# answer = transpose_algo([1, 2, 4, 3, 5 ,8], 11)
# answer = transpose_algo([3, 2, 4], 6)
# answer = transpose_algo([2, 7, 11, 15], 9)
answer = transpose_algo([3, 3], 6)
print(answer)
# transpose_algo([1, 2, 4, 3, 16 ,12], 16)

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




# 1, 8
# 2, 5
# 3, ?(3) --> 6