import sys
cnt=0
def is_append(i, j):
    temp=set([n for n in range(1, 10)])
    temp-=set(sudoku[i])
    for m in range(9):
        temp.discard(sudoku[m][j])
    for n in range((i//3)*3, (i//3)*3+3):
        for m in range((j//3)*3, (j//3)*3+3):
            temp.discard(sudoku[n][m])
    return temp
def dfs(a, b):
    global cnt
    if cnt==0:
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end=' ')
            print()
        exit()
    for i in range(a, 9):
        for j in range(b, 9):
            if sudoku[i][j]==0:
                s=is_append(i, j)
                for k in s:
                    sudoku[i][j]=k
                    cnt-=1
                    dfs(a, b)
                    sudoku[i][j]=0
                    cnt+=1
                return


        
sudoku=[]
for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))
    cnt+=sudoku[i].count(0)
dfs(0, 0)
for i in range(9):
    for j in range(9):
        print(sudoku[i][j], end=' ')
    print()