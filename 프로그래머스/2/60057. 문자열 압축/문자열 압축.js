// arr를 n개 기준으로 자름
function splitString(arr, n){
    const splitted = [];
    for (let i=0;i<arr.length;i+=n){
        // n번 반복
        let tmp = '';
        // 마지막에 남은 문자열의 길이가 n보다 작을 때를 대비
        for (let j=0;j<n && i+j<arr.length;j++){
            tmp+=arr[i+j];
        }
        splitted.push(tmp);
    }
    return splitted;
}
function solution(s) {
    let res = s.length;
    // i는 자를 개수
    for (let i=1;i<s.length;i++){
        let answer = '';
        const arr = splitString(s, i);
        let cnt=1;
        for (let j=1;j<arr.length;j++){
            // 같다면 cnt 증가
            if (arr[j] == arr[j-1]){
                cnt += 1;
            } else{
                // 다른데 cnt가 2 이상이면 숫자 붙임
                if (cnt>=2){
                    answer += `${cnt}${arr[j-1]}`;
                    cnt=1;
                }
                // 다른데 cnt가 2 미만이면 그냥 넣음
                else{

                    answer += arr[j-1];
                    cnt=1;
                }
            }
        }
        
                // 다른데 cnt가 2 이상이면 숫자 붙임
                if (cnt>=2){
                    answer += `${cnt}${arr[arr.length-1]}`;
                }
                // 다른데 cnt가 2 미만이면 그냥 넣음
                else{
                    answer += arr[arr.length-1];
                }
        if (answer.length < res){
            res = answer.length;
        }
    }
    return res;
}