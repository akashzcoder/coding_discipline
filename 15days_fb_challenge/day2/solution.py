class Solution:

    @staticmethod
    def _get_states(cur_state, value):
        state = {
            1: {'blank': 1, 'sign': 2, 'digit': 3},
            2: {'digit': 3},
            3: {'digit': 3}
        }
        if value in state[cur_state]:
            return state[cur_state][value]
        return False

    @staticmethod
    def _in_range(num):
        if num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif num < -1 * (2 ** 31):
            return -1 * (2 ** 31)
        else:
            return num

    def myAtoi(self, s: str) -> int:
        sign = 1
        cur_state = 1
        num = 0

        for ch in s:
            if ch == ' ':
                value = 'blank'
            elif ch == '-' or ch == '+':
                value = 'sign'
            elif ch in '0123456789':
                value = 'digit'
            else:
                value = 'unknown'
            cur_state = Solution._get_states(cur_state, value)

            if cur_state is False:
                break

            if value == 'sign':
                sign = -1 if ch == '-' else 1
            elif value == 'digit':
                num = num * 10 + int(ch)

        return self._in_range(sign * num)