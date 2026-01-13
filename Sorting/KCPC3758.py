import sys
input= sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k, t, m= map(int, input().split())
    
    scores= [[0]*(k+1) for _ in range(n+1)]
    submit_cnt= [0]*(n+1)
    last_submit= [0]*(n+1)
    
    for time in range(m):
        team_id, prob_id, score= map(int, input().split())

        if score > scores[team_id][prob_id]:
            scores[team_id][prob_id]= score

        submit_cnt[team_id] += 1
        last_submit[team_id]= time

    team_results= []
    for i in range(1, n + 1):
        total_score= sum(scores[i])
        team_results.append((total_score, submit_cnt[i], last_submit[i], i))

    team_results.sort(key=lambda x:(-x[0], x[1], x[2]))

    for rank in range(n):
        if team_results[rank][3] == t:
            print(rank+1)
            break
