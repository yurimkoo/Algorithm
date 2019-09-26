def solution(answers):
    supos = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    for i in range(3):
        supos[i] = (supos[i]*(len(answers)-len(supos[i])))[:len(answers)] if len(supos[i]) < len(answers) else supos[i][:len(answers)]
        for j in range(len(answers)):
            supos[i][j] = supos[i][j] == answers[j]
        supos[i] = sum(supos[i])
    
    max_score = max(supos)
    answer = []
    for i in range(3):
        if supos[i] == max_score:
            answer.append(i+1)
    return sorted(answer)