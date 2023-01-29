

def solution(x):
    answer = 0
    
    if x == 0:
        answer = 0
    if x == 1:
        answer = 1
    if x >= 2:
        answer = solution(x-1) + solution(x-2)
        
    return answer

print(solution(5))


