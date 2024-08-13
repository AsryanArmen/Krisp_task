def find_min_pledge(pledge_list):
    min_pledge = 1

    while min_pledge in pledge_list:
        min_pledge += 1
    
    return min_pledge


assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
assert find_min_pledge([1, 2, 3]) == 4
assert find_min_pledge([-1, -3]) == 1