function solution(num_list) {
    const mul = num_list.reduce((acc, num)=>acc*num, 1);
    const squareOfSum = num_list.reduce((acc, num)=>acc+num)**2;
    return mul<squareOfSum ? 1 : 0;
}