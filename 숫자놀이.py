# 문제 이해 : N개의 수 >>> 산술평균 / 중앙값 / 최빈값 / 범위 출력

# 산술평균: N개 값들을 모두 더하고, 수의 개수로 나눈 값
# 중앙값: N개 수들을 정렬했을때, 중앙에 위치한 값
# 최빈값: N개 수들 중에서 가장 자주 등장하는 값, 여러개라면 가장 큰 값을 출력하자.
# 범위: N개 수들 중에서 최소값과 최대값의 차이

# N 은 500,000이하의 양의 홀수이다.
# 주어지는 모든 수는 100 이하이다.

import sys

N = int(input())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort(reverse=True)

# 1. 오름차순으로 정렬된 수들의 현재 값, 다음 값 비교
# 2. 만약 같다면 count += 1
# 3. 만약 다르다면 count = 1 에서부터 다시 시작.
count = 1
tmp_dict = {}
for i in range(N):
	if i+1 == N:
		tmp_dict[arr[i]] = count
		break
	if arr[i] != arr[i+1]:
		tmp_dict[arr[i]] = count
		count = 1
	else:
		count += 1

tmp_list = [k for k, v in tmp_dict.items() if v == max(tmp_dict.values())]

mode = max(tmp_list)

mean = sum(arr)/N
median = arr[N//2]
rang = max(arr)-min(arr)

print(f'{round(mean)}\n{median}\n{mode}\n{rang}')
