function solution(numbers = []) {
    var answer = '';

    numbers.sort((a,b)=>{

        let strA = String(a), strB = String(b)

        if (strA + strB > strB + strA){
            return -1
        }else {
            return 1
        }
    })

    if(numbers[0] == 0){
        return '0'
    }

    answer = String("".concat(numbers.join('')))

    return answer;
}


console.log(solution([0,0,0]))
console.log(solution([979, 97, 978, 81,818,817]))