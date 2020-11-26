def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    len_arr1 = len(arrayOne)
    len_arr2 = len(arrayTwo)
    if len_arr1 == 0 and len_arr2 == 0:
        return True
    elif arrayOne[0] != arrayTwo[0] or len_arr1 != len_arr2:
        return False
    ele = arrayOne[0]
    aux1_s = []
    aux1_l = []
    aux2_s = []
    aux2_l = []
    for i in range(1, len_arr1):
        if arrayOne[i] < ele:
            aux1_s.append(arrayOne[i])
        else:
            aux1_l.append(arrayOne[i])
        if arrayTwo[i] < ele:
            aux2_s.append(arrayTwo[i])
        else:
            aux2_l.append(arrayTwo[i])
    return sameBsts(aux1_s, aux2_s) and sameBsts(aux1_l, aux2_l)
