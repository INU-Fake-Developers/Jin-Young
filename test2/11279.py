import heapq
import sys


n = int(input())
heap = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0: #0이 아니라면
        heapq.heappush(heap, (-num)) #num값에 -를 입혀 heap으로 푸쉬
    else:
        #예외 처리
        try:
            print(-(heapq.heappop(heap))) #실행할 코드 (heap에서 가장 작은 값을 반환)
        except:
            print(0)  #예외가 발생하면 실행할 코드 (0으로 출력)