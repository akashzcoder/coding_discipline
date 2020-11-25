def kadanesAlgorithm(array):
    # Write your code here.
    """
    [3, -10, 4]
    if s > 0:
        continue adding
    else:
        reset sum
        update max_until_now
    return max_until_now
    """
    #
    if len(array) == 0:
        return
    subarr_sum = array[0]
    max_subarr_sum = array[0]
    for val in array[1:]:
        subarr_sum = max(subarr_sum + val, val)
        max_subarr_sum = max(max_subarr_sum, subarr_sum)
    return max_subarr_sum
