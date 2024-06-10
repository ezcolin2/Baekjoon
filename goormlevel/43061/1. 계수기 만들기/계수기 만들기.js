// Run by Node.js

function next(N, arrA, arrB){
	/*
	  자릿수의 최대 값을 넘으면 실행
		처음부터 끝까지 조사하면서 자릿수 올림
		@param {N} 숫자판 개수
		@param {A} 각 숫자판의 최대 값
		@param {B} 각 숫자판의 초기 값
		@returns {void} 없음
	*/
	// 낮은 자릿수부터 탐색
	for (let i=N-1; i>0; i--){
		// 최대값을 넘으면 해당 자리수는 0으로 만들고 다음 자리수 1 증가
		if (arrB[i] > arrA[i]){
			arrB[i]=0;
			arrB[i-1]++;
		}
	}
}
function solution(N, A, B, cnt){
	/*
		메인 함수
		@param {N} 숫자판 개수
		@param {A} 각 숫자판의 최대 값
		@param {B} 각 숫자판의 초기 값
	*/
	// N번 누름
	for (let i=0; i<cnt; i++){
		// 누르고 최대 값 넘었는지 체크
		B[N-1]++;
		// 넘었을 때만 
		if (A[N-1] < B[N-1]){
			next(N, A, B);
		}
	}
	arrB[0] %= (arrA[0]+1)
	console.log(arrB.join(""))	
	
}
const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
let N = null;
let arrA = null;
let arrB = null;
let cnt = null;
rl.on("line", function(line) {
	if (!line){
		rl.close();
	}
	if (!N){
		N = +line;
	} else if(!arrA){
		arrA = line.trim().split(' ').map(Number);
	} else if(!arrB){
		arrB = line.trim().split(' ').map(Number);
	} else if (!cnt){
		cnt = +line;
	}
	
}).on("close", function() {
	solution(N, arrA, arrB, cnt)
	process.exit();
});