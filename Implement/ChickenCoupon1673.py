import sys
input= sys.stdin.readline

while True:
    line= input()
    if not line:
        break
    n, k= map(int, line.split())
    stamps= n
    while stamps >= k:
        new= stamps//k
        n += new
        stamps= stamps%k + new
    print(n)