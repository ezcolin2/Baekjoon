# 백준 2608
# 문자열
import sys
input=sys.stdin.readline
rome={'V':5, 'L':50, 'D':500, 'I':1, 'X':10, 'C':100, 'M':1000}
s={'I', 'X', 'C'} # 이 문자는 뒤 문자에 따라 값이 달라짐
def change_value_to_arabic(x): # 로마 숫자를 아라비아 숫자로 변경
    num=0
    i=0
    while i<len(x):
        if x[i]=='I':
            if i+1<len(x) and x[i+1]=='V':
                num+=4
                i+=1
            elif i+1<len(x) and x[i+1]=='X':
                num+=9
                i+=1
            else:
                num+=1
        elif x[i]=='X':
            if i+1<len(x) and x[i+1]=='L':
                num+=40
                i+=1
            elif i+1<len(x) and x[i+1]=='C':
                num+=90
                i+=1
            else:
                num+=10
        elif x[i]=='C':
            if i+1<len(x) and x[i+1]=='D':
                num+=400
                i+=1
            elif i+1<len(x) and x[i+1]=='M':
                num+=900
                i+=1
            else:
                num+=100
        else:
            num+=rome[x[i]]
        i+=1
    return num
arr=[ # idx 0은 1의 자리, idx 1은 10의 자리, idx 2는 100의 자리, idx 3은 1000의 자리 
    
    ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    ['', 'M', 'MM', 'MMM']
]
def change_value_to_roman(num):
    roman=''
    for i in range(len(num)-1, -1, -1):
        roman+=arr[i][int(num[len(num)-1-i])]
    return roman
a=input().rstrip()
b=input().rstrip()
arabic=change_value_to_arabic(a)+change_value_to_arabic(b)
roman=change_value_to_roman(str(arabic))
print(arabic)
print(roman)