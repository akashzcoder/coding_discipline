"""
Input: "mamad"
                "mamad"
            "mamad"       "ammad"
    "mamad"  "mamad" "ammad"   "mmaad"

O(2^n) ===> memoization: O(n^2)

Output: 3
---------
"""


def solution(s: str) -> int:
    return helper_solution(list(s), 0, 0, float('inf'))


def helper_solution(s, index, cur_swap, swap) -> int:
    if len(s) == index-1:
        if ''.join(s) == ''.join(s[::-1]):
            swap = min(swap, cur_swap)
        else:
            return 0
    s[index], s[index+1] = s[index+1], s[index]
    cur_swap += 1
    helper_solution(s, index+1, cur_swap, swap)
    s[index+1], s[index] = s[index], s[index+1]
    cur_swap -= 1
    return swap


print(solution("madam"))
