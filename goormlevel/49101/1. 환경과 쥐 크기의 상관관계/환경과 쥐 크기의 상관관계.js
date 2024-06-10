// Run by Node.js
const readline = require('readline');
function getNumberOfRat(arr, x){
	return arr[x-2]+arr[x-1]+arr[x]+arr[x+1]+arr[x+2];
}
function solution(N, A, B){
	// arr[i]의 의미는 크기가 i인 생쥐의 수
	const arrA = Array(100001).fill(0);
	const arrB = Array(100001).fill(0);
	// 모든 개수를 전부 다 구함
	A.forEach((item)=>{
		arrA[item]++;
	});
	B.forEach((item)=>{
		arrB[item]++;
	});
	
	// 현재까지 가장 많은 수
	let numA = 0;
	let numB = 0;
	// 대표값 
	let resA = 2;
	let resB = 2;
	
	for (let i=3;i<=99998;i++){
		if (getNumberOfRat(arrA, i) > getNumberOfRat(arrA, resA)){
			resA = i;
		}
		if (getNumberOfRat(arrB, i) > getNumberOfRat(arrB, resB)){
			resB = i;
		}
	}
	console.log(resA, resB);
	if (resA > resB){
		console.log("good")
	} else{
		console.log("bad")
	}
}
(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let N = null;
	let A = null;
	let B = null;
	for await (const line of rl) {
		if (!line){
			rl.close();
		}
		if (!N){
			N = +line
		}
		else if (!A){
			A = line.trim().split(' ').map(Number);
		}
		else if (!B){
			B = line.trim().split(' ').map(Number);
		}
	}
	solution(N, A, B);
	process.exit();
})();
