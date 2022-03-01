#! /usr/bin/python3

DIV = 1000000007

def solve():
	
	n = int(input())
	arr = [int(x) for x in input().split()]

	arr.sort()

	cache = list(range(arr[-1] * n, 0, -n)) 

	for i in range(n - 2, -1, -1):

		for j in range(arr[i] - 2, -1, -1):

			cache[j] = cache[j] + cache[j + 1] % DIV
	print(cache[0])

t = int(input())

for _ in range(t):
	
	solve()


