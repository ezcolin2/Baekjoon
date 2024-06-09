function recursive(a, b, cnt){
    // 숫자가 같아지면 멈춤
    if (a==b){
        return cnt;
    }
    return recursive(Math.ceil(a/2), Math.ceil(b/2), cnt+1);
}
function solution(n,a,b)
{
    return recursive(a, b, 0);
}