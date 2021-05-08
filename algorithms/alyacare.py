"""
Palindrome of a string.

input str:
output: bool
"""


def palindrome(input: str) -> bool:
    """
    Find palindrome of a string

    input: str
    return: bool
    """
    if not input:
        return False
    len_str = len(input)
    for index, ch in enumerate(input):
        if index == len_str // 2:
            return True
        if ch != input[len_str-index-1]:
            return False


print(palindrome("akash singh is king!"))
