def is_strictly_decreasing(list_of_integers):
    for i in range(len(list_of_integers) - 1):
        if list_of_integers[i] <= list_of_integers[i+1]:
            return False
    return True