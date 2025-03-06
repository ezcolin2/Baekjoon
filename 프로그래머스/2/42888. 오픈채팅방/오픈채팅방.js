/**
	1. 유저 아이디 식별자로 사용하여 닉네임을 매핑하는 구조 필요 -> Map 사용
    2. 유저의 행동과 유저 아이디를 매핑하는 구조 필요 
    	-> 출입 기록만 출력하기 때문에 enter와 leave 정보만 저장
        -> 순서가 중요하기 때문에 {행동, 유저 아이디}의 배열 사용
    1, 2번 구조를 가지고 최종적으로 로그를 출력하는 함수 필요
*/

// record 정보를 바탕으로 유저 식별자마다 닉네임이 매핑된 map을 반환한다.
function getUserNicknameMap(record){
    // 유저 식별자 - 닉네임 map 생성
    const userNicknameMap = {};
    // 각 로그를 순회한다.
    for (const log of record){
        // 공백을 기준으로 나눈다.
        const logArr = log.split(' ');
        
        // 행동과 유저 식별자를 구한다.
        const activity = logArr[0];
        const userId = logArr[1];
        
        // 들어오거나 닉네임을 변경했다면
        if (activity === "Enter" || activity === "Change"){
            const userNickname = logArr[2];
            // Map에 저장
            userNicknameMap[userId] = userNickname;
        }
        
        // 나간 경우는 원래 닉네임을 유지한다.
    }
    return userNicknameMap;
}

// record 정보를 바탕으로 유저마다 행동을 기록한 배열을 반환한다.
function getUserActivityArr(record){
    // 배열을 생성한다.
    const userActivityArr = [];
    
    // 각 로그를 순회한다.
    for (const log of record){
        // 공백을 기준으로 나눈다.
        const logArr = log.split(' ');
        
        // 행동과 유저 식별자를 구한다.
        // 닉네임은 변동되기 때문에 사용할 필요 없다.
        const activity = logArr[0];
        const userId = logArr[1];
        
        // 닉네임 변경은 로그에 출력할 필요 없기 때문에 제외한다.
        if (activity === "Change"){
            continue;
        }
        
        // 출입 기록만 배열에 저장한다.
        const userActivity = {activity, userId};
        userActivityArr.push(userActivity);
        
    }
    return userActivityArr;
}
function getFinalLogArr(userNicknameMap, userActivityArr){
    const finalLogArr = [];
    // 출입 기록을 순회한다.
    for (const userActivity of userActivityArr){
        // 출입 기록과 유저 닉네임을 매핑한다.
        const {activity, userId} = userActivity;
        const userNickname = userNicknameMap[userId];
        
        // 들어왔을 때
        if (activity === "Enter"){
            const finalLog = `${userNickname}님이 들어왔습니다.`;
            finalLogArr.push(finalLog);
        }
        
        // 나갔을 때
        else{
            const finalLog = `${userNickname}님이 나갔습니다.`;
            finalLogArr.push(finalLog);
        }
    }
    return finalLogArr;
}
function solution(record) {
    userNicknameMap = getUserNicknameMap(record);
    userActivityArr = getUserActivityArr(record);
    const answer = getFinalLogArr(userNicknameMap, userActivityArr);
    return answer;
}