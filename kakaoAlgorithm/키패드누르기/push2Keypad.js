'use strict'

let keyPad = {
    1 : [0,0], 2 : [0,1], 3 : [0,2],
    4 : [1,0], 5 : [1,1], 6 : [1,2],
    7 : [2,0], 8 : [2,1], 9 : [2,2],
    '*' : [3,0], 0 : [3,1], '#' : [3,2]
}

let location_left_hand = keyPad['*'];
let location_right_hand = keyPad['#'];

function solution(numbers, hand) {
    
    let answer = ''

    numbers.forEach(item => {
        // 눌린 키패드가 1,4,7일때
        if( item == 1 || item == 4 || item == 7){
            location_left_hand = keyPad[item];
            answer += 'L'
        } 
        // 눌린 키패드가 3,6,9일때
        else if( item == 3 || item == 6 || item == 9 ){
            location_right_hand = keyPad[item];
            answer += 'R'
        } 
        // 눌린 키패드가 2,5,8 0일때
        else{
            answer += getPushHand(keyPad[item],location_left_hand, location_right_hand, hand);
        }
    })
    return answer;
}

function getPushHand(pushKeyPad,leftHand, rightHand, mainHand){
    // 왼손의 움직인 횟수
    let move_left_hand = Math.abs(pushKeyPad[0] - leftHand[0]) + Math.abs(pushKeyPad[1] - leftHand[1]);
    // 오른손의 움직인 횟수
    let move_right_hand = Math.abs(pushKeyPad[0] - rightHand[0]) + Math.abs(pushKeyPad[1] - rightHand[1]);

    //움직인 횟수가 똑같다면
    if(move_left_hand == move_right_hand){
        switch(mainHand){
            case "left" :
                location_left_hand = pushKeyPad;
                return "L";
            case "right" :
                location_right_hand = pushKeyPad;
                return "R";
            default :
                throw Error;
        }
    }

    //움직인 횟수가 left가 더 작다.
    if(move_left_hand - move_right_hand < 0){
        location_left_hand = pushKeyPad;
        return "L";
    } else {
        location_right_hand = pushKeyPad;
        return "R"
    }
}

console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"));
console.log(solution([4,3,2,8,0,8], "right"));
console.log(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"));
