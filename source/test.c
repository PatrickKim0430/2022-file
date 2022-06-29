# This file is to store my computer science coding problem solutions
# It contains bunch of problems from baekjoon and code up which are popular coding problem site in Korea

# Programmer:  Patrick Junhee Kim 
# Date: 2022/6/29 
# Problem: Baekjoon 2003 / Sum of numbers 2
  https://www.acmicpc.net/problem/2003 
# Solution: Using python and two pointers concept to solve this problem


N, M = map(int,input().split())
List = list(map(int,input().split()))

Left = 0
Right = 0
cnt = 0
sum2 = 0

while Left <= N:
    if sum2 == M: #
        sum2 = sum2 - List[Right] 
        Right = Right+ 1
        cnt = cnt +1
    elif sum2 > M:
        sum2 = sum2 - List[Right] 
        Right = Right +1 
    else: # sum2 < M:
        if Left == N :
            break
        sum2 = sum2 + List[Left] 
        Left = Left + 1 
print(cnt)
    
   

