function solution(n, lost, reserve) {
    var answer = 0;

    // 학생 수 만큼 array에 1씩 추가. 1은 체육복의 갯수
    let students = new Array(n).fill(1);
    
    // 놓고 온 학생의 체육복의 갯수 -1
    lost.forEach( item => {
        students[ item - 1] = students[ item - 1 ] -1;
    })

    //여유분 학생의 체육복 갯수 +1
    reserve.forEach( item => {
        students [ item - 1 ] = students [ item - 1 ] + 1;
    })
                                                                   
    //학생들 배열에서 순회.
    students.map( (item, index) => {

        // 현재 학생의 체육복 갯수가 0이고 앞에 번호 학생의 체육복 갯수가 2이상이면 실행.
        if( item == 0 && students[ index - 1] >= 2 ){
            students[ index -1 ] = students[ index -1 ] -1;
            students[ index ] = students[ index ] + 1;
        } 
        // 현재 학생의 체육복 갯수가 0이고 뒷번호 학생의 체육복 갯수가 2이상이면 실행.
        else if( item == 0 && students[ index + 1] >= 2){
            students[ index + 1 ] = students[ index + 1 ] -1;
            students[ index ] = students[ index ] + 1;
        }
    })

    // 학생들의 체육복 갯수가 1이상이면 answer에 1씩 더한다.
    students.forEach(item => item >= 1 && answer++)

    return answer;
}

// console.log(solution(2, [1], [1]));    // result : 2
console.log(solution(5, [2,4], [3]));        // result : 4
// console.log(solution(3, [3], [1]));          // result : 2
// console.log(solution(5, [3,6], [4,5]));      // result : 5
// console.log(solution(8, [3,4,5], [2,7]));    // result : 6
console.log(solution(7, [2, 3, 4], [1, 2, 3, 6])); // result : 6
// console.log(solution(5, [1, 2, 3], [ 2, 4 ]));// result : 4