def solution(priorities, location):
    pri = [(i, p) for i, p in enumerate(priorities)]
    
    print_list = []
    i = 0
    while 1:
        out = priorities.pop(0)
        for i, p in pri:
            if out == p:
                out_index = i
                break
        p_tmp = pri.pop(0)

        if len(priorities) > 0:
            max_p = max(priorities)
            if out < max_p:
                priorities.append(out)
                pri.append(p_tmp)
                i += 1
            else:
                print_list.append((out_index, out))
        else:
            print_list.append((out_index, out))
            break

    for i, p in print_list:
        if i == location:
            return print_list.index((i, p))+1