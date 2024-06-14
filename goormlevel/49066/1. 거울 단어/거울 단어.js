
const readline = require('readline');
let N = null;
const arr = [];
const table = {
	'b': 'd','d': 'b','i': 'i','l': 'l','m': 'm','n': 'n','o': 'o','p': 'q','q': 'p', 's':'z','z':'s','u':'u', 'v':'v', 'w':'w', 'x':'x'
}
function isMirror(s){
	/**
		@param {String} s : 거울 단어 여부를 판단할 문자열
		@return {String} : 거울 단어라면 "Mirror", 거울 단어가 아니라면 "Normal" 반환
	*/
	let temp = ""; // 거울 문자를 만들어서 넣을 곳
	const arr = s.split(''); // 문자열을 탐색하기 위해 배열로 만듦
	for (tempS of arr){
		// 만약 매칭되는 알파벳이 아니면 false 반환
		if (!(tempS in table)){
			return false;
		}
		// 매칭되는 알파벳이 있다면 temp에 추가
		temp = table[tempS] + temp;
	}
	// 모든 알파벳이 매칭되는 알파벳이 있었다면 마지막으로 거울 단어 판단
	return temp == s;
}
function solution(arr){
	/**
		@param {String[]} : 단어들의 배열
		@return {void} : 없음
		arr에 존재하는 모든 문자에 대해서 거울 단어 여부 판단.
	*/
	for (s of arr){
		// 거울 문자라면 "Mirror 출력"
		if (isMirror(s)){
			console.log("Mirror");
		}
		// 아니라면 "Normal 출력"
		else{
			console.log("Normal");
		}
	}
}
(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		if (!line){
			rl.close();
		}
		else if (!N){
			N = +line;
		}
		else if (arr.length<N){
			arr.push(line.trim());
		} 
	}
	solution(arr);
	process.exit();
})();
