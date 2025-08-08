// 동서남북
const dx = [0, 0, 1, -1];
const dy = [1, -1, 0, 0];

function solution(maze) {
    const n = maze.length;
    const m = maze[0].length;
    
    let redStart = null, blueStart = null;
    let redEnd = null, blueEnd = null;
    
    // 시작점과 도착점 찾기
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (maze[i][j] === 1) redStart = [i, j];
            else if (maze[i][j] === 2) blueStart = [i, j];
            else if (maze[i][j] === 3) redEnd = [i, j];
            else if (maze[i][j] === 4) blueEnd = [i, j];
        }
    }
    
    // BFS
    const queue = [];
    const visited = new Set();
    
    // 초기 상태: 각 수레의 방문 배열 초기화
    const initRedVisited = Array(n).fill().map(() => Array(m).fill(false));
    const initBlueVisited = Array(n).fill().map(() => Array(m).fill(false));
    initRedVisited[redStart[0]][redStart[1]] = true;
    initBlueVisited[blueStart[0]][blueStart[1]] = true;
    
    queue.push({
        redPos: redStart,
        bluePos: blueStart,
        redVisited: initRedVisited,
        blueVisited: initBlueVisited,
        turns: 0
    });
    
    // 상태를 문자열로 변환
    const getStateKey = (redPos, bluePos) => {
        return `${redPos[0]},${redPos[1]},${bluePos[0]},${bluePos[1]}`;
    };
    
    visited.add(getStateKey(redStart, blueStart));
    
    while (queue.length > 0) {
        const { redPos, bluePos, redVisited, blueVisited, turns } = queue.shift();
        
        // 둘 다 도착했는지 확인
        if (redPos[0] === redEnd[0] && redPos[1] === redEnd[1] && 
            bluePos[0] === blueEnd[0] && bluePos[1] === blueEnd[1]) {
            return turns;
        }
        
        // 각 수레가 도착했는지 확인
        const redArrived = (redPos[0] === redEnd[0] && redPos[1] === redEnd[1]);
        const blueArrived = (bluePos[0] === blueEnd[0] && bluePos[1] === blueEnd[1]);
        
        // 빨간 수레의 가능한 이동
        const redMoves = [];
        if (redArrived) {
            redMoves.push(redPos);
        } else {
            for (let i = 0; i < 4; i++) {
                const nx = redPos[0] + dx[i];
                const ny = redPos[1] + dy[i];
                
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && 
                    maze[nx][ny] !== 5 && !redVisited[nx][ny]) {
                    redMoves.push([nx, ny]);
                }
            }
        }
        
        // 파란 수레의 가능한 이동
        const blueMoves = [];
        if (blueArrived) {
            blueMoves.push(bluePos);
        } else {
            for (let i = 0; i < 4; i++) {
                const nx = bluePos[0] + dx[i];
                const ny = bluePos[1] + dy[i];
                
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && 
                    maze[nx][ny] !== 5 && !blueVisited[nx][ny]) {
                    blueMoves.push([nx, ny]);
                }
            }
        }
        
        // 모든 가능한 조합 시도
        for (const nextRed of redMoves) {
            for (const nextBlue of blueMoves) {
                // 같은 칸에 있는지 확인
                if (nextRed[0] === nextBlue[0] && nextRed[1] === nextBlue[1]) continue;
                
                // 서로 자리를 바꾸는지 확인
                if (redPos[0] === nextBlue[0] && redPos[1] === nextBlue[1] && 
                    bluePos[0] === nextRed[0] && bluePos[1] === nextRed[1]) continue;
                
                // 이미 방문한 상태인지 확인
                const stateKey = getStateKey(nextRed, nextBlue);
                if (visited.has(stateKey)) continue;
                
                // 새로운 방문 배열 생성
                const newRedVisited = redVisited.map(row => [...row]);
                const newBlueVisited = blueVisited.map(row => [...row]);
                
                // 실제로 이동한 경우에만 방문 표시
                if (!redArrived) {
                    newRedVisited[nextRed[0]][nextRed[1]] = true;
                }
                if (!blueArrived) {
                    newBlueVisited[nextBlue[0]][nextBlue[1]] = true;
                }
                
                visited.add(stateKey);
                queue.push({
                    redPos: nextRed,
                    bluePos: nextBlue,
                    redVisited: newRedVisited,
                    blueVisited: newBlueVisited,
                    turns: turns + 1
                });
            }
        }
    }
    
    return 0; // 도달 불가능
}