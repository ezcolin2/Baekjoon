function maxSquareOfTwo(N){
		/**
		@param {Number} N : 숫자
		@return {Number} : N보다 작은 2의 제곱 중 가장 큰 값의 제곱수를 반환한다.
		ex) N이 500이면 2의 8 제곱이 256으로 가장 크기 때문에 8 반환.
		
	*/
	// N보다 커질 때까지 구함
	let res = 0;
	while (2**res <= N){
		res++;
	}
	// 커졌을 때 멈추므로 1을 뺌
	return res-1;
}

function solution(N){
	/**
		@param {Number} N : 만들고 싶은 세포의 크기
		@return {String} : 세포들의 분열 시간이 공백을 두고 띄어진 문자열
		만들고 싶은 세포의 크기 N을 입력 받아서 각 세포들에 필요한 분열 시간을 문자열 형태로 반환한다.
	*/
	// 문자열을 더할 변수
	let res = "";
	
	// N이 0 될때까지
	while (N > 0){
		// 2의 i 제곱이 N보다 작은 수 중 가장 큰 값을 구한다.
		const squareCnt = maxSquareOfTwo(N);
	
		// N에서 2의 해당 제곱만큼 뺀다.
		N-=2**squareCnt;
		
		// 큰 값이 뒤로 가도록 문자열에 더한다.
		res = `${squareCnt} ${res}`;
	}
	
	return res;

}
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let N = null;
	for await (const line of rl) {
		if (!line){
			rl.close();
		}
		if (!N){
			N = +line;
		}
	}
	const res = solution(N);
	console.log(res.trim().split(' ').length);
	console.log(res.trim());
	process.exit();
})();
