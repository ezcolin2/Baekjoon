function solution(id_list, report, k) {
    // 이름을 인덱스로 변경하는 Map
    const nameToIndex = new Map();
    id_list.forEach((id, index)=>{
        nameToIndex.set(id, index)
    })
    
    // 신고 여부 2차원 배열
    const userNum = id_list.length
    const isReported = Array(userNum).fill(0).map((item) =>Array(userNum).fill(false))
    
    // 신고 횟수 1차원 배열
    const reportCount = Array(userNum).fill(0)
    
    report.forEach((item)=>{
        const [reportId, reportedId] = item.trim().split(' ').map((id)=>nameToIndex.get(id))
        // 같은 사람이 신고한지 파악 후 아니라면 신고 횟수 증가
        if (!isReported[reportedId][reportId]){
            reportCount[reportedId]+=1
        }
        // 계산의 편의를 위해 [신고 받은 사람][신고 한 사람]으로 저장
        
        isReported[reportedId][reportId] = true
    })
    
    const answer = Array(userNum).fill(0)
    reportCount.forEach((count, index)=>{
        // 일정 횟수 이상 신고를 받았다면
        if (count>=k){
            isReported[index].forEach((bool, idx)=>{
                if (bool){
                    answer[idx]+=1
                }
            })
        }
    })
    console.log(isReported)
    return answer;

}