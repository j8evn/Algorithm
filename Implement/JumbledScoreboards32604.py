def is_chronological(n, scores):
    for i in range(1, n):
        if scores[i][0]<scores[i-1][0] or scores[i][1]<scores[i-1][1]:
            return "no"
    return "yes"

n = int(input())
scores = [tuple(map(int, input().split())) for _ in range(n)]

print(is_chronological(n, scores))
