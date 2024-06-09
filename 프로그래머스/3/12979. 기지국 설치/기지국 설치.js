function solution(n, stations, w) {
    let cnt = Math.ceil((stations[0]-w-1)/(2*w+1));
	for (let i=1;i<stations.length;i++){
        cnt += Math.ceil((stations[i] - stations[i-1]-1-2*w)/(2*w+1));
    }
    if (n-stations[stations.length-1]-w > 0){
        cnt += Math.ceil((n- stations[stations.length-1]-w)/ (2*w+1));
    }
    return cnt;
}