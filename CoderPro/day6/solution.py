def find_redundant_number(ls):
    if len(ls) == 0:
        return None
    final_result = ls[0]
    for val in ls[1:]:
        final_result ^= val
    return final_result


answer = find_redundant_number([1, 1, 2, 3, 3])
assert answer == 2

answer = find_redundant_number([4,1,2,1,2])
assert answer == 4

# test corner cases
answer = find_redundant_number([])
assert answer is None

answer = find_redundant_number([0, 0, 0, 0])
assert answer == 0
