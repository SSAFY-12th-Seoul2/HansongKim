n=int(input())
paper=[[0 for _ in range(100)] for _ in range(100)]
for i in range(n):
    a,b=map(int,input().split())
    ae=a+10; be=b+10
    for j in range(b,be):
        for k in range(a,ae):
            paper[j][k]=1
count=0
for s in range(100):
    for t in range(100):
        if paper[s][t]==1:
            count+=1
print(count)