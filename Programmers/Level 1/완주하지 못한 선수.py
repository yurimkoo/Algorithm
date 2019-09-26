def solution(participant, completion):
    for par, com in zip(sorted(participant), sorted(completion)):
        if par != com:
            return par
    return participant[-1]