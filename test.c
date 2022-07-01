# This file is to store my computer science coding problem solutions
# It contains bunch of problems from baekjoon and code up which are popular coding problem site in Korea

# Programmer:  Patrick Junhee Kim 
# Date: 2022/7/1 
# Problem: Baekjoon 9872 / Record keeping 
  https://www.acmicpc.net/problem/9872 
# Solution: Using python and list concepts to solve this problem


All=[]
Count=0
List=[]
Num=int(input(""))
for a in range(Num):
    All.append([(i) for i in input().split(' ')])
for b in All:
    b.sort()
All.sort()
compare=All[0]
for c in range(0,Num):
    if All[c]==compare:
        Count+=1
    else:
        List.append(Count)
        compare=All[c]
        Count=1
if len(List)==0:
    print(Count)
else:
    print(max(List))
