# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/2 
# Problem: Baekjoon 2003 https://www.acmicpc.net/problem/2003
# Solution: Using python and two pointer concepts to solve this problem


N, S = map(int, input().split())
A = list(map(int, input().split()))
# First of all solving sum of  0~n
sum_A = [0] * (N + 1)
for i in range(1, N + 1):
    sum_A[i] = sum_A[i-1] + A[i-1]  
    
# Two pointer concepts
answer = 1000001
start = 0
end = 1

# Performing program
while start != N:
    if sum_A[end] - sum_A[start] >= S:
        if end - start< answer:
            answer = end - start
        start += 1
        
    else:
        if end != N:
            end += 1
        else:
            start += 1

if answer != 1000001:
    print(answer)
else:
    print(0)
