import math


def finalInstances (instances, averageUtil):
    """
    :type instances: int
    :type averageUtil: List[int]
    :rtype: int
    """
    ptr = 0
    while ptr < len(averageUtil):
        if 25 <= averageUtil[ptr] <= 60:
            ptr += 1
        elif averageUtil[ptr] < 25 and instances > 1:
            instances = math.ceil(instances / 2.0)
            ptr += 11
        elif averageUtil[ptr] < 25 and instances <= 1:
            ptr += 1
        elif averageUtil[ptr] > 60 and instances > 0 and (instances * 2) <= (2 * (10 ** 8)):
            instances = instances * 2
            ptr += 11
        else:
            ptr += 1

    return instances
