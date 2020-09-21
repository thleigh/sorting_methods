from random import shuffle
tries = 0

def is_sorted(ls):
    # loop through the list
    # 
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]: return False
    return True

def bogo_sort(ls):
    global tries
    tries += 1
    if is_sorted(ls): return ls
    # if not, shuffle list + 
    shuffle(ls)
    return bogo_sort(ls)

test = [1, 9, 23, 5, 2, 6, 45]
print('Testing', test, 'and it is ', bogo_sort(test), ' sort was found aft ', tries, 'tries')