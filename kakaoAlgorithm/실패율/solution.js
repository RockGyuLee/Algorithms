function solution(N, stages) {
    let answer = [];

    let stageCount = []
    

    for( let i = 1; i <= N;  i++ ){
        let userCount = stages.length;
        let stageUser =  stages.filter(item => item == i)
        if(stageUser.length == 0){
            stageCount.push(0)
        }else{
            stageCount.push(stageUser.length/ userCount)
            stages = stages.filter( item => item != i);
        }
    }

    for(let i = 0; i < N; i++){
        let size = Math.max(...stageCount);
        let stageIndex = stageCount.indexOf(size)
        answer.push(stageIndex+1)
        stageCount[stageIndex] = -1
    }
    
    console.log(answer);
    return answer;
}


solution(5,[2, 1, 2, 6, 2, 4, 3, 3] )
solution(4,[4,4,4,4,4] )

/*
N	stages	result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	[4,1,2,3]

*/