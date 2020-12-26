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


# Validation of float number
class Solution:
    def isNumber(self, s: str) -> bool:

        state_dict = {
            1: {'num': 2, 'sign': 3, 'dot': 10},
            2: {'num': 2, 'dot': 4, 'e': 5, 'final': 6},
            3: {'num': 2, 'dot': 10},
            4: {'num': 9, 'final': 6, 'e': 5},
            5: {'num': 7, 'sign': 8},
            7: {'num': 7, 'final': 6},
            8: {'num': 7},
            6: {},
            9: {'e': 5, 'num': 9, 'final': 6},
            10: {'num': 9}
        }
        cur_state = 1

        s = s.strip()

        if len(s) == 1 and s[0] == '.':
            return False

        for ch in s:
            if ch in '0123456789':
                state = 'num'
            elif ch in 'e':
                state = 'e'
                flag_e = True
            elif ch in '+-':
                state = 'sign'
            elif ch in '.':
                state = 'dot'
            else:
                state = 'unknown'

            if state not in state_dict[cur_state]:
                return False

            cur_state = state_dict[cur_state][state]

        if 'final' in state_dict[cur_state]:
            return True

        return False

