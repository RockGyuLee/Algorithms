function solution(numbers) {
    let answer = -1;

    let filterNum = [0,1,2,3,4,5,6,7,8,9].filter( item => !numbers.includes(item))

    if(filterNum.length == 0) return answer

    answer = 0

    filterNum.forEach( item=>{
        answer += item
    })

    return answer;
}

/*

[1,2,3,4,6,7,8,0]	14
[5,8,4,0,6,7,9]	6

*/

console.log(solution([1,2,3,4,6,7,8,0]));
console.log(solution([5,8,4,0,6,7,9]));