import sys
from collections import defaultdict
input = sys.stdin.readline

key = input().strip()
cypher_text = input().strip()
dic = defaultdict(list)
i = 0
for k in sorted(key):
    dic[k].append(cypher_text[i:i+len(cypher_text)//len(key)])
    i += len(cypher_text)//len(key)

plain_text = ''
for i in range(len(cypher_text)//len(key)):
    check = defaultdict(int)
    for k in key:
        plain_text += dic[k][check[k]][i]
        check[k] += 1
print(plain_text)