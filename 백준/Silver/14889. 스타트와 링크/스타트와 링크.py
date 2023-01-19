import sys
n=int(sys.stdin.readline())
people=[]
for i in range(n):
    people.append(list(map(int, sys.stdin.readline().split())))
team_start=[]
team_link=[]
res=1e9
def cal():
    start=0
    link=0
    for i in range(n//2):
        for j in range(i+1, n//2):
            start+=people[team_start[i]][team_start[j]]
            start+=people[team_start[j]][team_start[i]]
    for i in range(n//2):
        for j in range(i+1, n//2):
            link+=people[team_link[i]][team_link[j]]
            link+=people[team_link[j]][team_link[i]]
    return abs(start-link)

def start_link():
    global res
    global team_link
    if len(team_start)==n//2:
        team_link=list(set([i for i in range(n)])-set(team_start))
        res=min(res, cal())
    else:
        for i in range(n):
            if i not in team_start and (len(team_start)==0 or team_start[-1]>i):
                team_start.append(i)
                start_link()
                team_start.pop()

start_link()
print(res)