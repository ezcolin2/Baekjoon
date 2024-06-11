// Run by Node.js
/*
	실제로 회전을 하지 않고 head의 인덱스만 변경한다.
*/
function solution(n, m, arr){
	/**
		@param {number} n : 수열의 길이
		@param {number} m : 회전 횟수
		@param {number[]} arr : 수열
		@return {void} : 반환 값 없음
	*/
	// 가장 첫 번째 원소의 인덱스
	let head = 0;
	
	for (let i = 0; i<m ; i++){
		// 회전할 횟수
		// n번 회전하면 처음과 동일하기 때문에 나머지를 구함
		let cnt = arr[head] % n;
		// head 왼쪽으로 이동
		head = head+cnt;
		if (head>n-1){
			head-=n;
		}
	}
	console.log(arr[head]);
	process.exit();
}
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let [n, m, arr] = [null, null, null];
	for await (const line of rl) {
		if (!n && !m){
			[n, m] = line.trim().split(' ').map(Number);
		}
		else if (!arr){
			arr = line.trim().split(' ').map(Number);
			solution(n, m, arr);
			rl.close();
		}
	}
	
	process.exit();
})();
