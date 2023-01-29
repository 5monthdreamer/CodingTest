
# 이진 탐색 (Iterative version)

def solution(L: list, x: int):
    answer = -1
    start = 0
    end = len(L)-1
    
    while start <= end and start in range(len(L)) and end in range(len(L)):
        mid = (start+end)//2
        if L[mid] == x:
            answer = mid
            break
        elif L[mid] > x:
            end = mid-1
        elif L[mid] < x:
            start = mid+1
    
    return answer


print(solution([2,3,5,6,9,11,15],6))


