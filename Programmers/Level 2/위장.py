def solution(clothes):
    answer = 1
    
    d = {}
    for val, key in clothes:
        if key in d.keys():
            d[key].append(val)
        else:
            d[key] = [val]
    
    for val in d.values():
        answer *= (len(val)+1)
    
    return answer - 1
    