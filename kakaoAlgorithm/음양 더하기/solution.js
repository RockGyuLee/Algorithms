function solution(absolutes, signs) {
    
    let signLength = signs.length;

    let answer = 0;

    for( let i = 0; i < signLength; i++){
        signs[i] ? answer += absolutes[i] : answer -= absolutes[i]
    }


    return answer
}

/*
absolutes	signs	result
[4,7,12]	[true,false,true]	9
[1,2,3]	[false,false,true]	0
*/

console.log(
    solution([4,7,12],	[true,false,true])
)
console.log(
    solution([1,2,3],	[false,false,true])
)