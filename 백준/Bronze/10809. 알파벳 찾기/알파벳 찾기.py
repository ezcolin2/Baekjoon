s=input()
alpha=[chr(ord('a')+i) for i in range(26)] #모든 알파벳을 저장한다. 
for i in alpha:
    print(s.find(i), end=" ") #해당 알파벳이 존재하지 않으면 -1, 존재하면 인덱스 출력력