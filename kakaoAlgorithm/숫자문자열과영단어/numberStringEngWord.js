/*
    카카오 숫자문자열과 영단어.
*/

// 0	zero
// 1	one
// 2	two
// 3	three
// 4	four
// 5	five
// 6	six
// 7	seven
// 8	eight
// 9	nine
'use strict';

let numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

function solution(s){
    var answer = s;
    for(let i = 0; i < numbers.length; i++) {
        
        let arr = answer.split(numbers[i]);
        console.log(arr,arr.join(i))
        answer = arr.join(i);
    }

    return answer;
}

// 내가 풀었던 코드.
// function solution(s) {
//     let answer = '';
    
//     let strArray = s.split('');

//     let translateWord = '';

//     for( let i = 0; i < strArray.length; i++){

//         let item = strArray[i]

//         if(Number.isInteger(Number.parseInt(item))) {
//             answer += item;
//             continue;
//         }

//         translateWord += item;

//         if(wordDictionary[translateWord]){
//             answer += wordDictionary[translateWord].toString();
//             translateWord = '';
//         }
//     }

//     return Number.parseInt(answer);
// }

console.log(solution("2three45sixseven"));
