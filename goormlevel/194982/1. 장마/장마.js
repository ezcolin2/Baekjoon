// Run by Node.js
const readline = require('readline');
let [N, M, heights, rainRange] = [null, null, null, ['a']];
(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		if (!line){
			rl.close();
		}
		if (!N && !M){
			[N, M] = line.trim().split(' ').map(Number);
		}
		else if(!heights){
			heights = line.trim().split(' ').map(Number);
			heights.unshift(0)
		}
		else if (rainRange.length <=M){
			rainRange.push(line.trim().split(' ').map(Number));
		}
	}
	// 집의 개수만큼 배열 생성
	// 물의 높이
	const water = Array(N+1).fill(0);
	// 그 동안 물이 내렸던 위치
	// 집합을 통해 중복 거름
	let set = new Set();
	// 탐색 시작
	// 장마 기간 동안 물의 높이 측정

	for (let i=1; i<=M; i++){
		for (let j=rainRange[i][0]; j<=rainRange[i][1]; j++){
			water[j]+=1;
			set.add(j);
		}
		// 3의 배수면 배수 시스템 동작
		if (i%3 == 0){
			for (s of set){
				water[s] -= 1;
				if (water[s] <0){
					water[s] = 0;
				}
			}
			set = new Set();
			
		}
	}
	// 땅의 높이 계산
	for (let i=1;i<=N;i++){
		heights[i]+=water[i];
	}
	console.log(heights.slice(1).join(' '))
	process.exit();
})();
