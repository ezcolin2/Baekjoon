// 동서남북
const dx = [0, 0, 1, -1];
const dy = [1, -1, 0, 0];

function solution(rectangle, characterX, characterY, itemX, itemY) {
    for (const rect of rectangle){
        rect[0]*=2;
        rect[1]*=2;
        rect[2]*=2;
        rect[3]*=2
    }
    characterX*=2;
    characterY*=2;
    itemX*=2;
    itemY*=2;
    // 둘레 경로 구하기
    const pathCoordinates = getPathCoordinates(rectangle);
    
    // 둘레 경로 기반으로 50 x 50 좌표 생성
    const arr = Array(101).fill().map(() => Array(101).fill(0));
    
    // 경로를 1로 표현
    for (const pathCoordinate of pathCoordinates){
        arr[pathCoordinate[0]][pathCoordinate[1]] = 1;
    }
    
    let hello = 0;
    for (const row of arr){
        for (const val of row){
            if (val === 1){
                hello++;
            }
        }
    }
    // 최단 거리 구하기
   return getShortestDistance(arr, characterX, characterY, itemX, itemY)/2;
}

// 최단 거리 구하기
function getShortestDistance(arr, startX, startY, endX, endY){
    const n = arr.length;
    const m = arr[0].length;
    // 방문 여부
    const visited = Array(n).fill().map(() => Array(m).fill(false));
    
    // 각 좌표까지 도달하는데 최단 거리
    const distanceArr = Array(n).fill().map(() => Array(m).fill(0));
    const queue = new Queue();
    
    // 첫 위치 방문
    visited[startX][startY] = true;
    queue.enqueue([startX, startY]);
    
    // 큐가 빌 때까지
    while (!queue.isEmpty()){
        // 꺼내오기 
        const [x, y] = queue.dequeue();
        
        // 4방향 탐색
        for (let i=0; i<4; i++){
            const [nx, ny] = [x+dx[i], y+dy[i]];
            // 만약 좌표 벗어나면 스킵
            if (nx<0 || nx>=n || ny<0 || ny>=m){
                continue;
            }
            
            // 방문했다면 스킵
            if (visited[nx][ny]){
                continue;
            }
            
            // 길이 아니라면 스킵
            if (arr[nx][ny] === 0){
                continue;
            }
            
            // 만약 다음 갈 곳이 분기되어 있다면 스킵
            if (isSplitted(arr, visited, nx, ny) && isSplitted(arr, visited, x, y)){
                continue;
            }
            
            // 방문
            distanceArr[nx][ny] = distanceArr[x][y] + 1;
            queue.enqueue([nx, ny]);
            visited[nx][ny] = true;
            
            // 만약 도착했다면
            if (nx === endX && ny === endY){
                return distanceArr[nx][ny];
            }
        }
    }
}

// 갈 수 있는 곳이 분기되어 있는지
function isSplitted(arr, visited, x, y){
    const n = arr.length;
    const m = arr[0].length;
    let pathCnt = 0;
    for (let i=0; i<4; i++){
        const [nx, ny] = [x+dx[i], y+dy[i]];
        if (nx<0 || nx>=n || ny<0 || ny>=m || visited[nx][ny] || arr[nx][ny] === 0){
            continue;
        }
        pathCnt++;
    }
    return pathCnt>=2;
}

// 모든 둘레 좌표 반환 함수
function getPathCoordinates(rectangle){
    const pathCoordinates = [];
    // 모든 사각형 순회하면서 둘레 좌표 가져오기
    for (const rect of rectangle){
        for (let x=rect[0]; x<=rect[2]; x++){
            for (let y=rect[1]; y<=rect[3]; y++){
                // 단 하나의 사각형 안에 포함되면 스킵
                if (isInside(rectangle, x, y)){
                    continue;
                }
                pathCoordinates.push([x, y]);
            }
        }
    }
    return pathCoordinates;
}

// 모든 사각형과 비교해서 좌표가 단 하나의 사각형 안에라도 포함되는지
function isInside(rectangle, x, y){
    for (const rect of rectangle){
        if (isInsideRectangle(rect, x, y)){
            return true;
        }
    }
    return false;
}

// (x, y) 좌표가 rectangle 안에 있는지
function isInsideRectangle(rect, x, y){
    return rect[0] < x && x < rect[2] && rect[1] < y && y < rect[3];
}

class Queue{
    constructor(){
        this.items = {};
        this.head = 0;
        this.tail = 0;
    }
    
    isEmpty(){
        return this.head === this.tail;
    }
    
    enqueue(item){
        this.items[this.tail++] = item;
    }
    
    dequeue(){
        const item = this.items[this.head];
        delete this.items[this.head++]
        return item;
    }
}