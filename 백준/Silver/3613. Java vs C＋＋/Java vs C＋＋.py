import sys
input=sys.stdin.readline
from_str=input().rstrip()
if from_str[0].isupper() or from_str[0]=='_' or from_str[-1]=='_':
    print('Error!')
    exit()
to_java=from_str[0] # 첫 번째 문자는 동일
to_cpp=from_str[0] # 첫 번째 문자는 동일
is_c=False
is_java=False
#c++ 형식이면 java로 
for i in range(1, len(from_str)):
    if from_str[i-1]=='_':
        if from_str[i]=='_':
            print('Error!')
            exit()
        to_java+=from_str[i].upper()
    elif from_str[i]=='_':
        is_c=True # '_'가 존재하면 C++이라는 뜻
        continue
    else:
        to_java+=from_str[i]

#java 형식이면 c++로
for i in range(1, len(from_str)):
    if from_str[i].isupper():
        is_java=True # 대문자가 있으면 java라는 뜻
        to_cpp+='_'
        to_cpp+=from_str[i].lower()
    else:
        to_cpp+=from_str[i]
if is_c and is_java:
    print('Error!')
elif is_c==True:
    print(to_java)
else:
    print(to_cpp)