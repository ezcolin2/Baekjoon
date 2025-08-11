function solution(coin, cards) {
    const n = cards.length;
    let maxRound = 0;
	const chosenCards = Array(n+1).fill(false);
    const visitedCards = Array(n+1).fill(false);
    // 합쳐서 n이 나오는 카드 조합 개수
    let combinationCnt = 0;
    let possibleCombinationCnt = 0; // 가능성이 있는 조합 개수
    for (let i=0; i<n/3; i++){
        chosenCards[cards[i]] = true;
        visitedCards[cards[i]] = true;
        if (chosenCards[n-cards[i]+1]){
            combinationCnt++;
        }
    }
    
    // 시작
    for (let i=0; i<=(n-n/3)/2; i++){
        maxRound++;
        if (i===(n-n/3)/2){
            break;
        }
        const firstCard = cards[n/3+i*2];
        const secondCard = cards[n/3+i*2+1];
        visitedCards[firstCard] = true;
        visitedCards[secondCard] = true;
        
        // 만약 조합이 가능하다면 바로 뽑기
        if (chosenCards[n-firstCard+1]){
            // coin이 남았다면 뽑기
            if (coin>0){
                chosenCards[firstCard] = true;
                combinationCnt++;
                coin--;
            }
            
        }
        if (chosenCards[n-secondCard+1]){
            // coin이 남았다면 뽑기
            if (coin>0){
                chosenCards[secondCard] = true;
                combinationCnt++;
                coin--;
            }

        }
        
        // 이전에 방문했던 카드 중에서 뽑아서 조합을 만들 수 있다면
        if (!chosenCards[n-firstCard+1] && visitedCards[n-firstCard+1]){
            possibleCombinationCnt++;
        }
        // 이전에 방문했던 카드 중에서 뽑아서 조합을 만들 수 있다면
        if (!chosenCards[n-secondCard+1] && visitedCards[n-secondCard+1]){
            possibleCombinationCnt++;
        }
        console.log(firstCard, secondCard, combinationCnt, possibleCombinationCnt, coin)
        // combinationCnt가 있다면 다음 라운드 진출 가능
        if (combinationCnt>0){
            combinationCnt--;
        } 
        // 방문했던 카드 두 개 뽑아서 할 수 있다면
        else if (possibleCombinationCnt>0 && coin>1){
            possibleCombinationCnt--;
            coin-=2;
        } else{
            break;
        }
    }
    return maxRound;
}