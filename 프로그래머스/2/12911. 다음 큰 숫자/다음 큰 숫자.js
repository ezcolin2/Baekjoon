function toBinary(n){
    let i=0;
    while(2**i <= n){
        i++;
    }
    let binary = '';
    for (let j=i-1;j>=0;j--){
        if (2**j <= n){
            binary+='1';
            n-=2**j;
        } else{
            binary+='0';
        }
    }
    return binary;
}
function countOne(binary){
    let cnt=0;
    for (let i=0;i<binary.length;i++){
        if (binary[i]=='1'){
            cnt+=1;
        }
    }
    return cnt;
}
function solution(n) {
    const binary = toBinary(n);
    const numberOfOne = countOne(binary);
    let answer = n+1;
    while (true){
        if (countOne(toBinary(answer)) == numberOfOne){
            return answer;
        }
        answer+=1;
    }
}