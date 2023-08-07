def solution(a_list, index):
    if index >= len(a_list) or index < 0:
        return "invalid index"
    val = a_list[index]
    if val == max(a_list):
        return -1
    b_list = a_list[:]
    b_list.sort()
    return a_list.index(b_list[b_list.index(val) + 1])

print(solution([-1,-2,-3],1))
