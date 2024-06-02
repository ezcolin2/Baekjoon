// 편의를 위해 이름을 인덱스로 변경하는 Map
const nameToIndex = new Map()

// 선물을 주고받을 기록을 저장할 2차원 배열
const presentHistory = []

// 선물 지수를 저장할 1차원 배열
const presentIndicator = []

function solution(friends, gifts) {
    // nameToIndex 배열 초기화
    friends.forEach((name, index)=>{
        nameToIndex.set(name, index)
    })
    
    // presentHistory, presentIndicator 초기화
    for (let i=0;i<friends.length;i++){
        presentHistory.push(Array(friends.length).fill(0))
        presentIndicator.push(0)
    }
    
    // presentHistory, presentIndicator 세팅
    gifts.forEach((history)=>{
        const [give, take] = history.trim().split(' ')
        presentHistory[nameToIndex.get(give)][nameToIndex.get(take)]+=1
        presentIndicator[nameToIndex.get(give)]+=1
        presentIndicator[nameToIndex.get(take)]-=1
    })
    
    // 각자 받을 선물 개수
    const presentCount = Array(friends.length).fill(0)
    
    // 탐색 
    // i는 선물을 준 사람, j는 선물을 받은 사람
    for (let i=0;i<friends.length;i++){
        for (let j=0;j<friends.length;j++){
            // 자기 자신과는 비교할 수 없음
            if (i==j){
                continue
            }
            // 준 선물이 더 많다면 선물 받을 예정 
            if (presentHistory[i][j] > presentHistory[j][i]){
                presentCount[i]+=1
            }
            // 주고 받은 선물이 같다면 선물 지수 비교
            else if(presentHistory[i][j] == presentHistory[j][i]){
                
                // 준 사람의 선물 지수가 크다면 선물 개수 증가
                if (presentIndicator[i] > presentIndicator[j]){
                    presentCount[i]+=1
                } 
            }
            // 받은 사람이 더 큰 경우는 고려하지 않음
            // 어차피 반복문이 돌면서 받은 사람이 주는 사람 입장이 되는 순간이 존재하기 때문
        }
    }
    
    let answer = 0;
    presentCount.forEach((cnt)=>{
        if (cnt>answer){
            answer = cnt
        }
    })
    return answer;
}