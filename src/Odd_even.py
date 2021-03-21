'''You will be given an array of numbers. You have to sort 
the odd numbers in ascending order while leaving the even numbers at their original positions.

example:
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

'''


def sort_array(source_array):
    # Return a sorted array.
    if len(source_array) <= 1:
        return source_array
    
    odd = []
    for number in source_array:
        if number % 2 != 0:
            odd.append(number)
    odd.sort()
    
    indx = 0
    for pos in  range(len(source_array)):
        if source_array[pos] % 2 != 0:
            source_array[pos] = odd[indx]
            indx +=1
 
  
    return source_array


print(sort_array([5, 3, 2, 8, 1, 4]))    