T= int(input())
for _ in range(T):
        x1, y1, r1, x2, y2, r2= map(int,input().split())
        
        # 두 중심점 사이의 거리의 제곱
        dist_sq= (x1-x2)**2 + (y1-y2)**2
        
        # 반지름 합과 차의 제곱
        sum_r= (r1+r2)**2
        diff_r= (r1-r2)**2
        
        # 1. 두 원이 일치하는 경우
        if dist_sq == 0 and r1 == r2:
            print(-1)
        # 2. 한 점에서 만나는 경우 (외접 또는 내접)
        elif dist_sq == sum_r or dist_sq == diff_r:
            print(1)
        # 3. 두 점에서 만나는 경우
        elif diff_r < dist_sq < sum_r:
            print(2)
        # 4. 만나지 않는 경우
        else:
            print(0)