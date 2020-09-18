# BUBBLE SORT
# O(n) best case 
# O(n^2) worst case
​
def bubble_sort(num_list):
    n = len(num_list)
    # Initial setup, will use n later
    for i in range(n):
        # Traverse the list and all items within the list
        for j in range(0, n - i -1):
            # Traverse the list from 0 to n-i-1, since i has already been traversed
            # this will be our comparison for each value
            # Swap if elements found are greater than previous elements
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
                # Shorthand for swapping values in python
    print("List is sorted!")
    print(num_list)
    return num_list
​
bubble_sort(numbers)