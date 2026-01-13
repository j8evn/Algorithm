N=int(input())

nums=[]
for i in range(N):
    x,y=list(map(int,input().split()))
    nums.append([x,y])
    
nums.sort() # 2차원 배열에서 sort 함수의 기본값: 행 정렬 -> 열 정렬

for i in range(N):
    print(nums[i][0],nums[i][1])
