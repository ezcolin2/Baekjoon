const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let N = null; // 보드의 크기 
let [rA, cA, rB, cB] = [null, null, null, null]; // 플레이어 A와 B의 시작 위치
const arr = [[0, 0, 0, 0]]; // 지시 사항
const dx = { // command에 따라 이동할 행의 방향
	'U': -1,
	'D': 1,
	'R': 0,
	'L': 0
};
const dy = { // command에 따라 이동할 열의 방향
	'U': 0,
	'D' : 0,
	'R': 1,
	'L': -1
};
function checkOutside(x, N){
	/**
		말이 바깥으로 나갔다면 반대쪽으로 이동시키는 함수
		행과 열 모두 공통적으로 사용한다
		@param {Number} x : 말의 다음 위치
		@return {Number} : 조정한 말의 위치
	*/
	if (x==0){
		return N;
	} else if (x==N+1){
		return 1;
	} else{
		return x;
	}
}
function move(visited, r, c){
	/**
		현재 위치와 이동 방향을 받아서 이동 가능 여부와 다음 위치를 반환하는 함수
		@param {String[]} direction : [count][command]. command 위치로 count 만큼 이동하라는 명령
		@param {boolean[][]} visited : visited[a][b]의 의미는 arr[a][b]의 방문 여부 
		@param {Number} r : 현재 행의 위치
		@param {Number} c : 현재 열의 위치
		@return {Any[]} : [다음 행, 다음 열, 얻은 점수]
		만약 반환 값의 다음 행과 다음 열이 모두 -1 이라는 것은 재방문 한 곳이 있어서 게임이 종료되었다는 뜻
	*/
	const direction = arr[r][c];
	const [count, command] = [Number(direction.slice(0, direction.length-1)), direction[direction.length-1]];
	
	// 다음 위치 초기화
	let [nr, nc] = [r, c];
	
	// 점수
	let score = 0;
	
	// count만큼 반복 
	for (let i=0; i<count; i++){
		// 한 번 움직일 때마다 바깥인지 체크해서 위치 조정
		[nr, nc] = [checkOutside(nr+dx[command], N), checkOutside(nc+dy[command], N)];
		
		// 방문했다면 반환
		if (visited[nr][nc]){
			return [-1, -1, score];
		}
		// 방문하지 않았다면 점수 증가
		score+=1;
		visited[nr][nc] = true;
	}
	// 방문한 곳을 다시 방문하지 않았다면 제대로 반환
	return [nr, nc, score];
}

function solution(N, rA, cA, rB, cB, arr){
	let [visitedA, visitedB] = [[], []]; // 플레이어 A와 B의 방문 배열
	let [isEndA, isEndB] = [false, false]; // 플레이어 A와 B의 게임 끝 여부
	// 계산의 편의를 위해 N+1개 생성
	visitedA = Array(N+1).fill(0).map(()=>Array(N+1).fill(false));
	visitedB = Array(N+1).fill(0).map(()=>Array(N+1).fill(false));

	// 시작 점 방문 
	visitedA[rA][cA] = true;
	visitedB[rB][cB] = true;
	
	// 플레이어 A와 B의 점수
	let [scoreA, scoreB] = [1, 1]; 
	while(true){
		if (isEndA && isEndB){
			break;
		}
		if (!isEndA){
			const [nrA, ncA, tempScoreA] = move(visitedA, rA, cA);

			// 종료
			if (nrA == -1 && ncA == -1){
				scoreA += tempScoreA;
				isEndA = true;
			}
			// 아직 안 끝남
			else{
				scoreA += tempScoreA;
				[rA, cA] = [nrA, ncA];
			}
		}
		if (!isEndB){
			const [nrB, ncB, tempScoreB] = move(visitedB, rB, cB);

			// 종료
			if (nrB == -1 && ncB == -1){
				scoreB += tempScoreB;
				isEndB = true;
			}
			// 아직 안 끝남
			else{
				scoreB += tempScoreB;
				[rB, cB] = [nrB, ncB];
			}
		}
	}
	// while(true){
	// 	const [nrB, ncB, tempScoreB] = move(visitedB, rB, cB);
	// 	// 종료
	// 	if (nrB == -1 && ncB == -1){
	// 		scoreB += tempScoreB;
	// 		break;
	// 	}
	// 	// 아직 안 끝남
	// 	else{
	// 		scoreB += tempScoreB;
	// 		[rB, cB] = [nrB, ncB];
	// 	}
	// }
	
	// 구름이의 승리
	if (scoreA > scoreB){
		console.log(`goorm ${scoreA}`);
	} 
	// 플레이어의 승리
	else{
		console.log(`player ${scoreB}`);
	}

}
rl.on('line', (line) => {
	// input start
	if (!N){
		N = +line;
	}
	else if (!rA && !cA){
		[rA, cA] = line.trim().split(' ').map(Number);
	} else if (!rB && !cB){
		[rB, cB] = line.trim().split(' ').map(Number);
	} else if (arr.length <= N){
		const temp = [0];
		line.trim().split(' ').forEach((item)=>{temp.push(item)});
		arr.push(temp);
	} else{


		rl.close();
	}
	// input end
	
	
});

rl.on('close', () => {
	// 입력 모두 받았으면 실행
	solution(N, rA, cA, rB, cB, arr);
	process.exit();
})