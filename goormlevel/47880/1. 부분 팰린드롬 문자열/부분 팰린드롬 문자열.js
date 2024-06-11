// Run by Node.js
function isPal(s, startIdx, endIdx){
	/**
		부분 문자열 s[startIdx]~s[endIdx]가 회문인지 검사하는 함수
		@param {number} startIdx : 부분 문자열 시작 인덱스
		@param {number} endIdx : 부분 문자열 끝 인덱스
		@return {boolean} : 회문 여부
	*/
	// startIdx가 endIdx보다 같거나 커질때까지 반복
	while (startIdx < endIdx){
		// 달라지는 순간 false 반환
		if (s.charAt(startIdx) != s.charAt(endIdx)){
			return false;
		}
		startIdx++;
		endIdx--;
	}
	// 같아졌는데도 동일하면 true 반환
	return true;
}
function solution(s){
	/**
		본격적으로 해결하는 함수
		@param {number} s : 문자열
		@return {void} : 반환값 없음
	*/
	
	// len에 해당하는 모든 부분 문자열에 대해서 회문 여부 조사
	// 큰 것부터 조사하면 처음 발견하는 것이 가장 긴 펠린드롬이 된다.
	for (let len = s.length; len>=2; len--){
		for (let i = 0; i<=s.length-len; i++){
			// 부분 문자열의 시작, 끝 인덱스를 가지고 회문 여부 판단
			// 회문이면 길이 출력하고 끝
			if (isPal(s, i, i+len-1)){
				console.log(len);
				process.exit();
			}
		}
	}
	// 길이가 1인 것은 반드시 회문 
	console.log(1);
}
const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
rl.on("line", function(line) {
	solution(line);
	rl.close();
}).on("close", function() {
	process.exit();
});

