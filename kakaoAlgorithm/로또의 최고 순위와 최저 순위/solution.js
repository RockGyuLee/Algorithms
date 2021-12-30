/*
    1	6개 번호가 모두 일치
    2	5개 번호가 일치
    3	4개 번호가 일치
    4	3개 번호가 일치
    5	2개 번호가 일치
    6(낙첨)	그 외
*/
function solution(lottos, win_nums) {

    let grade = [ 6, 6, 5, 4, 3, 2, 1]

    let zeroPoints = lottos.filter(item => item == 0);

    let succNumbers = lottos.filter( n => {
        return win_nums.find(nm => n==nm)
    })

    return [grade[succNumbers.length + zeroPoints.length],grade[succNumbers.length]]
}

/*

lottos	win_nums	result
[44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
[0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
[45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]

*/

console.log(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
console.log(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
console.log(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
