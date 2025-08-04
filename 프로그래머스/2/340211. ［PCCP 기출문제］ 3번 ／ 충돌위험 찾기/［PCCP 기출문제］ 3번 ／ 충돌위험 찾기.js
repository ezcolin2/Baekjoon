function solution(points, routes) {
    let duplicatedCnt = 0;
    // 모든 로봇 생성
    let robots = routes.map((route) => new Robot(points, route));
    
    // 처음 위치에서 중복된 위치 체크
    duplicatedCnt += getDuplicatedLocationCnt(robots);
    while (robots.length > 0){
        // 모든 로봇을 움직인다.
        for (const robot of robots){
            robot.move();
        }
        
        // 중복된 위치 개수 
        duplicatedCnt += getDuplicatedLocationCnt(robots);
        
        // 만약 종료된 로봇이 있다면 배열에서 제거한다.
        robots = robots.filter((robot) => !robot.isEnd());
    }
    return duplicatedCnt;
    
}

// 중복된 위치를 구한다.
function getDuplicatedLocationCnt(robots){
    const map = new Map();
    for (const robot of robots){
        const key = `${robot.currentX},${robot.currentY}`;
        // 만약 키가 map에 없으면 생성해서 1 저장
        if (!map.has(key)){
            map.set(key, 1);
        }
        // 있으면 1 추가
        else{
            map.set(key, map.get(key)+1);
        }
        
    }
    
    // Map 순회해서 중복된 개수 구하기
    let duplicatedLocationCnt = 0;
    for (const [key, value] of map){
        if (value > 1){
            duplicatedLocationCnt += 1;
        }
    }
    return duplicatedLocationCnt;
    
}

class Robot{
    constructor(points, route){
        this.route = route;
        this.points = points;
        this.totalStep = route.length-1; // 총 단계 (0 ~ route 길이)
        this.currentStep = 0;
        this.currentX = points[route[0]-1][0];
        this.currentY = points[route[0]-1][1];
        this.goalX = points[route[1]-1][0];
        this.goalY = points[route[1]-1][1];
    }
    
    // 목적지 도달 여부
    isEnd(){
        return this.currentStep === this.totalStep;
    }
    
    // 한 번 이동
    move(){
        // x 좌표가 동일하지 않다면 x 좌표 이동
        if (this.currentX !== this.goalX){
            if (this.currentX < this.goalX){
                this.currentX += 1;
            }
            else{
                this.currentX -= 1;
            }
            
        }
        
        // x 좌표가 동일하다면 y 좌표 이동
        else{
            if (this.currentY < this.goalY){
                this.currentY += 1;
            }
            else{
                this.currentY -= 1;
            }
        }
        // 목표에 도달한 상황이라면 step 증가
        if (this.currentX === this.goalX && this.currentY === this.goalY){
            this.currentStep += 1;
            // 모두 끝났다면
            if (this.isEnd()){
                return;
            }
            
            // 목표 갱신
            const nextPoint = this.route[this.currentStep+1];
            this.goalX = this.points[nextPoint-1][0];
            this.goalY = this.points[nextPoint-1][1];
        }
    }
}