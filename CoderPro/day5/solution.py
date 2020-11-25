class Solution:

    @staticmethod
    def reoder_person(inp):
        inp.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for x in inp:
            result.insert(x[1], x)
        return result


output = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
assert Solution.reoder_person(inp=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]) == output
